from ..clauses.multiclause        import MultiClause, expand_multiclause, create_multiclause, is_var
from ..clauses.multichainedclause import expand_multichainedclause, MultiChainClause
from ..clauses.chainedclause      import ChainClause

from ..tools.common_entries import common_entries

from collections import defaultdict

class Pattern(object):
    def __init__(self, predicates, inferred):
        self.predicates = predicates 
        self.inferred   = inferred
        self.variables  = defaultdict(list)

    def __str__(self):
        return 'if\n    {}\nthen\n    {}\n'.format(
                '\n    '.join(map(str, self.predicates)),
                '\n    '.join(map(str, self.inferred)))

    def process(self, field):
        if '@' in field:
            if field in self.variables:
                return self.variables[field]
            else:
                return ['*']
        else:
            return [field]

    def create_multiclause(self, clause):
        return MultiClause(*tuple(self.process(field) for field in clause))

    def to_queries(self, eclause):
        mc = self.create_multiclause(eclause.clause)
        chainDict = {k : self.create_multiclause(c) for k, vs in eclause.chained.items() for c in vs}
        mec = MultiChainClause(mc, chainDict)
        return expand_multichainedclause(mec)

    def compare_chains(self, a, b):
        if len(a.keys()) == 0:
            return False
        return sorted(list(a.keys())) == sorted(list(b.keys()))

    def add_variables(self, fields):
        for cfield, mfield in fields:
            if is_var(cfield): 
                self.variables[cfield].append(mfield)

    def fill_variables(self, database):
        for predicate in self.predicates:
            for query in self.to_queries(predicate):
                matches = database.get(query)
                for match in matches:
                    if self.compare_chains(predicate.chained, match.chained):
                        self.add_variables(zip(predicate.clause, match.clause))
                        for k, *vs in common_entries(predicate.chained, match.chained):
                            self.add_variables(zip(*vs))

    def get_inferred(self):
        for eclause in self.inferred:
            try:
                mc  = create_multiclause(eclause.clause, self.variables)
                chainDict = {k : create_multiclause(c, self.variables) for k, vs in eclause.chained.items() for c in vs}
                mec = MultiChainClause(mc, chainDict)
                for clause in expand_multichainedclause(mec):
                    yield clause
            except KeyError:
                pass

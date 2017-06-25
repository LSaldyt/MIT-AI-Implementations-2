from multiclause import MultiClause, expand_multiclause, create_multiclause, is_var
from multichainedclause import expand_multichainedclause, MultiChainClause
from chainedclause import ChainClause
from common_entries import common_entries

from collections import defaultdict

class Pattern(object):
    def __init__(self, predicates, inferred):
        self.predicates = predicates 
        self.inferred   = inferred
        self.variables  = defaultdict(set)

    def process(self, field):
        if '@' in field:
            if field in self.variables:
                return self.variables[field]
            else:
                return ['*']
        else:
            return [field]

    def to_queries(self, clause):
        mc = MultiClause(*tuple(self.process(field) for field in clause))
        return expand_multiclause(mc)

    def compare_chains(self, a, b):
        return set.issubset(set(a.keys()), set(b.keys()))

    def add_variables(self, fields):
        for cfield, mfield in fields:
            if is_var(cfield): 
                self.variables[cfield].add(mfield)

    def fill_variables(self, kmap):
        for predicate in self.predicates:
            for query in self.to_queries(predicate.clause):
                matches = kmap.get(ChainClause(query))
                for match in matches:
                    if self.compare_chains(predicate.chained, match.chained):
                        self.add_variables(zip(predicate.clause, match.clause))
                        for k, *vs in common_entries(predicate.chained, match.chained):
                            self.add_variables(zip(*vs))

    def get_inferred(self):
        for eclause in self.inferred:
            mc  = create_multiclause(eclause.clause, self.variables)
            chainDict = {k : create_multiclause(c, self.variables) for k, vs in eclause.chained.items() for c in vs}
            mec = MultiChainClause(mc, chainDict)

            '''
    for k, vs in mec.chaindict.items():
        for v in vs:
            expandedChainDict[k].append(expand_multiclause(v))
            '''

            for clause in expand_multichainedclause(mec):
                yield clause

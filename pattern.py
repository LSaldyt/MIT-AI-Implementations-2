from multiclause import MultiClause, expand_multiclause, create_multiclause, is_var
from multiextraclause import expand_multiextraclause, MultiExtraClause
from extraclause import ExtraClause
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

    def compare_extras(self, a, b):
        return set.issubset(set(a.keys()), set(b.keys()))

    def add_variables(self, fields):
        for cfield, mfield in fields:
            if is_var(cfield): 
                self.variables[cfield].add(mfield)

    def fill_variables(self, kmap):
        for predicate in self.predicates:
            for query in self.to_queries(predicate.clause):
                matches = kmap.get(ExtraClause(query))
                for match in matches:
                    if self.compare_extras(predicate.extra, match.extra):
                        self.add_variables(zip(predicate.clause, match.clause))
                        for k, *vs in common_entries(predicate.extra, match.extra):
                            self.add_variables(zip(*vs))

    def get_inferred(self):
        for eclause in self.inferred:
            mc  = create_multiclause(eclause.clause, self.variables)
            extraDict = {k : create_multiclause(c, self.variables) for k, vs in eclause.extra.items() for c in vs}
            mec = MultiExtraClause(mc, extraDict)

            '''
    for k, vs in mec.extradict.items():
        for v in vs:
            expandedExtraDict[k].append(expand_multiclause(v))
            '''

            for clause in expand_multiextraclause(mec):
                yield clause

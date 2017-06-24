from multiclause import MultiClause, expand_multiclause
from common_entries import common_entries

from collections import defaultdict

is_var = lambda s : '@' in s

class Pattern(object):
    def __init__(self, predicates, inferred):
        self.predicates = predicates 
        self.inferred   = inferred
        self.variables  = defaultdict(set)

    def to_queries(self, clause):
        def process(s):
            if '@' in s:
                if s in self.variables:
                    return self.variables[s]
                else:
                    return ['*']
            else:
                return [s]
        mc = MultiClause(*tuple(process(field) for field in clause))
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
                matches = kmap.get(query)
                for match, extra in matches:
                    if self.compare_extras(predicate.extra, extra):
                        self.add_variables(zip(predicate.clause, match))
                        for k, *vs in common_entries(predicate.extra, extra):
                            self.add_variables(zip(*vs))

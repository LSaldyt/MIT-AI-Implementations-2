from multiclause import MultiClause, expand_multiclause
from extraclause import ExtraClause
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
                matches = kmap.get(ExtraClause(query))
                for match in matches:
                    if self.compare_extras(predicate.extra, match.extra):
                        self.add_variables(zip(predicate.clause, match.clause))
                        for k, *vs in common_entries(predicate.extra, match.extra):
                            self.add_variables(zip(*vs))

    def get_inferred(self):
        for eclause in self.inferred:
            mc = MultiClause([], [], [])
            extras = defaultdict(set)
            broke = False
            for i, field in enumerate(eclause.clause):
                if is_var(field):
                    if field in self.variables:
                        for var in self.variables[field]:
                            mc[i].append(var)
                    else:
                        broke = True
                        break
                else:
                    mc[i].append(field)
            if broke:
                break

            for clause in expand_multiclause(mc):
                yield ExtraClause(clause, {})

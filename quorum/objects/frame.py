from .multiclause    import MultiClause, expand_multiclause, create_multiclause, is_var
from .multistatement import expand_multistatement, MultiStatement
from .statement      import Statement

from ..tools.common_entries import common_entries

from collections import defaultdict
from pprint import pprint

class Frame(object):
    def __init__(self, slots):
        self.slots     = slots 
        self.variables = defaultdict(list)
        self.locks     = defaultdict(lambda : False)

    def __str__(self):
        return '\n    '.join(map(str, self.slots))

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
        mc        = self.create_multiclause(eclause.clause)
        chainDict = {k : self.create_multiclause(c) for k, vs in eclause.chained.items() for c in vs}
        mec       = MultiStatement(mc, chainDict)
        return expand_multistatement(mec)

    def compare_chains(self, a, b):
        if len(a.keys()) == 0:
            return False
        return sorted(list(a.keys())) == sorted(list(b.keys()))

    def add_variables(self, fields):
        for cfield, mfield in fields:
            if is_var(cfield) and not self.locks[cfield]:
                self.variables[cfield].append(mfield)

    def fill_variables(self, database):
        for predicate in sorted(self.slots, key = lambda s : len(s), reverse=True):
            for query in self.to_queries(predicate):
                matches = database.get(query)
                print(query)
                #print(matches)
                for match in matches:
                    self.add_variables(zip(predicate.clause, match.clause))
                    if self.compare_chains(predicate.chained, match.chained):
                        for (k1, v1), (k2, v2) in zip(predicate.chained_items(), match.chained_items()):
                            self.add_variables(zip(v1, v2))
            for key in self.variables:
                self.locks[key] = True 
        pprint(self.variables)


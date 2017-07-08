from .clause         import Clause
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
        self.seen      = set()

    def __str__(self):
        return '\n    '.join(map(str, self.slots))

    def to_queries(self, eclause):
        mc        = create_multiclause(eclause.clause, self.variables)
        chainDict = {k : create_multiclause(c, self.variables) for k, c in eclause.chained_items()}
        mec       = MultiStatement(mc, chainDict)
        return expand_multistatement(mec)

    def compare_chains(self, a, b):
        if len(a.keys()) == 0:
            return False
        return sorted(list(a.keys())) == sorted(list(b.keys()))

    def add_variables(self, fields):
        for cfield, mfield in fields:
            if is_var(cfield) and cfield not in self.seen:
                self.variables[cfield].append(mfield)
                self.seen.add(cfield)
            elif cfield in self.seen:
                assert mfield in self.variables[cfield]


    def fill_variables(self, database):
        for predicate in sorted(self.slots, key = lambda s : len(s), reverse=True):
            print('predicate:')
            print('    {}'.format(predicate))
            for query in self.to_queries(predicate):
                print('query:')
                print('    {}'.format(query))
                matches = database.get(query)
                print('result:')
                for match in matches:
                    self.add_variables(zip(predicate.clause, match.clause))
                    if self.compare_chains(predicate.chained, match.chained):
                        for (k1, v1), (k2, v2) in zip(predicate.chained_items(), match.chained_items()):
                            self.add_variables(zip(v1, v2))
                    self.seen.clear()
        pprint(self.variables)


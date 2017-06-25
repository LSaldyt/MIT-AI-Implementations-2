from collections import defaultdict

from ..clauses.clause        import Clause
from ..clauses.multiclause   import MultiClause, expand_multiclause
from ..clauses.chainedclause import ChainClause

from ..structs.database      import DataBase

from .pattern import Pattern, is_var

class KnowledgeMap(object):
    def __init__(self):
        self.database  = DataBase()
        self.learned   = list()
        self.inferred  = list()

    def __str__(self):
        return str(self.database)

    def add(self, ec):
        self.database.add(ec)

    def get(self, ec):
        return self.database.get(ec)

    def teach(self, pattern):
        self.learned.append(pattern)

    def infer(self):
        for pattern in self.learned:
            pattern.fill_variables(self)
            self.inferred.extend(pattern.get_inferred())
        print(self.inferred)

    def ask(self, t):
        raise NotImplementedError('Self explanatory')

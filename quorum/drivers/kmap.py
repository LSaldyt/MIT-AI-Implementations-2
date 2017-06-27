from collections import defaultdict

from ..clauses.clause        import Clause
from ..clauses.multiclause   import MultiClause, expand_multiclause
from ..clauses.chainedclause import ChainClause

from ..structs.database import DataBase

from .pattern import Pattern, is_var

class KnowledgeMap(object):
    def __init__(self):
        self.database  = DataBase()
        self.learned   = list()

    def __str__(self):
        return 'KnowledgeMap:\n{}\n{}\n{}\n'.format(
                str(self.database),
                '_' * 80,
                '\n'.join(map(str, self.learned)))

    def add(self, ec):
        self.database.add(ec)

    def get(self, ec):
        return self.database.get(ec)

    def teach(self, pattern):
        self.learned.append(pattern)

    def infer(self):
        for pattern in self.learned:
            pattern.fill_variables(self)
            for item in pattern.get_inferred():
                self.add(item)

    def update(self, other):
        for clause in other.database.clauses():
            self.add(clause)
        for pattern in other.learned:
            self.learned.append(pattern)

    def ask(self, t):
        raise NotImplementedError('Self explanatory')

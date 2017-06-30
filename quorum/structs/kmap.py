from collections import defaultdict, Counter
from pprint      import pprint

from ..clauses.clause        import Clause
from ..clauses.multiclause   import MultiClause, expand_multiclause
from ..clauses.chainedclause import ChainClause

from ..pattern.pattern import Pattern, is_var

from .database   import DataBase
from .symboldict import SymbolDict

class KnowledgeMap(object):
    def __init__(self):
        self.database   = DataBase()
        self.symbolDict = SymbolDict()
        self.learned    = list()

    def __str__(self):
        return 'KnowledgeMap'

    def add(self, ec):
        if isinstance(ec, str):
            ec = ChainClause(ec)
        self.symbolDict.add(ec.clause.name)
        self.database.add(ec)

    def add_components(self, name, components):
        self.symbolDict.add(name, components)

    def get(self, ec):
        if isinstance(ec, str):
            ec = ChainClause(ec)
        return self.database.get(ec)

    def get_components(self, name, query='* * *'):
        return self.symbolDict.get(name, query)

    def elements(self, index):
        return [clause.item[index] for clause in self.database.clauses()]

    def teach(self, pattern):
        self.learned.append(pattern)

    def infer(self):
        for pattern in self.learned:
            pattern.fill_variables(self.database)
            for item in pattern.get_inferred():
                self.add(item)

    def update(self, other):
        for clause in other.database.clauses():
            self.add(clause)
        for pattern in other.learned:
            self.learned.append(pattern)

    def ask(self, t):
        raise NotImplementedError('Self explanatory')


from ..objects.statement import Statement

from .database        import DataBase
from .symbol_dict     import SymbolDict
from .pattern_library import PatternLibrary

class KnowledgeMap(object):
    def __init__(self):
        self.database       = DataBase()
        self.symbolDict     = SymbolDict()
        self.patternLibrary = PatternLibrary()

    def __str__(self):
        return 'KnowledgeMap'

    def add(self, ec):
        if isinstance(ec, str):
            ec = Statement(ec)
        self.symbolDict.add(ec.clause.name)
        self.database.add(ec)

    def add_components(self, name, components):
        self.symbolDict.add(name, components)

    def get(self, ec):
        if isinstance(ec, str):
            ec = Statement(ec)
        return self.database.get(ec)

    def get_components(self, name, query='* * *'):
        return self.symbolDict.get(name, query)

    def teach(self, pattern):
        self.patternLibrary.teach(pattern)

    def infer(self):
        for item in self.patternLibrary.get_inferences(self.database):
            self.add(item)

    def ask(self, t):
        raise NotImplementedError('Self explanatory')


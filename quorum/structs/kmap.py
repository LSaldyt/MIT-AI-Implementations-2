from collections import defaultdict

from ..objects.statement import Statement

from .database        import DataBase
from .symbol_dict     import SymbolDict
from .relation_dict   import RelationDict
from .pattern_library import PatternLibrary

class KnowledgeMap(object):
    def __init__(self):
        self.database       = DataBase()
        self.symbolDict     = SymbolDict()
        self.relationDict   = RelationDict()
        self.patternLibrary = PatternLibrary()

    def __str__(self):
        return 'KnowledgeMap'

    def add(self, ec):
        if isinstance(ec, str):
            ec = Statement(ec)
        self.symbolDict.add(ec.clause.name)
        self.relationDict.add(ec.clause.relation)
        self.database.add(ec)

    def add_components(self, name, components):
        self.symbolDict.add(name, components)

    def get(self, ec):
        if isinstance(ec, str):
            ec = Statement(ec)
        return self.database.get(ec)

    def get_components(self, name, query='* * *'):
        return self.symbolDict.get(name, query)

    def attrs(self, attr, clauses=None):
        if clauses is None:
            clauses = self.get('* * *')
        return {getattr(c.clause, attr) for c in clauses}

    def teach(self, pattern):
        self.patternLibrary.teach(pattern)

    def infer(self):
        for item in self.patternLibrary.get_inferences(self.database):
            self.add(item)

    def ask(self, t):
        raise NotImplementedError('Self explanatory')

    def references(self, root, depth):
        assert depth >= 0
        result  = dict()
        clauses = set.union(
                    self.get('{} * *'.format(root)),
                    self.get('* * {}'.format(root)))
        names   = set.union(
                    self.attrs('name', clauses),
                    self.attrs('node', clauses))
        names.discard(root)
        if depth == 0:
            return names
        else:
            searches = [self.references(name, depth - 1) 
                        for name in names]
            return set.union(names, *searches)

    def reference_dict(self, root, depth):
        result = dict()
        for i in range(depth):
            result[i] = self.references(root, i)
        return result

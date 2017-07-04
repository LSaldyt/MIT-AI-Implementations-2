from collections import defaultdict, Counter

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
        if attr is None:
            return clauses
        if isinstance(attr, str):
            return (getattr(c.clause, attr) for c in clauses)
        elif isinstance(attr, tuple):
            return (t for t in zip(*(self.attrs(a, clauses) for a in attr)))
        else:
            raise ValueError('Invalid attr {}'.format(attr))

    def teach(self, pattern):
        self.patternLibrary.teach(pattern)

    def infer(self):
        for item in self.patternLibrary.get_inferences(self.database):
            self.add(item)

    def ask(self, t):
        raise NotImplementedError('Self explanatory')

    def references(self, root, depth=0, attr=None):
        assert depth >= 0
        result  = dict()
        clauses = set.union(
                    self.get('{} * *'.format(root)),
                    self.get('* * {}'.format(root)))
        names   = set.union(
                    set(self.attrs('name', clauses)),
                    set(self.attrs('node', clauses)))
        if depth == 0:
            return set(self.attrs(attr, clauses))
        else:
            searches = [self.references(name, depth-1, attr=attr) 
                        for name in names]
            result = set.union(names, *searches)
            return result

    def reference_dict(self, root, depth=0):
        result = dict()
        for i in range(depth):
            result[i] = self.references(root, i)
        return result

    def build_classifier(self, classname, query='* isa {}'):
        query    = query.format(classname)
        examples = self.get(query)
        names    = set(self.attrs('name', examples))
        refs     = [self.references(name, attr=('relation', 'node')) for name in names]
        refs     = [item for s in refs for item in s]

        matches = Counter()
        matches.update(refs)
        print('matches')
        print(matches)
        nonExclusive = Counter()

        for ref in refs:
            refclauses = self.get('* {} {}'.format(*ref))
            refnames   = self.attrs('name', refclauses)
            for name in refnames:
                if name not in names:
                    nonExclusive[ref] += 1
        print('non exclusive counter')
        print(nonExclusive)
        print('Classification:')
        classifyCounter = matches - nonExclusive
        print(classifyCounter)

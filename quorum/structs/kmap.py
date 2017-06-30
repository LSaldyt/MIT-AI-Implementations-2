from collections import defaultdict, Counter
from pprint      import pprint

from ..clauses.clause        import Clause
from ..clauses.multiclause   import MultiClause, expand_multiclause
from ..clauses.chainedclause import ChainClause

from ..pattern.pattern import Pattern, is_var

from .database import DataBase

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
        if isinstance(ec, str):
            ec = ChainClause(ec)
        return self.database.get(ec)

    def elements(self, index):
        return [clause.item[index] for clause in self.database.clauses()]

    def relations_of(self, name):
        return self.get('{} * *'.format(name))

    def relations_to(self, search):
        results = self.get(search)
        retrieved = {cc.clause.name for cc in results}
        relations = (self.get('{} * *'.format(r)) for r in retrieved)
        relations = [set.difference(r, results) for r in relations]
        relations = [{'{} {}'.format(c.clause.relation, c.clause.node) for c in s} for s in relations]
        c = Counter()
        for s in relations:
            c.update(s)
        print(c)
        return relations

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


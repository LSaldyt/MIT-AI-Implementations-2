from collections import defaultdict
from clause      import Clause
from node        import Node


class DataBase(object):
    def __init__(self):
        self.dictionaries = []

    def __str__(self):
        return '\n'.join(str(node) for node in self.clauses())

    def __contains__(self, other):
        return len(self.get(other)) > 0

    def clauses(self):
        for clauseset in self.dictionaries[0].values():
            for clause in clauseset:
                yield clause

    def add(self, t):
        node = Node(t)
        for i, elem in enumerate(t):
            if len(self.dictionaries) < i + 1:
                self.dictionaries.append(defaultdict(set))
            self.dictionaries[i][elem].add(node)

    def get(self, t):
        if t == Clause('* * *'):
            return [node.item for node in self.clauses()]
        foundSets = []
        for i, elem in enumerate(t):
            if i + 1 > len(self.dictionaries):
                raise KeyError(
                        'DataBase can only be indexed by tuples ' + \
                        'equal or less in length to the tuples it stores')
            if elem != '*':
                foundSets.append(self.dictionaries[i][elem])
        if len(foundSets) == 0:
            return []
        found = set.intersection(*foundSets)
        return [node.item for node in found]





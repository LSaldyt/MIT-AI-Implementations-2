from collections import defaultdict

from ..objects.clause import Clause

class ClauseDataBase(object):
    def __init__(self):
        self.dictionaries = []

    def __str__(self):
        return '\n'.join(str(node) for node in self.clauses())

    def __repr__(self):
        return str(self)

    def __contains__(self, other):
        return len(self.get(other)) > 0

    def clauses(self):
        if len(self.dictionaries) > 0:
            for clauseset in self.dictionaries[0].values():
                for clause in clauseset:
                    yield clause

    def add(self, node, clause):
        for i, elem in enumerate(clause):
            if len(self.dictionaries) < i + 1:
                self.dictionaries.append(defaultdict(set))
            self.dictionaries[i][elem].add(node)

    def get(self, clause):
        if clause == Clause('* * *'):
            return [node.item for node in self.clauses()]
        foundSets = []
        for i, elem in enumerate(clause):
            if i + 1 > len(self.dictionaries):
                '''
                print('Warning: DataBase can only be indexed by tuples ' + \
                       'equal or less in length to the tuples it stores')
               '''
                return []
            if elem != '*':
                foundSets.append(self.dictionaries[i][elem])
        if len(foundSets) == 0:
            return []
        found = set.intersection(*foundSets)
        return [node.item for node in found]

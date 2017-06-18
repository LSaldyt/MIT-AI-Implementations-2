from collections import defaultdict

class Node(object):
    def __init__(self, item):
        self.item = item

    def __getattr__(self, attr):
        return getattr(self.item, attr)

class DataBase(object):
    def __init__(self):
        self.dictionaries = []

    def __str__(self):
        return '\n'.join(str(d) for d in self.dictionaries)

    def __contains__(self, other):
        return len(self.get(other)) > 0

    def add(self, t):
        node = Node(t)
        for i, elem in enumerate(t):
            if len(self.dictionaries) < i + 1:
                self.dictionaries.append(defaultdict(set))
            self.dictionaries[i][elem].add(node)

    def get(self, t):
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





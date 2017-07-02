from ..objects import Relation

class RelationDict(object):
    def __init__(self):
        self.relations= dict()

    def __getitem__(self, key):
        return self.relations[key]

    def add(self, name):
        if name not in self.relations:
            self.relations[name] = Relation(name)

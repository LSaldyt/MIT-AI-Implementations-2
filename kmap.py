from collections import defaultdict
from database import DataBase

class KnowledgeMap():
    
    def __init__(self):
        self.database = DataBase()
        self.extra    = defaultdict(lambda : defaultdict(set))

    def add(self, t, **kwargs):
        self.database.add(t)
        for k, v in kwargs.items():
            self.extra[t][k] = v

    def get(self, t):
        matches = self.database.get(t)
        matches = [(m, self.extra[m]) for m in matches]
        return matches




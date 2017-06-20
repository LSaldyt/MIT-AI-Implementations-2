from collections import defaultdict
from database    import DataBase
from clause      import Clause

class RelationMap(object):
    
    def __init__(self):
        self.database = DataBase()
        self.extra    = defaultdict(lambda : defaultdict(set))

    def __str__(self):
        render_defaultdict = lambda d : str(dict(d))
        s = ''
        for clause in self.database.clauses():
            s += '{} | {} '.format(clause, render_defaultdict(self.extra[clause.item]))
            s += '\n'
        return s

    def add(self, t, **kwargs):
        t = Clause(t)
        self.database.add(t)
        for k, v in kwargs.items():
            v = set(Clause(elem) for elem in v)
            self.extra[t][k].update(v)

    def get(self, t):
        t = Clause(t)
        matches = self.database.get(t)
        matches = [(m, self.extra[m]) for m in matches]
        return matches

    def pretty_get(self, t):
        print(t)
        print('_' * 47)
        matches = self.get(t)
        for match, extra in matches:
            print(match)
            if len(extra) > 0:
                print(extra)
        print('_' * 47)
                
    def query(self, t, check_extra=lambda e : True):
        t = Clause(t)
        match = t in self.database
        extra = self.extra[t]
        return match and check_extra(extra)

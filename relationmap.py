from collections import defaultdict
from database    import DataBase
from to_clause   import to_clause

class RelationMap(object):
    
    def __init__(self):
        self.database = DataBase()
        self.extra    = defaultdict(lambda : defaultdict(set))

    def __str__(self):
        render_defaultdict = lambda d : str(dict(d))
        s = ''
        for clauseset in self.database.clauses():
            for clause in clauseset:
                s += '{} | {} '.format(clause, render_defaultdict(self.extra[clause.item]))
                s += '\n'
        return s

    def add(self, t, **kwargs):
        t = to_clause(t)
        self.database.add(t)
        for k, v in kwargs.items():
            v = set(to_clause(elem) for elem in v)
            self.extra[t][k].update(v)

    def get(self, t):
        t = to_clause(t)
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
        t = to_clause(t)
        match = t in self.database
        extra = self.extra[t]
        return match and check_extra(extra)

    def create_extra_checker(self, field, function):
        def check(extra):
            for clause in extra[field]:
                if not getattr(self, function)(clause):
                    return False
            return True
        return check

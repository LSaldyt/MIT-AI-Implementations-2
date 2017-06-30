from collections  import namedtuple

from .clause import Clause

class Statement(object):
    def __init__(self, clause, chained=None):
        if chained is None:
            chained = dict()
        self.clause = Clause(clause)
        self.chained  = {k : {Clause(item) for item in v} for k, v in chained.items()}

    def __str__(self):
        if len(self.chained) < 1:
            return str(self.clause)
        return '{} {}'.format(self.clause, self.chained)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return ((self.clause,) + tuple(sorted(self.chained_items())) == 
                (self.clause,) + tuple(sorted(self.chained_items())))

    def __hash__(self):
        return hash((self.clause,) + tuple(sorted(self.chained_items())))

    def __getitem__(self, key):
        if isinstance(key, str):
            return self.clause._asdict()[key]
        return self.clause[key]

    def fields(self):
        return list(self.clause) + [clause for s in self.chained.values() for clause in s]

    def chained_items(self):
        return ((k, v) for k, vs in self.chained.items() for v in vs)

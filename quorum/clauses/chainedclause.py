from collections  import namedtuple

from .clause import Clause

class ChainClause(object):
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

    def fields(self):
        return list(self.clause) + [clause for subclauses in self.chained.values() for clause in subclauses]

    def chained_items(self):
        return ((k, v) for k, vs in self.chained.items() for v in vs)

from collections import namedtuple
from clause      import Clause

class ExtraClause(object):
    def __init__(self, clause, extra=None):
        if extra is None:
            extra = dict()
        self.clause = Clause(clause)
        self.extra  = {k : {Clause(item) for item in v} for k, v in extra.items()}

    def __str__(self):
        return '{} where {}'.format(self.clause, self.extra)

    def __repr__(self):
        return str(self)

    def fields(self):
        return list(self.clause) + [clause for subclauses in self.extra.values() for clause in subclauses]

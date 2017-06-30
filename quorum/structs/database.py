from collections import defaultdict

from .node        import Node

from ..clauses.clause        import Clause
from ..clauses.chainedclause import ChainClause

from .clausedb import ClauseDB

class DataBase(object):
    def __init__(self):
        self.clauseDB   = ClauseDB()
        self.chainDicts = defaultdict(ClauseDB)
        self.names      = set()

    def __str__(self):
        chainDictStr = '{}'.format(
                str(list(self.chainDicts.items()))
                )
        return '{}\n{}'.format(
                self.clauseDB,
                chainDictStr)

    def clauses(self):
        return self.clauseDB.clauses()

    def add(self, ec):
        if isinstance(ec, str):
            ec = ChainClause(ec)
        self.names.add(ec.clause.name)
        if ec in self.get(ec):
            return
        node = Node(ec)
        self.clauseDB.add(node, ec.clause)
        for k, v in ec.chained_items():
            self.chainDicts[k].add(node, v)

    def get(self, ec, strict=False):
        cresults = set(self.clauseDB.get(ec.clause))
        if not strict and len(ec.chained.items()) == 0:
            return cresults
        eresults = set()
        for k, v in ec.chained_items():
            for found in self.chainDicts[k].get(v):
                eresults.add(found)
        return set.intersection(cresults, eresults)

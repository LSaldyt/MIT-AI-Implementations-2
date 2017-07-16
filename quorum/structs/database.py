from collections import defaultdict

from .node        import Node

from ..objects.clause        import Clause
from ..objects.statement import Statement

from .clause_database import ClauseDataBase

class DataBase(object):
    def __init__(self):
        self.clauseDataBase   = ClauseDataBase()
        self.chainDicts = defaultdict(ClauseDataBase)
        self.names      = set()

    def __str__(self):
        return str(self.clauseDataBase)

    def clauses(self):
        return self.clauseDataBase.clauses()

    def add(self, ec):
        if isinstance(ec, str):
            ec = Statement(ec)
        self.names.add(ec.clause.name)
        if ec in self.get(ec):
            return
        node = Node(ec)
        self.clauseDataBase.add(node, ec.clause)
        for k, v in ec.chained_items():
            self.chainDicts[k].add(node, v)

    def get(self, ec, strict=False):
        cresults = set(self.clauseDataBase.get(ec.clause))
        if not strict and len(ec.chained.items()) == 0:
            return cresults
        eresults = set()
        for k, v in ec.chained_items():
            for found in self.chainDicts[k].get(v):
                eresults.add(found)
        return set.intersection(cresults, eresults)

from collections import defaultdict
from clause      import Clause
from extraclause import ExtraClause
from node        import Node

from clausedb import ClauseDB

class DataBase(object):
    def __init__(self):
        self.clauseDB   = ClauseDB()
        self.extraDicts = defaultdict(ClauseDB)

    def add(self, ec):
        node = Node(ec)
        self.clauseDB.add(node, ec.clause)
        for k, vs in ec.extra.items():
            for v in vs:
                self.extraDicts[k].add(node, v)

    def get(self, ec):
        cresults = set(self.clauseDB.get(ec.clause))
        if len(ec.extra.items()) == 0:
            return cresults
        eresults = set()
        for k, vs in ec.extra.items():
            for v in vs:
                for found in self.extraDicts[k].get(v):
                    eresults.add(found)
        return set.intersection(cresults, eresults)


if __name__ == '__main__':
    db = DataBase()
    db.add(ExtraClause('macbeth kill king', {'cause' : {'macbeth is weak'}}))
    print(db.get(ExtraClause('* kill *', {})))
    print(db.get(ExtraClause('* * *', {'cause' : {'* is weak'}})))

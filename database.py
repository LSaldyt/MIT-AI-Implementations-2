from collections import defaultdict
from clause      import Clause
from chainedclause import ChainClause
from node        import Node

from clausedb import ClauseDB

class DataBase(object):
    def __init__(self):
        self.clauseDB   = ClauseDB()
        self.chainDicts = defaultdict(ClauseDB)

    def add(self, ec):
        node = Node(ec)
        self.clauseDB.add(node, ec.clause)
        for k, v in ec.chained_items():
            self.chainDicts[k].add(node, v)

    def get(self, ec):
        cresults = set(self.clauseDB.get(ec.clause))
        if len(ec.chained.items()) == 0:
            return cresults
        eresults = set()
        for k, v in ec.chained_items():
            for found in self.chainDicts[k].get(v):
                eresults.add(found)
        return set.intersection(cresults, eresults)


if __name__ == '__main__':
    db = DataBase()
    db.add(ChainClause('macbeth kill king', {'cause' : {'macbeth is weak'}}))
    print(db.get(ChainClause('* kill *', {})))
    print(db.get(ChainClause('* * *', {'cause' : {'* is weak'}})))

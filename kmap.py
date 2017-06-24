from relationmap import RelationMap
from collections import defaultdict
from hash_dict   import hash_dict
from clause      import Clause
from multiclause import MultiClause, expand_multiclause
from extraclause import ExtraClause


from pattern import Pattern, is_var

class KnowledgeMap(object):
    def __init__(self):
        self.relations = RelationMap()
        self.learned   = list()
        self.inferred  = list()

    def __str__(self):
        return str(self.relations)

    def add(self, t, **kwargs):
        self.relations.add(t, **kwargs)

    def get(self, t):
        return self.relations.get(t)

    def teach(self, pattern):
        self.learned.append(pattern)


    def infer(self):
        for pattern in self.learned:
            pattern.fill_variables(self)
            self.inferred.extend(pattern.get_inferred())
        print(self.inferred)

    def ask(self, t):
        return False

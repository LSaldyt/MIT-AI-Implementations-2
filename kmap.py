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


    def add_inferred(self, infers, variables):
        for eclause in infers:
            mc = MultiClause([], [], [])
            extras = defaultdict(set)
            broke = False
            for i, field in enumerate(eclause.clause):
                if is_var(field):
                    if field in variables:
                        for var in variables[field]:
                            mc[i].append(var)
                    else:
                        broke = True
                        break
                else:
                    mc[i].append(field)
            if broke:
                break

            for clause in expand_multiclause(mc):
                print('adding {}'.format(clause))
                self.inferred.append(ExtraClause(clause, {})) # TODO: retain extra info in inferences

    def infer(self):
        for pattern in self.learned:
            pattern.fill_variables(self)
            self.add_inferred(pattern.inferred, pattern.variables)
        print(self.inferred)

    def ask(self, t):
        return False

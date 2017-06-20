from relationmap import RelationMap
from collections import defaultdict
from hash_dict   import hash_dict
from clause      import Clause
from multiclause import MultiClause, expand_multiclause
from extraclause import ExtraClause

from common_entries import common_entries

def to_queries(clause, variables):
    def process(s):
        if '@' in s:
            if s in variables:
                return variables[s]
            else:
                return ['*']
        else:
            return [s]
    mc = MultiClause(*tuple(process(field) for field in clause))
    return expand_multiclause(mc)

is_var = lambda s : '@' in s

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

    def teach(self, teachDict):
        teachDict = {k : v for k, v in teachDict.items()}
        self.learned.append(teachDict)

    def compare_extras(self, a, b):
        return set.issubset(set(a.keys()), set(b.keys()))

    def fill_variables(self, eclause, variables):
        for query in to_queries(eclause.clause, variables):
            matches = self.get(query)
            for match, extra in matches:
                if self.compare_extras(eclause.extra, extra):
                    for cfield, mfield in zip(eclause.clause, match):
                        if is_var(cfield):
                            variables[cfield].add(mfield)
                    for k, *vs in common_entries(eclause.extra, extra):
                        for cfield, mfield in zip(*vs):
                            if is_var(cfield):
                                variables[cfield].add(mfield)
                        #print('here k:{} vs:{}'.format(k, vs))

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
        for teachDict in self.learned:
            variables = defaultdict(set)
            predicates = teachDict['if']
            for predicate in predicates:
                self.fill_variables(predicate, variables)
            print(variables)
            self.add_inferred(teachDict['then'], variables)
        print(self.inferred)

    def ask(self, t):
        return False

from relationmap import RelationMap
from collections import defaultdict, namedtuple
from to_clause   import to_clause, Clause

MultiClause = namedtuple('MultiClause', ['names', 'relations', 'nodes'])

def score_concreteness(clause):
    return sum([(1 if '@' not in field else 0) for field in clause])

def to_queries(clause, variables):
    def process(s):
        if '@' in s:
            if s in variables:
                return variables[s]
            else:
                return ['*']
        else:
            return [s]
    mc      = MultiClause(*tuple(process(field) for field in clause))
    queries = []
    for name in mc.names:
        for relation in mc.relations:
            for node in mc.nodes:
                queries.append(Clause(name, relation, node))
    return queries 

is_var = lambda s : '@' in s

class KnowledgeMap(object):
    def __init__(self):
        self.relations = RelationMap()
        self.learned   = list()

    def __str__(self):
        return str(self.relations)

    def add(self, t, **kwargs):
        self.relations.add(t, **kwargs)

    def get(self, t):
        return self.relations.get(t)

    def teach(self, teachDict):
        process = lambda v : {to_clause(s) for s in v}
        teachDict = {k : process(v) for k, v in teachDict.items()}
        self.learned.append(teachDict)

    def fill_variables(self, clause, variables):
        for query in to_queries(clause, variables):
            matches = self.get(query)
            for match, extra in matches:
                for cfield, mfield in zip(clause, match):
                    if is_var(cfield):
                        variables[cfield].add(mfield)

    def add_inferred(self, infers, variables):
        for clause in infers:
            mc = MultiClause([], [], [])
            for i, field in enumerate(clause):
                if field in variables:
                    for var in variables[field]:
                        mc[i].append(var)
                else:
                    mc[i].append(field)
            for name in mc.names:
                for relation in mc.relations:
                    for node in mc.nodes:
                        self.add(Clause(name, relation, node))

    def infer(self):
        for teachDict in self.learned:
            variables = defaultdict(set)
            predicates = sorted(teachDict['if'], key=score_concreteness, reverse=True)
            for predicate in predicates:
                self.fill_variables(predicate, variables)
            self.add_inferred(teachDict['then'], variables)

    def ask(self, t):
        return False

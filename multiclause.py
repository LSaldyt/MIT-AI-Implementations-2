from collections import namedtuple
from clause      import Clause
MultiClause = namedtuple('MultiClause', ['names', 'relations', 'nodes'])

def expand_multiclause(mc):
    clauses = []
    for name in mc.names:
        for relation in mc.relations:
            for node in mc.nodes:
                clauses.append(Clause(name, relation, node))
    return clauses 

from collections import namedtuple, defaultdict

from .clause import Clause

from ..tools.subsets import subsets

MultiClause = namedtuple('MultiClause', ['names', 'relations', 'nodes'])

is_var = lambda s : '@' in s

def expand_multiclause(mc):
    clauses = []
    for name, relation, node in zip(mc.names, mc.relations, mc.nodes):
        clauses.append(Clause(name, relation, node))
    return clauses

def expand_multiclauses(mcs):
    expanded = [expand_multiclause(mc) for mc in mcs]
    return subsets(expanded)

def create_multiclause(clause, variables):
    mc = MultiClause([], [], [])
    l = 1
    for i, field in enumerate(clause):
        if is_var(field):
            if field in variables:
                fieldvals = variables[field]
                l         = max(len(fieldvals), l)
                for val in fieldvals:
                    mc[i].append(val)
            else:
                mc[i].append('*')
        else:
            mc[i].append(field)
    for i in range(len(clause)):
        if len(mc[i]) < l:
            mc[i].extend(mc[i] * (l - len(mc[i])))
    return mc

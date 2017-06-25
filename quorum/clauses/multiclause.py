from collections import namedtuple, defaultdict

from .clause import Clause

from ..tools.subsets import all_subsets

MultiClause = namedtuple('MultiClause', ['names', 'relations', 'nodes'])

is_var = lambda s : '@' in s

def expand_multiclause(mc):
    clauses = []
    for name in mc.names:
        for relation in mc.relations:
            for node in mc.nodes:
                clauses.append(Clause(name, relation, node))
    return clauses

def expand_multiclauses(mcs):
    expanded = [expand_multiclause(mc) for mc in mcs]
    return all_subsets(expanded)

def create_multiclause(clause, variables):
    mc = MultiClause([], [], [])
    for i, field in enumerate(clause):
        if is_var(field):
            if field in variables:
                for var in variables[field]:
                    mc[i].append(var)
            else:
                raise KeyError('The field {} was not filled for the pattern-clause {}'.format(field, clause))
        else:
            mc[i].append(field)
    return mc

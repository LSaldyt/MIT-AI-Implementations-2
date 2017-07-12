from collections import namedtuple, defaultdict

from .clause        import Clause
from .multiclause   import MultiClause, expand_multiclause, expand_multiclauses, create_multiclause
from .statement import Statement

from ..tools.subsets import subsets

MultiStatement = namedtuple('MultiStatement', ['root', 'chaindict'])

def expand_multistatement(mec):
    roots             = expand_multiclause(mec.root)
    expandedChainDict = defaultdict(list)

    for k, v in mec.chaindict.items():
        expandedChainDict[k].append(v)
    for root in roots:
        kvs = []
        for k, chainClauses in expandedChainDict.items():
            for subset in expand_multiclauses(chainClauses):
                for item in subset:
                    kvs.append((k, set(item)))
        if len(kvs) == 0:
            yield Statement(root, dict())
        for subset in subsets(kvs):
            if len(subset) > 0:
                yield Statement(root, dict(subset))

def expand_from_vars(statement, variables):
    mc        = create_multiclause(statement.clause, variables)
    chainDict = {k : create_multiclause(c, variables) for k, c in statement.chained_items()}
    mec       = MultiStatement(mc, chainDict)
    return expand_multistatement(mec)

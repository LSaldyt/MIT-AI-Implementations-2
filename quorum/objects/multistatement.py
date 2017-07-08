from collections import namedtuple, defaultdict

from .clause        import Clause
from .multiclause   import MultiClause, expand_multiclause, expand_multiclauses
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

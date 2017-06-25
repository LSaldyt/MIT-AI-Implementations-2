from collections import namedtuple, defaultdict

from .clause        import Clause
from .multiclause   import MultiClause, expand_multiclause, expand_multiclauses
from .chainedclause import ChainClause

from ..tools.subsets import all_subsets

MultiChainClause = namedtuple('MultiChainClause', ['root', 'chaindict'])

def expand_multichainedclause(mec):
    roots = expand_multiclause(mec.root)
    expandedChainDict = defaultdict(list)
    for k, v in mec.chaindict.items():
        expandedChainDict[k].append(v)
    for root in roots:
        kvs = []
        for k, chainClauses in expandedChainDict.items():
            for subset in expand_multiclauses(chainClauses):
                for item in subset:
                    kvs.append((k, set(item)))
        for subset in all_subsets(kvs):
            yield ChainClause(root, dict(subset))

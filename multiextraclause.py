from collections import namedtuple, defaultdict
from clause      import Clause
from multiclause import MultiClause, expand_multiclause, expand_multiclauses
from extraclause import ExtraClause
from subsets     import all_subsets

MultiExtraClause = namedtuple('MultiExtraClause', ['root', 'extradict'])

def expand_multiextraclause(mec):
    roots = expand_multiclause(mec.root)
    expandedExtraDict = defaultdict(list)
    for k, v in mec.extradict.items():
        expandedExtraDict[k].append(v)
    for root in roots:
        kvs = []
        for k, extraClauses in expandedExtraDict.items():
            for subset in expand_multiclauses(extraClauses):
                for item in subset:
                    kvs.append((k, set(item)))
        for subset in all_subsets(kvs):
            yield ExtraClause(root, dict(subset))

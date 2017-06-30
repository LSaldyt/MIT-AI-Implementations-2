#!/usr/bin/env python3
from quorum import KnowledgeMap
from quorum.clauses.chainedclause import ChainClause

from quorum.parse import parse_text

from quorum.symbol import Symbol

def main(args):
    kmap = KnowledgeMap()
    kmap.add('apple isa fruit')
    kmap.add_components(
            'apple', 
       ['body shape round',
        'body size fist',
        'body color red',
        'body taste tart',
        'body taste sweet',
        'stem color brown'])
    print(kmap.symbolDict['apple'])

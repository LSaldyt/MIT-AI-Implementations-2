#!/usr/bin/env python3
from quorum import KnowledgeMap
from quorum import Pattern

from quorum.clauses.chainedclause import ChainClause

def conditionality(args):
    kmap = KnowledgeMap()
    kmap.add(ChainClause('sky is cloudy', {'condition' : {'weather is raining'}}))
    kmap.add(ChainClause('weather is raining'))

    kmap.teach(Pattern(
        [ChainClause('@x @rel1 @y', {'condition' : {'@x @rel2 @c'}}), ChainClause('@x @rel2 @c', {})],
        [ChainClause('@x @rel1 @y', {})]
        ))

    kmap.infer()
    print(kmap)

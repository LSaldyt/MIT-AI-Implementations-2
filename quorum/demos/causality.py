#!/usr/bin/env python3
from quorum.kmap          import KnowledgeMap
from quorum.pattern       import Pattern

from quorum.clauses.chainedclause import ChainClause

def causality(args):
    kmap = KnowledgeMap()
    kmap.add(ChainClause('macbeth kill king', {'cause' : {'macbeth want-to-be king'}}))
    kmap.add(ChainClause('mystery-person want-to-be king'))

    kmap.teach(Pattern(
        [ChainClause('@x @rel1 @y', {'cause' : {'@x @rel2 @c'}}), ChainClause('@z @rel2 @c', {})],
        [ChainClause('@z @rel1 @y', {'cause' : {'@z @rel2 @c'}})]
        ))

    kmap.infer()

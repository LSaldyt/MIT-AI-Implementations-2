#!/usr/bin/env python3
from quorum import KnowledgeMap
from quorum import Pattern

from quorum.clauses.chainedclause import ChainClause

def syllogism(args):
    kmap = KnowledgeMap()
    kmap.add(ChainClause('socrates isa man'))
    kmap.add(ChainClause('man is mortal'))

    kmap.teach(Pattern(
        [ChainClause('@x isa @y', {}), ChainClause('@y @rel @z', {})],
        [ChainClause('@x @rel @z', {'cause' : {'@x isa @y'}})]
        ))

    kmap.infer()

#!/usr/bin/env python3
from quorum import KnowledgeMap
from quorum.parse import parse_text

from quorum.clauses.chainedclause import ChainClause

def event(args):
    text = '''
    event hasa time
    event hasa location
    wedding isa event
    '''
    kmap = parse_text(text)
    # Inheritance
    kmap.teach(Pattern(
        [ChainClause('@x isa @y', {}), ChainClause('@y @rel @z', {})],
        [ChainClause('@x @rel @z', {'cause' : {'@x isa @y'}})]
        ))
    kmap.teach(Pattern(
        [ChainClause('@class hasa @elem'), ChainClause('@instance isa @class')]
        [ChainClause('@instance @elem ?')]
        ))
    print(kmap)

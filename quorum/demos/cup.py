#!/usr/bin/env python3
from quorum import KnowledgeMap
from quorum.clauses.chainedclause import ChainClause

from quorum.parse import parse_text

def cup(args):
    story = '''
    brick is stable because brick hasa flatbottom.
    brick is heavy.
    glass carries liquid.
    glass hasa handle.
    glass enables drinking because glass hasa handle and glass carries liquid.
    glass is pretty.
    briefcase is liftable because briefcase hasa handle and briefcase is light.
    briefcase is useful because briefcase holds papers.
    briefcase enables organization because briefcase holds papers.
    bowl carries liquid because bowl hasa concavity.
    bowl contains cherry-soup.
    cup is stable.
    cup enables drinking.
    object ismadeof porcelain.
    object hasa decoration.
    object hasa concavity.
    '''
    kmap = parse_text(story)
    print(kmap)

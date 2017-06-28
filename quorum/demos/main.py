#!/usr/bin/env python3
from quorum import KnowledgeMap
from quorum.clauses.chainedclause import ChainClause

from quorum.parse import parse_text

def main(args):
    story = '''
    car1 isa car.
    car1 is red.
    car2 isa car.
    car2 is red.
    car3 isa car.
    car3 is blue.
    '''
    kmap = parse_text(story)
    print(kmap)
    print(kmap.elements('name'))
    print(kmap.relations_to())
    print(kmap.relations_to(indexstr='* is red'))
    print(kmap.relations_to(indexstr='* isa car'))

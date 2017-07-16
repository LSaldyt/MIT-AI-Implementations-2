#!/usr/bin/env python3
from quorum import KnowledgeMap
from quorum.objects import Statement, Pattern
from quorum.parse import parse_text
from quorum.parse import parse_file

def main(args):
    info = '''
    poles on-end-of magnet.
    terminals on-end-of battery.
    '''
    kmap = parse_text(info)
    kmap.shared('poles', 'terminals')
    info = '''
    a is-a cup.
    a is small.
    b is-a cup.
    b is large.
    c is-a bowl.
    c is small.
    d is-a bowl.
    d is large.
    '''
    kmap = parse_text(info)
    kmap.shared('a', 'c')
    info = '''
    tuna is-a fish.
    fish is-a animal.
    labrador is-a dog.
    dog is-a animal.
    '''
    kmap = parse_text(info)
    kmap.shared('tuna', 'labrador', depth=0)
    kmap.shared('tuna', 'labrador', depth=1)


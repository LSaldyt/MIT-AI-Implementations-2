#!/usr/bin/env python3
from quorum import KnowledgeMap

from quorum.parse import parse_file

def syllogism(args):
    kmap = parse_file('data/syllogism.txt')
    kmap.infer()
    print(kmap)

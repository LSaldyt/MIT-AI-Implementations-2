#!/usr/bin/env python3
from quorum import KnowledgeMap

from quorum.parse import parse_file

def read(args):
    for filename in args:
        kmap = parse_file(filename)
        kmap.infer()
        print(kmap)

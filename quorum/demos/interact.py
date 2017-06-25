#!/usr/bin/env python3
from quorum import KnowledgeMap

from quorum.parse import parse_text

def interact(args):
    kmap = KnowledgeMap()
    while True:
        text = input('\n>')
        kmap.update(parse_text(text))
        print(kmap)

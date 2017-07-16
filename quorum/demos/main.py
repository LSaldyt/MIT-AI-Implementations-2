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
    kmap.shared_relations('poles', 'terminals')

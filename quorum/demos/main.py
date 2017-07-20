#!/usr/bin/env python3
from quorum import KnowledgeMap
from quorum.objects import Statement, Pattern
from quorum.parse import parse_text
from quorum.parse import parse_file

def main(args):

    info = '''
    poles on-end-of magnet.
    terminals on-end-of battery.
    battery holds charge.
    magnet attracts objects.
    magnet repels objects.
    acid inside-of battery.
    '''
    kmap = parse_text(info)
    #kmap.shared('poles', 'terminals')
    kmap.compare('poles', 'terminals', 'acid')
    kmap.compare('battery', 'poles', 'acid', 'terminals')
    kmap.compare('battery', 'acid', 'terminals')

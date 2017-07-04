#!/usr/bin/env python3
from quorum import KnowledgeMap
from quorum.objects import Statement, Pattern
from quorum.parse import parse_text

def main(args):
    kmap = KnowledgeMap()
    kmap.add('duck has feathers')
    kmap.add('duck has bill')
    kmap.add('duck isa bird')
    kmap.add('duck can swim')
    kmap.add('platapus has bill')
    kmap.add('platapus can swim')
    kmap.add('platapus lays eggs')
    kmap.add('snake lays eggs')
    kmap.add('human can talk')
    kmap.add('parrot has feathers')
    kmap.add('parrot isa bird')
    kmap.add('parrot can talk')
    kmap.build_classifier('bird')

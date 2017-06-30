#!/usr/bin/env python3
from quorum import KnowledgeMap
from quorum.clauses.chainedclause import ChainClause

from quorum.parse import parse_text

from quorum.symbol import Symbol

def main(args):
    apple = Symbol('apple')
    apple.components.add('body shape round')
    apple.components.add('body size fist')
    apple.components.add('body color red')
    apple.components.add('body taste tart')
    apple.components.add('body taste sweet')
    apple.components.add('stem color brown')
    print('apple:')
    print(apple)
    print('component database:')
    print(apple.components)

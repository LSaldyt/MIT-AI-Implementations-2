#!/usr/bin/env python3
from quorum import KnowledgeMap
from quorum.objects import Statement, Pattern
from quorum.parse import parse_text

def main(args):
    kmap = KnowledgeMap()
    kmap.add('apple isa fruit')
    kmap.add_components(
            'apple', 
       ['body shape round',
        'body size fist',
        'body color red',
        'body taste tart',
        'body taste sweet',
        'stem color brown'])
    print(kmap.symbolDict['apple'])
    kmap.add('fruit is edible')
    kmap.add('apple is edible')
    kmap.add('apple grows-on tree')
    kmap.add('tree grow-in ground')
    kmap.add_components('tree',
            ['truck is round',
             'leaves are green',
             'bark is rough'])
    kmap.teach(Pattern({'@x isa @y', '@y is @z'}, {'@x is @z'}))
    print('Name reference trees by depth:')
    referenceDict = kmap.reference_dict('apple', 3)
    print(referenceDict)

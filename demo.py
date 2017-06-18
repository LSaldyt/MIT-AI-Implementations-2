#!/usr/bin/env python3
from kmap import KnowledgeMap

def demo():
    '''
    Why can you pull something with a string but not push it?
    '''
    kmap = KnowledgeMap()
    kmap.add('string can force-transfer', **{'conditions':{'string is taut'}})
    kmap.add('lever can force-transfer',  **{'causes':{'lever is solid'}})

    print(kmap.get('* can force-transfer'))

    check_condition = kmap.create_extra_checker('conditions', 'query')

    print(kmap.query('string can force-transfer', check_condition))
    kmap.add('string is taut')
    print(kmap.query('string can force-transfer', check_condition))

if __name__ == '__main__':
    demo()

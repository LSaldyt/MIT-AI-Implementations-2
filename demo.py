#!/usr/bin/env python3
from kmap import KnowledgeMap

def demo():
    '''
    Why can you pull something with a string but not push it?
    '''
    km = KnowledgeMap()
    km.add_str('string can force-transfer when taut')
    km.add_str('string is taut when pulling')
    km.add_str('push isa movement')
    km.add_str('pull isa movement')
    km.add_str('movement requires force-transfer')
    km.add_str('string is pulling')

    print(km.get_str('* can force-transfer'))
    print(km.get_str('* requires force-transfer'))

if __name__ == '__main__':
    demo()

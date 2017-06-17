#!/usr/bin/env python3
from kmap import KnowledgeMap

def demo():
    '''
    Why can you pull something with a string but not push it?
    '''
    km = KnowledgeMap()
    km.add(('string', 'can', 'force-transfer'), conditions={'taut'})
    km.add(('lever', 'can', 'force-transfer'), causes={'solid'})

    print(km.get(('*', 'can', 'force-transfer')))

if __name__ == '__main__':
    demo()

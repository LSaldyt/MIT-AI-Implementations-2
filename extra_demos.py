#!/usr/bin/env python3
from kmap import KnowledgeMap

def common_sense():
    '''
    Why can you pull something with a string but not push it?

    Obviously a work in progress
    '''
    kmap = KnowledgeMap()
    kmap.add('string can force-transfer', **{'conditions':{'string is taut'}})
    kmap.add('lever can force-transfer',  **{'causes':{'lever is solid'}})

    print(kmap.get('* can force-transfer'))

    check_condition = kmap.create_extra_checker('conditions', 'query')

    print(kmap.query('string can force-transfer', check_condition))
    kmap.add('string is taut')
    print(kmap.query('string can force-transfer', check_condition))

def syllogism():
    kmap = KnowledgeMap()
    kmap.add('socrates isa man')
    kmap.add('man is mortal')
    kmap.infer()
    print(kmap.query('socrates is mortal'))

def description_matching():
    kmap = KnowledgeMap()
    kmap.add('firetruck isa vehicle')
    kmap.add('firetruck is red')
    kmap.add('firetruck is metal')
    kmap.add('apple isa fruit')
    kmap.add('apple is red')
    kmap.add('apple is round')

    kmap.pretty_get('* is red')
    kmap.pretty_get('* is round')
if __name__ == '__main__':
    #print('common sense')
    #common_sense()
    #print('syllogism')
    #syllogism()
    print('description')
    description_matching()

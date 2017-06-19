#!/usr/bin/env python3
from relationmap import RelationMap

def common_sense():
    '''
    Why can you pull something with a string but not push it?

    Obviously a work in progress
    '''
    relationmap = RelationMap()
    relationmap.add('string can force-transfer', **{'conditions':{'string is taut'}})
    relationmap.add('lever can force-transfer',  **{'causes':{'lever is solid'}})

    print(relationmap.get('* can force-transfer'))

    check_condition = relationmap.create_extra_checker('conditions', 'query')

    print(relationmap.query('string can force-transfer', check_condition))
    relationmap.add('string is taut')
    print(relationmap.query('string can force-transfer', check_condition))

def syllogism():
    relationmap = RelationMap()
    relationmap.add('socrates isa man')
    relationmap.add('man is mortal')
    #relationmap.infer()
    #print(relationmap.query('socrates is mortal'))

def description_matching():
    relationmap = RelationMap()
    relationmap.add('firetruck isa vehicle')
    relationmap.add('firetruck is red')
    relationmap.add('firetruck is metal')
    relationmap.add('apple isa fruit')
    relationmap.add('apple is red')
    relationmap.add('apple is round')

    relationmap.pretty_get('* is red')
    relationmap.pretty_get('* is round')
if __name__ == '__main__':
    #print('common sense')
    #common_sense()
    #print('syllogism')
    #syllogism()
    print('description')
    description_matching()

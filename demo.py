#!/usr/bin/env python3
from kmap        import KnowledgeMap
from chainedclause import ChainClause
from pattern     import Pattern

def teach_syllogism():
    kmap = KnowledgeMap()
    kmap.add(ChainClause('socrates isa man'))
    kmap.add(ChainClause('man is mortal'))

    kmap.teach(Pattern(
        [ChainClause('@x isa @y', {}), ChainClause('@y @rel @z', {})],
        [ChainClause('@x @rel @z', {'cause' : {'@x isa @y'}})]
        ))

    kmap.infer()
    #kmap.ask('socrates is mortal')

def teach_conditionality():
    kmap = KnowledgeMap()
    kmap.add('sky is cloudy', **{'condition' : {'weather is raining'}})
    kmap.add('weather is raining')

    kmap.teach(Pattern(
        [ChainClause('@x @rel1 @y', {'condition' : {'@x @rel2 @c'}}), ChainClause('@x @rel2 @c', {})],
        [ChainClause('@x @rel1 @y', {})]
        ))

    kmap.infer()

def teach_causality():
    kmap = KnowledgeMap()
    kmap.add('macbeth kill king', **{'cause' : {'macbeth want-to-be king'}})
    kmap.add('mystery-person want-to-be king')

    kmap.teach(Pattern(
        [ChainClause('@x @rel1 @y', {'cause' : {'@x @rel2 @c'}}), ChainClause('@z @rel2 @c', {})],
        [ChainClause('@z @rel1 @y', {'cause' : {'@z @rel2 @c'}})]
        ))

    kmap.infer()

if __name__ == '__main__':
    teach_syllogism()
    #teach_conditionality()
    #teach_causality()

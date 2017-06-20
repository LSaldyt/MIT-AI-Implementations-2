#!/usr/bin/env python3
from kmap        import KnowledgeMap
from extraclause import ExtraClause

def teach_syllogism():
    kmap = KnowledgeMap()
    kmap.add('socrates isa man')
    kmap.add('man is mortal')

    kmap.teach({
        'if'   : [ExtraClause('@x isa @y', {}), ExtraClause('@y @rel @z', {})],
        'then' : [ExtraClause('@x @rel @z', {})]
        })

    kmap.infer()
    #print(kmap)
    kmap.ask('socrates is mortal')

def teach_conditionality():
    kmap = KnowledgeMap()
    kmap.add('sky is cloudy', **{'condition' : {'weather is raining'}})
    kmap.add('weather is raining')

    kmap.teach({
        'if'   : [ExtraClause('@x @rel1 @y', {'condition' : {'@x @rel2 @c'}}), ExtraClause('@x @rel2 @c', {})],
        'then' : [ExtraClause('@x @rel1 @y', {})]
        })

    kmap.infer()
    #print(kmap)

def teach_causality():
    kmap = KnowledgeMap()
    kmap.add('macbeth kill king', **{'cause' : {'macbeth want-to-be king'}})
    kmap.add('mystery-person want-to-be king')

    kmap.teach({
        'if'   : [ExtraClause('@x @rel1 @y', {'cause' : {'@x @rel2 @c'}}), ExtraClause('@z @rel2 @c', {})],
        'then' : [ExtraClause('@z @rel1 @y', {'cause' : {'@z @rel2 @c'}})]
        })

    kmap.infer()

if __name__ == '__main__':
    teach_syllogism()
    teach_conditionality()
    teach_causality()

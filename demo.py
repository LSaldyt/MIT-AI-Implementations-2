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

if __name__ == '__main__':
    teach_syllogism()
    teach_conditionality()

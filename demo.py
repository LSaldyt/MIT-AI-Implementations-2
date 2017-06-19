#!/usr/bin/env python3
from kmap import KnowledgeMap

def demo():
    kmap = KnowledgeMap()
    kmap.add('socrates isa man')
    kmap.add('man is mortal')

    kmap.teach({
        'if'   : {'@x isa @y', '@y @rel @z'},
        'then' : {'@x @rel @z'}
        })

    kmap.infer()
    print(kmap)
    kmap.ask('socrates is mortal')

if __name__ == '__main__':
    demo()

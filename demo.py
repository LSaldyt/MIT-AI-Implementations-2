#!/usr/bin/env python3
from kmap import KnowledgeMap

def cup():
    kmap = KnowledgeMap()
    kmap.add('brick is stable', **{'causes':{'brick hasa flatbottom'}})
    kmap.add('brick is heavy')
    kmap.add('glass enables drinking', **{'causes':{'glass hasa handle', 'glass carries liquid'}})
    kmap.add('glass is pretty')
    kmap.add('briefcase is liftable', **{'causes' : {'briefcase has handle', 'briefcase is light'}})
    kmap.add('briefcase is useful', **{'causes' : {'briefcase holds papers'}})
    kmap.add('briefcase enables organization', **{'causes' : {'briefcase holds papers'}})
    kmap.add('bowl carries liquid', **{'causes' : {'bowl hasa concavity'}})
    kmap.add('bowl contains cherry-soup')
    kmap.add('cup is stable')
    kmap.add('cup enables drinking')
    kmap.add('mystery-object madeof porcelain')
    kmap.add('mystery-object hasa decoration')
    kmap.add('mystery-object hasa concavity')
    print(kmap)

if __name__ == '__main__':
    cup()

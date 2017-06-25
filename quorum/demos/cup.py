#!/usr/bin/env python3
from quorum.kmap import KnowledgeMap
from quorum.clauses.chainedclause import ChainClause

def cup(args):
    kmap = KnowledgeMap()
    kmap.add(ChainClause('brick is stable', {'causes':{'brick hasa flatbottom'}}))
    kmap.add(ChainClause('brick is heavy'))
    kmap.add(ChainClause('glass carries liquid'))
    kmap.add(ChainClause('glass hasa handle'))
    kmap.add(ChainClause('glass enables drinking', {'causes':{'glass hasa handle', 'glass carries liquid'}}))
    kmap.add(ChainClause('glass is pretty'))
    kmap.add(ChainClause('briefcase is liftable', {'causes' : {'briefcase has handle', 'briefcase is light'}}))
    kmap.add(ChainClause('briefcase is useful', {'causes' : {'briefcase holds papers'}}))
    kmap.add(ChainClause('briefcase enables organization', {'causes' : {'briefcase holds papers'}}))
    kmap.add(ChainClause('bowl carries liquid', {'causes' : {'bowl hasa concavity'}}))
    kmap.add(ChainClause('bowl contains cherry-soup'))
    kmap.add(ChainClause('cup is stable'))
    kmap.add(ChainClause('cup enables drinking'))
    kmap.add(ChainClause('mystery-object madeof porcelain'))
    kmap.add(ChainClause('mystery-object hasa decoration'))
    kmap.add(ChainClause('mystery-object hasa concavity'))
    print(kmap)

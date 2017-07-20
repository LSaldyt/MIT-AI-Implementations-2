kmap = KnowledgeMap()
kmap.add('duck has feathers')
kmap.add('duck has bill')
kmap.add('duck isa bird')
kmap.add('duck can swim')
kmap.add('platapus has bill')
kmap.add('platapus can swim')
kmap.add('platapus lays eggs')
kmap.add('snake lays eggs')
kmap.add('human can talk')
kmap.add('parrot has feathers')
kmap.add('parrot isa bird')
kmap.add('parrot can talk')
kmap.build_classifier('bird')

kmap = parse_file('data/cup.txt')
print(kmap)
print(kmap.patternLibrary)
kmap.infer()
kmap.infer()
kmap.build_classifier('drinking', query='* enables {}')

kmap.shared_relations('

    """
    info = '''
    poles on-end-of magnet.
    terminals on-end-of battery.
    '''
    kmap = parse_text(info)
    kmap.shared('poles', 'terminals')
    info = '''
    a is-a cup.
    a is small.
    b is-a cup.
    b is large.
    c is-a bowl.
    c is small.
    d is-a bowl.
    d is large.
    '''
    kmap = parse_text(info)
    kmap.shared('a', 'c')
    """
    info = '''
    tuna is-a fish.
    fish is-a animal.
    labrador is-a dog.
    dog is-a animal.
    sparrow is-a bird.
    bird is-a animal.
    '''
    kmap = parse_text(info)
    '''
    kmap.shared('tuna', 'labrador', depth=0)
    kmap.shared('tuna', 'labrador', depth=1)
    '''
    kmap.compare('tuna', 'sparrow', 'labrador')

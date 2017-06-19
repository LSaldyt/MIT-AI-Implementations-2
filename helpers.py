def get(self, t, key='name', eKey=None):
    matches = self.relations.get(t)
    retrieve = lambda t : t if key is None else getattr(t, key)
    if eKey is None:
        return [retrieve(m) for m, _ in matches]
    elif eKey == '*':
        return [(retrive(m), extra) for m, extra in matches]
    else:
        return [(retrieve(m), extra[eKey]) for m, extra in matches]

def get_extra(self, t, eKey):
    return set.union(*[elem[1] for elem in self.get(t, eKey=eKey)])

def abstract(self, clause):
    return to_clause('* {} {}'.format(clause.relation, clause.node))

def get_aspects(self, name):
    return self.get('{} * *'.format(name), key=None)

def get_abstract_aspects(self, name):
    return {self.abstract(a) for a in self.get_aspects(name)}

def similar_to(self, name):
    aspects = self.get_abstract_aspects(name)
    similar = set()
    for aspect in aspects:
        for match in self.get(aspect):
            if match != name:
                similar.add(match)
    return similar

def contrast(self, namea, nameb):
    aAspects = self.get_abstract_aspects(namea)
    bAspects = self.get_abstract_aspects(nameb)
    similarities = set.intersection(aAspects, bAspects)
    return similarities, set.union(aAspects, bAspects) - similarities 

def similarities(self, a, b):
    return self.contrast(a, b)[0]

def differences(self, a, b):
    return self.contrast(a, b)[1]

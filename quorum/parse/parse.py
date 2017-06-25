from collections import defaultdict

from ..clauses.clause        import Clause
from ..clauses.chainedclause import ChainClause

from ..drivers import KnowledgeMap

def parse_clause(words):
    assert len(words) == 3
    name, relation, node = words
    return Clause((name, relation, node))


def parse_chained(words):
    chainDict = defaultdict(set)
    if len(words) >= 4:
        key, *chained = words
        clausewords   = chained[:3]
        chained       = chained[3:]
        chainDict[key].add(parse_clause(clausewords))
        recurse = parse_chained(chained)
        for k, v in recurse.items():
            if k == 'and':
                k = key
            for item in v:
                chainDict[k].add(item)
    elif len(words) > 0 and len(words) < 4:
        raise SyntaxError('Clause file not correctly formatted: {}'.format(str(words)))
    return chainDict


def parse_chained_clause(words):
    assert len(words) >= 3
    root      = parse_clause(words[:3])
    chainDict = parse_chained(words[3:])
    return ChainClause(root, chainDict)

def parse_text(text):
    kmap = KnowledgeMap()
    for sentence in text.split('.'):
        sentence = sentence.replace('\n', ' ')
        words    = sentence.split()
        if len(words) >= 3:
            kmap.add(parse_chained_clause(words))
    return kmap

def parse_file(filename):
    with open(filename, 'r') as infile:
        return parse_text(infile.read())

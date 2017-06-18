from collections import namedtuple

Clause = namedtuple('Clause', ['a', 'relation', 'b'])

def to_clause(*args):
    if len(args) == 1:
        item = args[0]
        if isinstance(item, Clause):
            return item
        else:
            return Clause(*item.split())
    else:
        return Clause(*args)

from collections import namedtuple

Clause = namedtuple('Clause', ['a', 'relation', 'b'])
def _show_clause(c):
    return '{:<15}-{:-^15}>{:>15}'.format(*c)
Clause.__str__ = _show_clause
Clause.__repr__ = _show_clause

def to_clause(*args):
    if len(args) == 1:
        item = args[0]
        if isinstance(item, Clause):
            return item
        elif isinstance(item, tuple):
            return Clause(*item)
        else:
            return Clause(*item.split())
    else:
        return Clause(*args)

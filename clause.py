from collections import namedtuple

_Clause = namedtuple('Clause', ['name', 'relation', 'node'])
def _show_clause(c):
    return '{:<15}-{:-^15}>{:>15}'.format(*c)
_Clause.__str__ = _show_clause
_Clause.__repr__ = _show_clause

def Clause(*args):
    if len(args) == 1:
        item = args[0]
        if isinstance(item, _Clause):
            return item
        elif isinstance(item, tuple):
            return _Clause(*item)
        elif isinstance(item, str):
            return _Clause(*item.split(' '))
        else:
            raise ValueError('{} not converitable to clause'.format(item))
    else:
        return _Clause(*args)


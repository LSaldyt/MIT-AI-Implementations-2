from ..symbol import Symbol
class SymbolDict(object):
    def __init__(self):
        self.symbols = dict()

    def __getitem__(self, key):
        return self.symbols[key]

    def add(self, name, clauses=None):
        if clauses is None:
            clauses = []
        if name not in self.symbols:
            self.symbols[name] = Symbol(name)
        symbol = self.symbols[name]
        for clause in clauses:
            symbol.components.add(clause)

    def get(self, name, query):
        if name not in self.symbols:
            return set()
        else:
            return self.symbols[name].components.get(query)

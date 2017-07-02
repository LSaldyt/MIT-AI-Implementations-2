from ..structs.database import DataBase

'''
Symbolic Apple example

name: Apple
external relations:
    origin: tree
    isa: fruit
internal relations:
    components:
        body:
            shape: round
            size: fist
            color: red, green
            taste: tart, sweet, ..
        stem:
            color: brown

KnowledgeMap will have a symbolDict {string : Symbol} which holds extra information about each symbol
'''

class Symbol(object):
    def __init__(self, name):
        self.name       = name
        self.components = DataBase()

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return '{} : {}'.format(self.name, self.components.names)

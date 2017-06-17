from collections import defaultdict, Counter
from pprint      import pprint
from copy        import deepcopy

from node import Node

from database import DataBase

class KnowledgeMap():
    
    def __init__(self):
        self.database = DataBase()

    def add(self, t):
        '''
        Add a piece of knowledge to the network

        Each piece of knowledge might have conditions and causes
        Conditions rely on states of instance objects
        '''
        self.database.add(t)

    def add_str(self, s):
        t = tuple(s.split(' '))
        self.add(t)

    def get(self, t):
        return self.database.get(t)

    def get_str(self, s):
        t = tuple(s.split(' '))
        return self.get(t)




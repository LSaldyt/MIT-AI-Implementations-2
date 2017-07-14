from .clause         import Clause
from .multiclause    import MultiClause, expand_multiclause, create_multiclause, is_var
from .multistatement import expand_multistatement, MultiStatement, expand_from_vars
from .statement      import Statement

from ..tools.common_entries import common_entries
from ..tools.flatten        import flatten

from collections import defaultdict
from pprint      import pprint
from copy        import deepcopy

class Frame(object):
    def __init__(self, slots):
        self.slots = slots
        self.remaining = slots
        self.variables = dict()

        for slot in self.slots:
            for field in slot.fields():
                if is_var(field):
                    self.variables[field] = None

    def __str__(self):
        if len(self.remaining) > 0:
            return '\n'.join(map(str, self.slots))
        return str(self.variables)
    
    def __repr__(self):
        return str(self)

    def process_field(self, string):
        if is_var(string):
            assert string in self.variables
            value = self.variables[string]
            if value is None:
                return '*'
            else:
                return value
        else:
            return string

    def process_field_list(self, fieldList):
        return ' '.join(self.process_field(field) for field in fieldList)

    def process_statement(self, statement):
        statementDict = defaultdict(set)
        clause = self.process_field_list(list(statement))
        for k, fieldList in statement.chained_items():
            statementDict[k].add(self.process_field_list(fieldList))
        return Statement(clause, statementDict)

    def filter_statement(self, statement, match):
        variables = dict()
        for sfield, mfield in zip(statement.fields(), match.fields()):
            if is_var(sfield):
                if sfield in variables and mfield != variables[sfield]:
                    return False
                else:
                    variables[sfield] = mfield
            else:
                if sfield != mfield:
                    return False
        print(variables)
        return True

    def fill_match(self, match, slot):
        frame = deepcopy(self)
        for mfield, sfield in zip(match.fields(), slot.fields()):
            if is_var(sfield):
                assert sfield in self.variables
                frame.variables[sfield] = mfield
        frame.remaining = frame.remaining[1:]
        return frame

    def fill_from(self, database):
        if len(self.remaining) == 0:
            return [self]
        else:
            first   = self.remaining[0]
            query   = self.process_statement(first)
            matches = database.get(query)
            mathces = {match for match in matches if self.filter_statement(first, match)}
            print(query)
            pprint(matches)
            frames  = [self.fill_match(m, first)   for m in matches]
            frames  = [list(f.fill_from(database)) for f in frames]
        return flatten(frames)

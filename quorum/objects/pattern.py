from .multiclause        import MultiClause, expand_multiclause, create_multiclause, is_var
from .multistatement import expand_multistatement, MultiStatement, expand_from_vars
from .statement      import Statement

from ..tools.common_entries import common_entries

from collections import defaultdict

from .frame import Frame

class Pattern(object):
    def __init__(self, predicates, inferred):
        self.frame    = Frame(predicates)
        self.inferred = inferred

    def __str__(self):
        return 'if\n    {}\nthen\n    {}\n'.format(
                str(self.frame),
                '\n    '.join(map(str, self.inferred)))

    def get_inferences(self, database):
        self.frame.fill_from(database)
        for statement in self.inferred:
            print(statement)
            for statement in expand_from_vars(statement, self.frame.variables):
                yield statement

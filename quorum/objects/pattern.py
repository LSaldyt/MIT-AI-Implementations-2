from ..clauses.multiclause        import MultiClause, expand_multiclause, create_multiclause, is_var
from ..clauses.multichainedclause import expand_multichainedclause, MultiChainClause
from ..clauses.chainedclause      import ChainClause

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
        frame.fill_variables(database)
        variables = frame.variables
        for eclause in self.inferred:
            try:
                mc  = create_multiclause(eclause.clause, variables)
                chainDict = {k : create_multiclause(c, variables) for k, vs in eclause.chained.items() for c in vs}
                mec = MultiChainClause(mc, chainDict)
                for clause in expand_multichainedclause(mec):
                    yield clause
            except KeyError:
                pass

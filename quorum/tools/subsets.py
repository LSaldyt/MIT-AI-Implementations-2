from itertools import chain, combinations

def subsets(ss):
      return chain(*map(lambda x: combinations(ss, x), range(0, len(ss)+1)))

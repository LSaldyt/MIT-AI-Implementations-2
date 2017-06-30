class PatternLibrary(object):
    def __init__(self):
        self.learned = []

    def teach(self, pattern):
        self.learned.append(pattern)

    def get_inferences(self, database):
        for pattern in self.learned:
            pattern.fill_variables(database)
            return pattern.get_inferred()

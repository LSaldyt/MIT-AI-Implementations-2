class PatternLibrary(object):
    def __init__(self):
        self.learned = dict()
        self.serialID = 0

    def teach(self, pattern, name=None):
        if name is None:
            name = 'Pattern{}'.format(self.serialID)
            self.serialID += 1
        assert name not in self.learned, 'Pattern name must be unique'
        self.learned[name] = pattern

    def get_inferences(self, database):
        for pattern in self.learned.values():
            return pattern.get_inferences(database)

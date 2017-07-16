class PatternLibrary(object):
    def __init__(self):
        self.learned = []

    def __str__(self):
        return '\n'.join(map(str, self.learned))

    def teach(self, pattern):
        self.learned.append(pattern)

    def get_inferences(self, database):
        for pattern in self.learned:
            for inference in pattern.get_inferences(database):
                yield inference

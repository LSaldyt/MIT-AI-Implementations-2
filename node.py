class Node(object):
    def __init__(self, item):
        self.item = item

    def __str__(self):
        return str(self.item)

    def __repr__(self):
        return str(self)

    def __getattr__(self, attr):
        return getattr(self.item, attr)

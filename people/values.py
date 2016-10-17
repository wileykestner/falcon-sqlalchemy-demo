class Person(object):
    def __init__(self, identifier, name: str):
        super().__init__()
        self.identifier = identifier
        self.name = name
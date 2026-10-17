

class WitWorld():
    class Blob():
        def __init__(self, contents: list[int]):
            self.contents = contents

        def append(self, value: int):
            self.contents.append(value)
            return self.contents
    pass

Blob = WitWorld.Blob

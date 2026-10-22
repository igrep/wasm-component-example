from wit_world.exports import blobs

escape = None

class Blob(blobs.Blob):
    def __init__(self, contents: bytes):
        self.contents = bytearray(contents)

    def append(self, value: int):
        global escape
        escape = self
        self.contents.append(value)

    def append_global(self, value: int):
        global escape
        escape.contents.append(value)

    def get_contents(self) -> bytes:
        return bytes(self.contents)

    @staticmethod
    def get_global_contents() -> bytes:
        global escape
        print("From staticmethod:")
        print(escape)
        print(escape.contents)
        return bytes(escape.contents)

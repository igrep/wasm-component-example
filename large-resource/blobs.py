from wit_world.exports import blobs


class Blob(blobs.Blob):
    def __init__(self, contents: bytes):
        self.contents = bytearray(contents)

    def append(self, value: int):
        self.contents.append(value)

    def get_contents(self) -> bytes:
        return bytes(self.contents)

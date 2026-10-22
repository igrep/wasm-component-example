import gc
import blobs

class WitWorld:
    def call_gc(self):
        gc.collect()

    def get_global_contents(self):
        print("Imported global:")
        print(blobs.escape)
        print(blobs.escape.contents)
        return blobs.escape.contents

import sys

class WitWorld():
    def greet(self, caller: str) -> str:
        version = sys.version_info
        major = version.major
        minor = version.minor
        micro = version.micro
        return f"Hello, {caller}! I'm Python {major}.{minor}.{micro}!"

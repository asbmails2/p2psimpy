from enum import Enum
from typing import List


class BundleType(Enum):
    DEFINITION = 0
    IMPLEMENTATION = 1


class Bundle:
    def __init__(self, name: str,
                 defines: List[str] = [],
                 provides: List[str] = []):
        self.name = name
        self.defines = defines
        self.provides = provides

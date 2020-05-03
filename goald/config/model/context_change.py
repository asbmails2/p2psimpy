# from typing import Any, Dict
from enum import Enum


class OP(Enum):
    ADDED = 1
    REMOVED = 2


class ContextChange:
    def __init__(self, op, label, time):
        self.op = op
        self.label = label
        self.time = time

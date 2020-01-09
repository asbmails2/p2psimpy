
from enum import Enum


class TypeMulti(Enum):
    UNARY = 1
    BINARY = 2


class Type(Enum):
    ONE = TypeMulti.UNARY
    ANY = TypeMulti.UNARY
    COND = TypeMulti.BINARY


class DependencyModifier:

    def __init__(self, type, groupId):
        self.type = type
        self.groupId = groupId

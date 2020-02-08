
from enum import Enum


class TypeMulti(Enum):
    UNARY = 1
    BINARY = 2


class DependencyType(Enum):
    ONE = TypeMulti.UNARY
    ANY = TypeMulti.UNARY
    COND = TypeMulti.BINARY


class DependencyModifier:

    def __init__(self, type: DependencyType, groupId: str):
        self.type = type
        self.groupId = groupId


class Dependency:
    def __init__(self,
                 identification: str,
                 modifierGroupId: str = None,
                 modifierType: DependencyType = DependencyType.ONE):
        self.identification = identification
        self.modifier = DependencyModifier(
            type=modifierType,
            groupId=modifierGroupId)

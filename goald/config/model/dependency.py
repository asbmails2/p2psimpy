
from goald.config.model.dependency_modifier import DependencyModifier, Type


class Dependency:
    def __init__(self,
                 identification,
                 modifierType:  Type,
                 modifierGroupId: str):
        self.identification = identification
        self.modifier = DependencyModifier(
            type=modifierType,
            groupId=modifierGroupId)


from goald.config.model.dependency_modifier import DependencyModifier


class Dependency:
    def __init__(self,
                 identification,
                 modifierType,
                 modifierGroupId):
        self.identification = identification
        self.modifier = DependencyModifier(
            type=modifierType,
            groupId=modifierGroupId)

from .component import Component
from .alternative import Alternative
from .dependency import Dependency

class VE:
    def __init__(self, definition: Component,
                 parentAlt: Alternative,
                 alternatives,
                 chosenAlternative: Alternative,
                 isAchievable: bool,
                 satisfy: Dependency):

        self.definition = definition
        self.parentAlt = parentAlt
        self.alternatives = alternatives
        self.chosenAlternative = chosenAlternative
        self.isAchievable = isAchievable
        self.satisfy = satisfy

from typing import List
from goald.config.model.alternative import Alternative
from goald.config.model.bundle import Bundle
from goald.config.model.dependency import Dependency


class VE:
    def __init__(self, parentAlt: Alternative,
                 definition: Bundle,
                 alternatives: List[Alternative],
                 satisfy: Dependency):
        # attrs that do not change
        self.definition = definition
        self.parentAlt = parentAlt
        self.alternatives = alternatives
        self.satisfy = satisfy
        # attrs to be resolved
        self.chosenAlternative: Alternative = None
        self.isAchievable = False
        self.restrictions = []

from typing import List
from goald.config.model.dependency import Dependency


class Alternative:
    def __init__(self, implementaion=None,
                 parentVE=None,
                 dependencies=[],
                 contextConditions=None,
                 quality=None,
                 resolved=False):
        self.parentVE = parentVE
        self.dependencies: List[Dependency] = dependencies
        self.contextConditions = contextConditions
        self.implementaion = implementaion
        self.quality = quality
        self.resolved = resolved

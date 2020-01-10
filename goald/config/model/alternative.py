# from typing import Any, Dict


class Alternative:
    def __init__(self, implementaion=None,
                 parentVE=None,
                 dependencies=[],
                 contextConditions=None,
                 quality=None,
                 resolved=False):
        self.parentVE = parentVE
        self.dependencies = dependencies
        self.contextConditions = contextConditions
        self.implementaion = implementaion
        self.quality = quality
        self.resolved = resolved


from typing import List, Type, TypeVar, Generic

from goald.config.model.dependency import Dependency

T = TypeVar('T')


class Alternative:
    def __init__(self, implementaion=None,
                 parentVE=None,
                 dependencies=[],
                 contextConditions=None,
                 quality=None,
                 resolved=False):
        self.parentVE = parentVE
        self.dependencies: List[Dependency] = dependencies
        self.implementaion = implementaion
        self.propertiesMap = {}

    def setProperty(self, propId: str, prop: Type[T]):
        self.propertiesMap[propId] = prop

    def getProperty(self, propId: str, propType: Type[T] = None) -> T:
        prop = self.propertiesMap[propId]
        if propType is None or isinstance(prop, propType):
            return prop
        else:
            raise TypeError(f'{propId} -> value, not instance of {propType}')

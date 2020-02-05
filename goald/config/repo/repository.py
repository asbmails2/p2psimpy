from abc import ABC, abstractmethod
from enum import Enum

from goald.config.model.bundle import Bundle


class BundleType(Enum):
    DEFINITION = 0
    IMPLEMENTATION = 1


class Repository(ABC):

    @abstractmethod
    def add(bundle: Bundle):
        pass

    @abstractmethod
    def getSize() -> int:
        pass

    @abstractmethod
    def queryForDefinition(identification):
        pass

    @abstractmethod
    def queryForImplementations(identification):
        pass

    @abstractmethod
    def queryForDefinitions(identification):
        pass

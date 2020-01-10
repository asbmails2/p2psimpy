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
    def queryForDefinition(String identification):
        pass

    @abstractmethod
    def queryForImplementations(String identification):
        pass

    @abstractmethod
    def queryForDefinitions(String identification):
        pass

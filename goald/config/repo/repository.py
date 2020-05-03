from abc import ABC, abstractmethod
from goald.config.model.bundle import Bundle


class Repository(ABC):
    @abstractmethod
    def createIndex(attribute: str, isMany: bool):
        pass

    @abstractmethod
    def add(bundle: Bundle):
        pass

    @abstractmethod
    def getSize() -> int:
        pass

    @abstractmethod
    def queryForDefinition(self, identification: str):
        pass

    @abstractmethod
    def queryForImplementations(self, identification: str):
        pass

    @abstractmethod
    def query(self, attr: any, value: str):
        pass

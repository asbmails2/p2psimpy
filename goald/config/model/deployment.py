from enum import Enum
from .component import Component


class Deployment:

    def __init__(self):
        self.componentStatus = []

    def add(self, status, component):
        self.componentStatus.append(ComponentStatus(status, component))

    def remove(self, component):
        return None

    def queryAll(self, status):
        return None


class Status(Enum):
    INSTALLED = 1
    RESOLVED = 2
    UNINSTALLED = 3
    STOPED = 4
    ACTIVE = 5


class ComponentStatus:
    def __init__(self, status: Status, component: Component):
        self.status = status
        self.component = component

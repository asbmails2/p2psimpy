from enum import Enum
from .bundle import Bundle


class Deployment:

    def __init__(self):
        self.bundleStatus = []

    def add(self, status, bundle):
        self.bundleStatus.append(BundleStatus(status, bundle))

    def remove(self, bundle):
        return None

    def queryAll(self, status):
        return None


class Status(Enum):
    INSTALLED = 1
    RESOLVED = 2
    UNINSTALLED = 3
    STOPED = 4
    ACTIVE = 5


class BundleStatus:
    def __init__(self, status: Status, bundle: Bundle):
        self.status = status
        self.bundle = bundle

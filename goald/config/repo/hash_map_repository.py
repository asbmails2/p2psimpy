
from goald.config.repo.repository import Repository
from goald.config.model.bundle import Bundle, BundleType


class HashMapRepository(Repository):
    def __init__(self):
        self.repoSize = 0
        self._indexedAttrs = {}
        self._bundlesMap = {}
        # default indexes
        self.createIndex(BundleType.DEFINITION, False)
        self.createIndex(BundleType.IMPLEMENTATION, True)

    def createIndex(self, attribute: any, isMany: bool):
        self._indexedAttrs[attribute] = {'isMany': isMany}
        self._bundlesMap[attribute] = {}

    def add(self, bundle: Bundle):
        self.repoSize += 1
        for definition in bundle.defines:
            self._put(BundleType.DEFINITION, definition, bundle)
        for provide in bundle.provides:
            self._put(BundleType.IMPLEMENTATION, provide, bundle)

    def getSize(self):
        return self.repoSize

    def query(self, attr: any, value: str):
        return self._get(attr, value)

    def queryForDefinition(self, identification: str):
        return self._get(BundleType.DEFINITION, identification)

    def queryForImplementations(self, identification: str):
        return self._get(BundleType.IMPLEMENTATION, identification)

    def _get(self, bundleType: BundleType, identification: str):
        try:
            return self._bundlesMap[bundleType][identification]
        except KeyError:
            return None

    def _put(self, attr: any, value: str, bundle: Bundle):
        if self._indexedAttrs[attr]['isMany']:
            if value not in self._bundlesMap[attr]:
                self._bundlesMap[attr][value] = []
            self._bundlesMap[attr][value].append(bundle)
        else:
            self._bundlesMap[attr][value] = bundle


from goald.config.repo.repository import BundleType, Repository
from goald.config.model.bundle import Bundle

class HashMapRepository(Repository):
    def __init__(self):
        self.repoSize = 0
        self.index = {}
        self.index[BundleType.DEFINITION] = {}
        self.index[BundleType.IMPLEMENTATION] = {}

    def add(self, bundle: Bundle):
        self.repoSize += 1

    def put(self, goal, bundle):
        bundleType = bundle.type

        if(not self.index[bundleType][goal]):
            self.index[bundleType][goal] = []
        
        ref = self.index[bundleType][goal]
        ref.append()

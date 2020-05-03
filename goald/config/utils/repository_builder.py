from goald.config.model.bundle import Bundle
from goald.config.repo.hash_map_repository import HashMapRepository


class RepositoryBuilder:
    def __init__(self):
        self._repo = HashMapRepository()
        self._goals = {}
        self._metadataAttrs = []

    def withMetadata(self, *attrs):
        self._metadataAttrs.extend(attrs)
        return self

    def withBundle(self, uuid, **metadata):
        bundle = Bundle(uuid)
        for key, value in metadata.items():
            if key not in self._metadataAttrs:
                raise KeyError(key)
            setattr(bundle, key, value)

        self._repo.add(bundle)
        return self

    def done(self):
        return self._repo

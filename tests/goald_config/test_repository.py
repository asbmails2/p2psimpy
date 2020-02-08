from goald.config.utils.repository_builder import RepositoryBuilder
from goald.config.repo.hash_map_repository import HashMapRepository
from goald.config.model.bundle import BundleType

import pytest


@pytest.fixture()
def repository() -> HashMapRepository:
    return RepositoryBuilder() \
        .withMetadata('defines', 'provides', 'conditions') \
        .withBundle('greater.def',
                    defines=['greet']) \
        .withBundle('greater.impl',
                    provides=['greet'],
                    conditions=['display_capability']) \
        .done()


def test_repository_size(repository):
    assert repository.repoSize == 2

    newRepo = RepositoryBuilder().done()
    assert newRepo.repoSize == 0


def test_query_definition(repository: HashMapRepository):

    bundle = repository.query(BundleType.DEFINITION, 'greet')
    assert bundle.name == 'greater.def'


def test_query_implementation(repository: HashMapRepository):

    bundles = repository.query(BundleType.IMPLEMENTATION, 'greet')
    assert bundles[0].name == 'greater.impl'


def test_invalid_attr():
    try:
        RepositoryBuilder() \
            .withMetadata('defines', 'provides', 'conditions') \
            .withBundle('greater.def',
                        definesX=['greet']) \
            .done()
        assert False
    except KeyError:
        assert True



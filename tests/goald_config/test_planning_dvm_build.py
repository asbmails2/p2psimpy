

from goald.config.utils.repository_builder import RepositoryBuilder
from goald.config.planning.dvm_builder import DVMBuilder

import pytest


@pytest.fixture()
def dvmBuilder() -> DVMBuilder:
    repo = RepositoryBuilder() \
        .withMetadata('defines', 'provides', 'conditions') \
        .withBundle('greater.def',
                    defines=['greet']) \
        .withBundle('greater.impl',
                    provides=['greet'],
                    conditions=['display_capability']) \
        .done()

    return DVMBuilder(repo)


def test_repository_size(dvmBuilder: DVMBuilder):
    dvm = dvmBuilder.resolveRootGoal("greet")
    assert len(dvm.alternatives) == 1

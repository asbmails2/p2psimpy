

from goald.config.utils.repository_builder import RepositoryBuilder
from goald.config.planning.gcvm_builder import GCVMBuilder

import pytest


@pytest.fixture()
def gcvmBuilder() -> GCVMBuilder:
    repo = RepositoryBuilder() \
        .withMetadata('defines', 'provides', 'conditions') \
        .withBundle('greater.def',
                    defines=['greet']) \
        .withBundle('greater.impl',
                    provides=['greet'],
                    conditions=['display_capability']) \
        .done()

    return GCVMBuilder(repo)


def test_repository_size(gcvmBuilder: GCVMBuilder):
    gcvm = gcvmBuilder.resolveRootGoal("greet")
    assert len(gcvm.alternatives) == 1

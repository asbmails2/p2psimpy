from goald.config.repo.repository import Repository
from typing import List
from goald.config.model.ve import VE
from goald.config.model.alternative import Alternative
from goald.config.model.dependency import Dependency, DependencyType
from goald.config.model.bundle import Bundle, BundleType


class GCVMBuilder:
    def __init__(self, repo: Repository):
        self._repo = repo

    def resolveRootGoal(self, identification: str) -> VE:
        rootDependency = Dependency(identification, DependencyType.ONE)
        rootVe = self.resolveVEforDependency(rootDependency)
        return rootVe

    def resolveVEforDependency(self, dependency: Dependency, parentAlt=None):
        identification = dependency.identification

        impls: List[Bundle] = None
        definition = self._repo.query(BundleType.DEFINITION, identification)
        impls = self._repo.query(BundleType.IMPLEMENTATION, identification)

        if definition is None:
            print("no def found for dep " + dependency)
            return None

        if impls is None:
            print("no impl found for dep " + dependency)
            return None

        alternatives = []

        ve = VE(parentAlt,
                definition,
                alternatives,
                satisfy=dependency)

        for impl in impls:
            alt = Alternative()
            alt.parentVE = ve
            alternatives.append(alt)

            alt.implementaion = impl
            alt.dependencies = impl  # todo
            alt.contextConditions = impl  # todo

        return ve

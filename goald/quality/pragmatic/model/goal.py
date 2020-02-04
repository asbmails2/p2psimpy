from goald.quality.pragmatic.model.refinement import Refinement
from goald.quality.pragmatic.model.plan import Plan
from goald.quality.pragmatic.model.decomposition import Decomposition


class Goal(Refinement):
    def __init__(self, decomposition, identifier=""):
        Refinement.__init__(self, identifier)
        self.decomposition = decomposition

    def myType(self):
        return Refinement().GOAL

    def isAchievable(self, current, interp):
        if not self.isApplicable(current):
            return None

        dependencies = self.getApplicableDependencies(current)

        if self.decomposition == Decomposition.OR:
            for dep in dependencies:
                plan = dep.isAchievable(current, interp)
                if plan:
                    return plan
            return None
        else:
            complete = Plan()
            for dep in dependencies:
                plan = dep.isAchievable(current, interp)
                if plan:
                    complete.add(plan)
                else:
                    return None
            if len(complete.getTasks()) > 0:
                return complete
            else:
                return None

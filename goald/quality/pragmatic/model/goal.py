from goald.quality.pragmatic.model.refinement import Refinement
from goald.quality.pragmatic.model.plan import Plan


class Goal(Refinement):
    def __init__(self, decomposition=False):
        Refinement.__init__(self)
        self.decomposition = decomposition

    def myType(self):
        return Refinement().GOAL

    def isAchievable(self, current, interp):
        if not self.isApplicable(current):
            return None

        if self.decomposition:
            for dep in self.getApplicableDependencies(current):
                plan = dep.isAchievable(current, interp)
                if plan is not None:
                    return plan
            return None
        else:
            complete = Plan()
            for dep in self.getApplicableDependencies(current):
                plan = dep.isAchievable(current, interp)
                if plan is not None:
                    complete.add(plan)
                else:
                    return None
            if len(complete.getTasks()) > 0:
                return complete
            else:
                return None

from goald.quality.pragmatic.model.refinement import Refinement
from goald.quality.pragmatic.model.plan import Plan

class Goal(Refinement):
    def __init__(self, *isDecompostion):
        Refinement.__init__(self)
        self.AND = False
        self.OR = True
        if isDecompostion:
            self.isOrDecomposition = isDecompostion

    def myType(self):
        return self.identification

    def isOrDecomposition(self):
        return self.isOrDecomposition

    def isAndDecomposition(self):
        return not self.isOrDecomposition

    def isAndDecomposition(self):
        return not self.isOrDecomposition

    def isAchievable(self, current, interp):
        if not self.isApplicable(current):
            return None
        if self.isOrDecomposition:
            plan = Plan()
            for dep in self.getApplicableDependencies(current):
                plan = dep.isAchievable(current, interp)
                if plan != None:
                    return plan
            return None
        else:
            complete = Plan()
            for dep in self.getApplicableDependencies(current):
                plan = dep.isAchievable(current, interp)
                if plan != None:
                     complete.add(plan)
                else:
                    return None
            if complete.getTasks().len() > 0:
                return complete
            else:
                return None
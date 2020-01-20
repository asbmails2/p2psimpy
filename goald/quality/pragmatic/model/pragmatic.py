from goald.quality.pragmatic.model.goal import Goal
from goald.quality.pragmatic.model.interpretation import Interpretation

class Pragmatic(Goal):

    def __init__(self, isOrDecomposition=None):
        Goal.__init__(self, isOrDecomposition)

        self.isOrDecomposition = isOrDecomposition
        self.interp = Interpretation()
    
    def getInterpretation(self):
        return self.interp

    def isAchievable(current, interp):
        newInterp = Interpretation()
        newInterp.merge(self.interp)
        newInterp.merge(interp)

        return Goal.isAchievable(current, newInterp)
from goald.quality.pragmatic.model.goal import Goal
from goald.quality.pragmatic.model.interpretation import Interpretation


class Pragmatic(Goal):

    def __init__(self, decomposition, identifier=""):
        Goal.__init__(self, decomposition, identifier)

        self.interp = Interpretation()

    def getInterpretation(self):
        return self.interp

    def isAchievable(self, current, interp):
        newInterp = Interpretation()
        newInterp.merge(self.interp)
        newInterp.merge(interp)

        return super().isAchievable(current, newInterp)

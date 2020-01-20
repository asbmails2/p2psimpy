from goald.quality.pragmatic.model.refinement import Refinement

class Delegation(Refinement):

    def __init__(self):
        Refinement.__init__(self)

    def myType(self):
        refinement = Refinement()
        return refinement.DELEGATION

    def isAchivable(currentContext, interpretation):
        return null
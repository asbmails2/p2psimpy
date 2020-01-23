from goald.quality.pragmatic.model.refinement import Refinement


class Delegation(Refinement):

    def __init__(self):
        Refinement.__init__(self)

    def myType(self):
        return Refinement().DELEGATION

    def isAchivable(self, currentContext, interpretation):
        return None

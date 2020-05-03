from goald.quality.pragmatic.model.refinement import Refinement


class Delegation(Refinement):

    def __init__(self, identifier=""):
        Refinement.__init__(self, identifier)

    def myType(self):
        return Refinement().DELEGATION

    def isAchivable(self, currentContext, interpretation):
        return None

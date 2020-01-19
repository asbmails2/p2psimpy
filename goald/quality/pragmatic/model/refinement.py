class Refinement():

    def __init__(self):
        self.GOAL = 1
        self.TASK = 2
        self.DELEGATION = 3

        self.aplicableContext = {}
        self.nonAplicableContexts = {}

        self.isOrDecomposition = False

        self.dependencies = {}

        self.identifier = ""

        self.aplicableContext.add(self.aplicableContext,None)

    def addApplicableContext(self,context):
        if self.aplicableContext:
            self.aplicableContext.popitem(None)
        else:
            self.aplicableContext[context] += context

    def addNonAplicableContext(context):
        self.nonAplicableContexts.add(context)



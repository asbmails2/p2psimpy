class Refinement():

    def __init__(self):
        self.GOAL = 1
        self.TASK = 2
        self.DELEGATION = 3

        self.aplicableContext = []
        self.nonAplicableContexts = []

        self.isOrDecomposition = False

        self.dependencies = []

        self.identifier = ""

        self.aplicableContext.append(None)

    def addApplicableContext(self,context):
        if None in self.aplicableContext:
            self.aplicableContext.remove(None)
        else:
            self.aplicableContext.append(context)

    def addNonAplicableContext(self,context):
        self.nonAplicableContexts.append(context)

    def addApplicableContext(self,context):
        self.aplicableContext.append(context)

    def getApplicableContext(self,context):
        return self.applicableContext

    def isApplicable(self,current):
        returnValue = False
        unapplicableContextsFound = 0
        if None in self.applicableContext:
            returnValue = True

        if self.nonAplicableContexts is None:
             returnValue = True

        for context in self.nonAplicableContexts:
            if context in self.nonAplicableContexts:
                return False
            if context in self.aplicableContext:
                returnValue = True

        return returnValue

    def getDependencies(self):
        return self.dependencies

    def getApplicableDependencies(self, context):
        applicableDeps = Refinement()
        for dep in self.dependencies:
            for cont in context:
                if context in dep.getApplicableContext() or None in dep.getApplicableContext():
                    applicableDeps.add(dep)
        return applicableDeps

    def  getIdentifier(self):
        return self.identifier

    def setIdentifier(self, identifier):
        self.identifier = identifier
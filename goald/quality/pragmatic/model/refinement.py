class Refinement():

    def __init__(self):
        self.GOAL = 1
        self.TASK = 2
        self.DELEGATION = 3

        self.applicableContext = []
        self.nonAplicableContexts = []

        self.isOrDecomposition = False

        self.dependencies = []

        self.identifier = ""

        self.applicableContext.append(None)

    def addApplicableContext(self,context):
        if None in self.applicableContext:
            self.applicableContext.remove(None)
        else:
            self.applicableContext.append(context)

    def addNonAplicableContext(self,context):
        self.nonAplicableContexts.append(context)

    def addDependency(self, goal):
        self.dependencies.append(goal)

    def addApplicableContext(self,context):
        self.applicableContext.append(context)

    def getApplicableContext(self):
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
            if context in self.applicableContext:
                returnValue = True

        return returnValue

    def getDependencies(self):
        return self.dependencies

    def getApplicableDependencies(self, context):
        applicableDeps = []
        for dep in self.dependencies:
            for cont in context:
                if context in dep.getApplicableContext() or None in dep.getApplicableContext():
                    applicableDeps.append(dep)
        return applicableDeps

    def  getIdentifier(self):
        return self.identifier

    def setIdentifier(self, identifier):
        self.identifier = identifier
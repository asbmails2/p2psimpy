class Refinement():

    def __init__(self):
        self.GOAL = 1
        self.TASK = 2
        self.DELEGATION = 3

        self.applicableContext = []
        self.nonapplicableContexts = []

        self.isOrDecomposition = False

        self.dependencies = []

        self.identifier = ""

        self.applicableContext.append(None)

    def addApplicableContext(self,context):
        if None in self.applicableContext:
            self.applicableContext.remove(None)
        else:
            self.applicableContext.append(context)

    def addNonapplicableContext(self,context):
        self.nonapplicableContexts.append(context)

    def addApplicableContext(self,context):
        self.applicableContext.append(context)

    def getApplicableContext(self,context):
        return self.applicableContext

    def isApplicable(self,current):
        returnValue = False
        unapplicableContextsFound = 0
        if None in self.applicableContext:
            returnValue = True

        if self.nonapplicableContexts is None:
             returnValue = True

        for context in self.nonapplicableContexts:
            if context in self.nonapplicableContexts:
                return False
            if context in self.applicableContext:
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
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

    def addNonapplicableContext(self, context):
        self.nonapplicableContexts.append(context)

    def addDependency(self, goal):
        self.dependencies.append(goal)

    def addApplicableContext(self, context):
        if None in self.applicableContext:
            self.applicableContext.remove(None)
        if isinstance(context, list):
            self.applicableContext.extend(context)
        else:
            self.applicableContext.append(context)

    def getApplicableContext(self):
        return self.applicableContext

    def isApplicable(self, current):
        returnValue = False

        if None in self.applicableContext:
            returnValue = True

        if len(self.nonapplicableContexts) > 0:
            returnValue = True

        for context in current:
            if context in self.nonapplicableContexts:
                return False
            if context in self.applicableContext:
                returnValue = True

        return returnValue

    def getDependencies(self):
        return self.dependencies

    def getApplicableDependencies(self, current):
        applicableDeps = []
        for dep in self.dependencies:
            for context in current:
                if context in dep.getApplicableContext() or \
                        None in dep.getApplicableContext():
                    applicableDeps.append(dep)
        return applicableDeps

    def getIdentifier(self):
        return self.identifier

    def setIdentifier(self, identifier):
        self.identifier = identifier

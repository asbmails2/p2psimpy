class Refinement():

    def __init__(self, identifier=""):
        self.GOAL = 1
        self.TASK = 2
        self.DELEGATION = 3

        self.applicableContext = None

        self.nonapplicableContexts = []

        self.dependencies = []

        self.identifier = identifier

    def addNonapplicableContext(self, context):
        self.nonapplicableContexts.append(context)

    def addDependency(self, goal):
        self.dependencies.append(goal)

    def addApplicableContext(self, context):
        if self.applicableContext is None:
            self.applicableContext = []
        if isinstance(context, list):
            self.applicableContext.extend(context)
        else:
            self.applicableContext.append(context)

    def getApplicableContext(self):
        return self.applicableContext

    def isApplicable(self, current):
        returnValue = False

        if self.applicableContext is None:
            returnValue = True

        if len(self.nonapplicableContexts) > 0:
            returnValue = True

        for context in current:
            if context in self.nonapplicableContexts:
                return False
            if self.applicableContext:
                if context in self.applicableContext:
                    returnValue = True

        return returnValue

    def getDependencies(self):
        return self.dependencies

    def getApplicableDependencies(self, current):
        applicableDeps = []

        for dep in self.dependencies:
            if dep.applicableContext is None:
                applicableDeps.append(dep)
                continue
            for context in current:
                if context in dep.applicableContext:
                    if(dep not in applicableDeps):
                        applicableDeps.append(dep)

        print("====== Applicable Dependencies ======")
        for d in applicableDeps:
            print(d.identifier)

        return applicableDeps

    def getIdentifier(self):
        return self.identifier

    def setIdentifier(self, identifier):
        self.identifier = identifier

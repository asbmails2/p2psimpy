class Interpretation():

    def __init__(self):
        self.qualityConstraints = []
        self.contextDependentInterpretation = {}

    def getContextDependentInterpretation(self):
        return self.contextDependentInterpretation

    def addQualityConstraint(self, constraint):
        self.qualityConstraints.append(constraint)
        context = constraint.getApplicableContext()

        if context in self.contextDependentInterpretation:
            self.contextDependentInterpretation[context].update(constraint)
        else:
            constraintSet = []
            constraintSet.append(constraint)
            self.contextDependentInterpretation[context] = constraintSet
        
    def getQualityConstraints(self, current):
        allQCs = {}

        if current:
            for context in current:
                if self.contextDependentInterpretation.containsKey(context):
                    allQCs.addAll(self.contextDependentInterpretation.get(context))
        elif self.contextDependentInterpretation.containsKey(None):
            allQCs.addAll(self.contextDependentInterpretation.get(None))
        
        return allQCs

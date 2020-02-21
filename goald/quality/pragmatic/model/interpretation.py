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
            self.contextDependentInterpretation[context].append(constraint)
        else:
            constraintSet = []
            constraintSet.append(constraint)
            self.contextDependentInterpretation[context] = constraintSet

    def getQualityConstraints(self, current):
        allQCs = []
        
        if None not in current:
            for context in current:
                if context in self.contextDependentInterpretation:
                    constrains = self.contextDependentInterpretation[context]
                    allQCs.extend(constrains)

        elif None in self.contextDependentInterpretation:
            baselineConstrains = self.contextDependentInterpretation.get(None)
            allQCs.extend(baselineConstrains)

        return allQCs

    def merge(self, interp):
        if interp is None:
            return
        for qc in interp.getAllQualityConstraints():
            self.addQualityConstraint(qc)

    def getAllQualityConstraints(self):
        return self.qualityConstraints

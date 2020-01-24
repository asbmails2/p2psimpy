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
        
        if current is not None:
            if(isinstance(current, list)):
                for context in current:
                    if context in self.contextDependentInterpretation:
                        allQCs.extend(
                            self.contextDependentInterpretation[context])
            elif current in self.contextDependentInterpretation:
                allQCs.extend(self.contextDependentInterpretation[current])

        elif None in self.contextDependentInterpretation.keys():
            allQCs.append(self.contextDependentInterpretation.get(None))

        return allQCs

    def merge(self, interp):
        if interp is None:
            return
        for qc in interp.getAllQualityConstraints():
            self.addQualityConstraint(qc)

    def getAllQualityConstraints(self):
        return self.qualityConstraints

from goald.quality.pragmatic.model.refinement import Refinement
from goald.quality.pragmatic.model.plan import Plan
from goald.quality.pragmatic.exceptions.metric_not_found import MetricNotFoundException


class Task(Refinement):
    def __init__(self, identifier=""):
        Refinement.__init__(self, identifier)
        self.providedQualityLevels = {}
        self.identifier = identifier

    def myType(self):
        return Refinement().TASK

    def setProvidedQuality(self, context, metric, value):
        metricMap = {}

        if metric in self.providedQualityLevels:
            metricMap = self.providedQualityLevels[metric]
            metricMap[context] = value
            self.providedQualityLevels[metric] = metricMap
        else:
            metricMap[context] = value
            self.providedQualityLevels[metric] = metricMap

    def myProvidedQuality(self, metric, contextSet):
        myQuality = 0
        baseline = False

        if metric not in self.providedQualityLevels.keys():
            message = "Metric: {0} not found".format(metric.name)
            print(message)
            return None

        metricQL = self.providedQualityLevels[metric]

        # getting baseline
        if None in metricQL:
            myQuality = metricQL[None]
            baseline = True

        for current in contextSet:
            if metricQL.get(current) is None:
                continue
            if not baseline:
                myQuality = metricQL.get(current)
                baseline = True
            else:
                if metric.getLessIsBetter():
                    if(myQuality > metricQL[current]):
                        myQuality = metricQL[current]
                elif(myQuality < metricQL[current]):
                    myQuality = metricQL[current]

        return myQuality

    def abidesByInterpretation(self, interp, current):
        feasible = True
        if interp is None:
            return True

        currentQcs = interp.getQualityConstraints(current)

        if interp.getQualityConstraints([None]):
            for qc in interp.getQualityConstraints([None]):
                feasible = self.checkQualityConstraint(qc, current)
                
        for qc in currentQcs:
            feasible = self.checkQualityConstraint(qc, current)

        return feasible

    def checkQualityConstraint(self, qc, current):
        myQC = self.myProvidedQuality(qc.metric, current)
        if myQC is None:
            return True
        if not qc.abidesByQC(myQC, qc.metric):
            return False
    
        return True


    def isAchievable(self, current, interp):
        if not self.isApplicable(current):
            return None
        if self.abidesByInterpretation(interp, current):
            return Plan(self)
        else:
            return None

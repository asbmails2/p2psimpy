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
        initQuality = False

        if metric not in self.providedQualityLevels.keys():
            message = "Metric: {0} not found".format(metric.name)
            print(message)
            return None

        metricQL = self.providedQualityLevels[metric]

        # getting baseline
        if None in metricQL:
            myQuality = metricQL[None]
            initQuality = True

        for current in contextSet:
            if metricQL.get(current) is None:
                continue
            if not initQuality:
                myQuality = metricQL.get(current)
                initQuality = True
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
                
        for qc in currentQcs:
            try:
                myQC = self.myProvidedQuality(qc.metric, current)
                if not qc.abidesByQC(myQC, qc.metric):
                    feasible = False
            except:
                pass

        if interp.getQualityConstraints([None]):
            for qc in interp.getQualityConstraints([None]):
                try:
                    myQC = self.myProvidedQuality(qc.metric, current)
                    if not qc.abidesByQC(myQC, qc.metric):
                        feasible = False
                except:
                    pass

        return feasible

    def isAchievable(self, current, interp):
        if not self.isApplicable(current):
            return None
        if self.abidesByInterpretation(interp, current):
            return Plan(self)
        else:
            return None

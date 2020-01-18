from goald.quality.pragmatic.model.context import Context

class Task():
    def __init__(self, metric, contextValueMap, lessIsMore):
        self.providedQualityLevels[metric] = contextValueMap
        self.lessIsMore = lessIsMore
    
    def __init__(self):
        self.providedQualityLevels = {}
        self.lessIsMore = False

    def setProvidedQuality(self, context, metric, value):
        map = {}

        if metric in self.providedQualityLevels:
            map = self.providedQualityLevels[metric]
            map[context] = value
            self.providedQualityLevels[metric] = map
        else:
            map[context] = value
            self.providedQualityLevels[metric] = map 

    def myProvidedQuality(self, metric, contextSet):
        myQuality = 0
        set = False

        if metric in self.providedQualityLevels:
            QLContexts = self.providedQualityLevels[metric].keys()
            for c in QLContexts:
                if 'None' == c.label:
                    myQuality = self.providedQualityLevels[metric][context]
                    set = True

        for current in contextSet:
            if metric in self.providedQualityLevels:
                if not set:
                    myQuality = self.providedQualityLevels[metric][current]
                    set = True
                else:
                    if metric.getLessIsBetter():
                        if(myQuality > self.providedQualityLevels[metric][current]):
                            myQuality = self.providedQualityLevels[metric][current]
                    elif(myQuality < self.providedQualityLevels[metric][current]):
                        myQuality = self.providedQualityLevels[metric][current]
    
        return myQuality
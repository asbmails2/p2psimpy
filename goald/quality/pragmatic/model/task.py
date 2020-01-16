from goald.quality.pragmatic.model.context import Context

class Task():
    def __init__(self, metric, contextValueMap):
        self.providedQualityLevels[metric] = contextValueMap;
    
    def __init__(self):
        self.providedQualityLevels = {}

    def setProvidedQuality(self, context, metric, value):
        map = {}

        #verificar se existe essa chave de metrica na providedQualityLevels
        #se sim substituir o value com novo value nesse contexto
        #senão criar novo quality level
        map[context.getName()] = value;
        self.providedQualityLevels[metric] = map;  

    def myProvidedQuality(self,metric, contextSet):
        myQuality = 0
        set = False

        #se existir a metric no providedQualityLevels set = true
        

        for current in contextSet:
            #se existir a metric no providedQualityLevels
            # !set set = true 
            myQuality = self.providedQualityLevels[metric][current.getName()]

        return myQuality


class Metrics():
    def __init__(self, *args):
        self.metricsMap = {}
        for elem in args:
            print(elem, elem[0], elem[1])
            self.metricsMap[elem[0]]=elem[1]
    def getLessIsBetter(self, metric):
        return self.metricsMap[metric]
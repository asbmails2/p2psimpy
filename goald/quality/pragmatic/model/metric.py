class CommonMetrics():
    def __init__(self):
        self.METERS = Metric('METERS', False)
        self.SECONDS = Metric('SECONDS', True)

class MetricsList():
    def __init__(self):
        self.metricsList = []
        
    def setMetricsList(self, *args):
        for item in args:
            self.metricsList.append(item)
    
    def getLessIsBetter(self, metric):
        index = self.metricsList.index(metric)
        return self.metricsList[index].getLessIsBetter()

class Metric():
    def __init__(self, name, lessIsBetter):
        self.name = name
        self.lessIsBetter = lessIsBetter

    def getLessIsBetter(self):
        return self.lessIsBetter
class QualityConstraint():

    def __init__(self, context, metric, value, comparison):
        self.aplicableContext = context
        self.metric = metric
        self.value = value
        self.comparison = comparison

    def getApplicableContext(self):
        return self.aplicableContext

    def abidesByQC(self, value, metric):
        #if metric in self.metric:
        if not self.compare(value):
            return False

        return True

    def compare(self, value):
        if self.comparison == "GREATER_THAN":
            if value > self.value:
                return True
            else:
                return False
        elif self.comparison == "GREATER_OR_EQUAL_TO":
            if value >= self.value:
                return True
            else:
                return False
        elif self.comparison == "EQUAL_TO":
            if value == self.value:
                return True
            else:
                return False
        elif self.comparison == "LESS_OR_EQUAL_TO":
            if value <= self.value:
                return True
            else:
                return False
        elif self.comparison == "LESS_THAN":
            if value < self.value:
                return True
            else:
                return False
        return False

    def stricterQC(self, qualityConstraint):
        if self.comparison in qualityConstraint.comparison:
            if qualityConstraint.compare(self.value):
                return self
            else:
                return qualityConstraint

        return None

    

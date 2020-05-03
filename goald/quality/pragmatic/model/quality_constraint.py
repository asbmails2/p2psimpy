from goald.quality.pragmatic.model.comparison import Comparison


class QualityConstraint():

    def __init__(self, context, metric, value, comparison):
        self.aplicableContext = context
        self.metric = metric
        self.value = value
        self.comparison = comparison

    def getApplicableContext(self):
        return self.aplicableContext

    def abidesByQC(self, value, metric):
        if metric is self.metric:
            self.compare(value)
            if self.compare(value) is False:
                return False

        return True

    def compare(self, value):
        if self.comparison == Comparison.GREATER_THAN:
            if value > self.value:
                return True
            else:
                return False
        elif self.comparison == Comparison.GREATER_OR_EQUAL_TO:
            if value >= self.value:
                return True
            else:
                return False
        elif self.comparison == Comparison.EQUAL_TO:
            if value == self.value:
                return True
            else:
                return False
        elif self.comparison == Comparison.LESS_OR_EQUAL_TO:
            if value <= self.value:
                return True
            else:
                return False
        elif self.comparison == Comparison.LESS_THAN:
            if value < self.value:
                return True
            else:
                return False
        return False

    def stricterQC(self, qualityConstraint):
        if self.comparison == qualityConstraint.comparison:
            if qualityConstraint.compare(self.value):
                return self
            else:
                return qualityConstraint

        return None

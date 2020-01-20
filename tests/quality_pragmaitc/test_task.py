from goald.quality.pragmatic.model.task import Task
from goald.quality.pragmatic.model.context import Context
from goald.quality.pragmatic.model.metric import CommonMetrics

def test_shouldProvideCorrectValueForMetric():
		task = Task()
		currentContext = Context("C1")
		baseline = Context(None)
		metric =  CommonMetrics()
		fullContext = set()

		fullContext.add(currentContext)
		fullContext.add(baseline)

		task.setProvidedQuality(currentContext, metric.METERS, 30.0)
		task.setProvidedQuality(baseline, metric.METERS, 50.0)

		assert 50.0 == task.myProvidedQuality(metric.METERS, fullContext)
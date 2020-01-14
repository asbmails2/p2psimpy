from goald.quality.pragmatic.model.task import Task
from goald.quality.pragmatic.model.context import Context
from goald.quality.pragmatic.model.metric import Metric

def test_shouldProvideCorrectValueForMetric():
		task = Task()
		currentContext = Context("C1")
		fullContext = set()
		fullContext.add(currentContext);

		task.setProvidedQuality(current, Metric.METERS, 30.0);

		assert 30.0 == task.myProvidedQuality(Metric.METERS, fullContext)
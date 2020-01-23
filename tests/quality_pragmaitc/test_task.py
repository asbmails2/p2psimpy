from goald.quality.pragmatic.model.task import Task
from goald.quality.pragmatic.model.context import Context
from goald.quality.pragmatic.model.common_metrics import CommonMetrics


def test_shouldProvideCorrectValueForMetric():
    task = Task()
    currentContext = Context("C1")
    baseline = Context(None)
    fullContext = set()

    fullContext.add(currentContext)
    fullContext.add(baseline)

    task.setProvidedQuality(currentContext, CommonMetrics.METERS, 30.0)
    task.setProvidedQuality(baseline, CommonMetrics.METERS, 50.0)

    assert 50.0 == task.myProvidedQuality(CommonMetrics.METERS, fullContext)

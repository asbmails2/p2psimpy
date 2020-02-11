from goald.quality.pragmatic.model.task import Task
from goald.quality.pragmatic.model.context import Context
from goald.quality.pragmatic.model.common_metrics import CommonMetrics
from goald.quality.pragmatic.exceptions.metric_not_found import MetricNotFoundException


def test_shouldProvideCorrectValueForMetric():
    task = Task("T1")
    currentContext = Context("C1")
    baseline = Context(None)
    fullContext = set()

    fullContext.add(currentContext)
    fullContext.add(baseline)

    task.setProvidedQuality(currentContext, CommonMetrics.METERS, 30.0)
    task.setProvidedQuality(baseline, CommonMetrics.METERS, 50.0)

    assert 50.0 == task.myProvidedQuality(CommonMetrics.METERS, fullContext)


def text_shouldProvideMetricForBaseline():
    task = Task("t1")

    current = Context("C1")
    fullContext = []
    fullContext.append(current)

    task.setProvidedQuality(None, CommonMetrics.METERS, 30.0)

    assert 30.0 == task.myProvidedQuality(CommonMetrics.METERS, fullContext)


def metricNotFound():
    task = Task()
    currentContext = Context("C1")
    fullContext = set()

    fullContext.add(currentContext)

    task.setProvidedQuality(currentContext, CommonMetrics.METERS, 30.0)

    try:
        task.myProvidedQuality(CommonMetrics.SECONDS, fullContext)
        assert False

    except MetricNotFoundException as exp:
        assert exp.message == 'Metric: SECONDS'


def test_OnlyBaselineDefined():
    task = Task()
    baseline = Context(None)
    fullContext = set()

    fullContext.add(baseline)

    task.setProvidedQuality(baseline, CommonMetrics.METERS, 50.0)

    assert 50.0 == task.myProvidedQuality(CommonMetrics.METERS, fullContext)


def test_shouldProvideSpecificContextMetric():
    task = Task()
    currentContext = Context("C1")
    baseline = Context(None)
    fullContext = set()

    fullContext.add(currentContext)
    fullContext.add(baseline)

    task.setProvidedQuality(currentContext, CommonMetrics.METERS, 50.0)
    task.setProvidedQuality(baseline, CommonMetrics.METERS, 30.0)

    assert 50.0 == task.myProvidedQuality(CommonMetrics.METERS, fullContext)

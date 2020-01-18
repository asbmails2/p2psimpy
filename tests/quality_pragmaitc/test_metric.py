from goald.quality.pragmatic.model.metric import MetricsList
from goald.quality.pragmatic.model.metric import Metric
from goald.quality.pragmatic.model.metric import CommonMetrics

def test_metric_list():
    metricsList = MetricsList()

    METERS = Metric('METERS', False)
    SECONDS = Metric('SECONDS', True)

    metricsList.setMetricsList(METERS, SECONDS)

    assert metricsList.getLessIsBetter(METERS) == False
    assert metricsList.getLessIsBetter(SECONDS) == True

def test_common_metrics():
    commonMetrics = CommonMetrics()

    assert commonMetrics.METERS.getLessIsBetter() == False
    assert commonMetrics.SECONDS.getLessIsBetter() == True

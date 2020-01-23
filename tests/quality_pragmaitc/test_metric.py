from goald.quality.pragmatic.model.common_metrics import CommonMetrics


def test_common_metrics():
    assert False is CommonMetrics.METERS.getLessIsBetter() 
    assert True is CommonMetrics.SECONDS.getLessIsBetter()

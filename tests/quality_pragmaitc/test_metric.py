from goald.quality.pragmatic.model.metric import Metrics

def test_metric_map():
    metrics = Metrics(('METERS', False))
    assert metrics.getLessIsBetter('METERS') == False

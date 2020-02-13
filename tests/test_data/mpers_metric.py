from goald.quality.pragmatic.model.metric import Metric

class MpersMetrics:
    FALSE_NEGATIVE_PERCENTAGE = Metric("False Negative", True)
    NOISE = Metric('Noise', True)
    SECONDS = Metric('Seconds', True)
    ERROR = Metric('Error', True)
    DISTANCE_ERROR = Metric('Distance', True)
    METERS = Metric('Meters', True)
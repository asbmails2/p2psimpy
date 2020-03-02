from goald.quality.pragmatic.model.metric import Metric

class MpersMetrics:
    FALSE_NEGATIVE_PERCENTAGE = Metric("False Negative")
    NOISE = Metric('Noise')
    SECONDS = Metric('Seconds')
    ERROR = Metric('Error')
    DISTANCE_ERROR = Metric('Distance')
    METERS = Metric('Meters')
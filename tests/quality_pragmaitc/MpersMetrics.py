from goald.quality.pragmatic.model.metric import Metric


class MpersMetrics:

    FALSE_NEGATIVE_PERCENTAGE = Metric("False Negative", True)
    NOISE = Metric('Noise', True)
    TIME = Metric('Time', True)
    ERROR = Metric('Error', True)

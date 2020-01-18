from goald.quality.pragmatic.model.metric import Metrics
from goald.quality.pragmatic.model.interpretation import Interpretation
from goald.quality.pragmatic.model.context import Context
from goald.quality.pragmatic.model.qualityConstraint import QualityConstraint


def test_interpretation():
    interp = Interpretation()
    context = Context("C1")
    metric = Metrics(('SECONDS', True))
    qc =  QualityConstraint(context, metric, 15, 'LESS_THAN')

    interp.addQualityConstraint(qc)
    map = interp.getContextDependentInterpretation()

    assert 1 == len(map)
    assert 1 == len(map[context])

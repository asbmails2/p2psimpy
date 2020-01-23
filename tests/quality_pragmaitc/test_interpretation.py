from goald.quality.pragmatic.model.common_metrics import CommonMetrics
from goald.quality.pragmatic.model.interpretation import Interpretation
from goald.quality.pragmatic.model.context import Context
from goald.quality.pragmatic.model.comparison import Comparison
from goald.quality.pragmatic.model.quality_constraint import QualityConstraint


def test_interpretation():
    interp = Interpretation()
    context = Context("C1")
    commonMetrics = CommonMetrics()
    qc = QualityConstraint(context, commonMetrics.SECONDS,
                           15, Comparison.LESS_THAN)

    interp.addQualityConstraint(qc)
    map = interp.getContextDependentInterpretation()

    assert 1 == len(map)
    assert 1 == len(map[context])

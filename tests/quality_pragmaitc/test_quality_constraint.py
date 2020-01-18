from goald.quality.pragmatic.model.qualityConstraint import QualityConstraint
from goald.quality.pragmatic.model.metric import CommonMetrics
from goald.quality.pragmatic.model.context import Context

def test_quality_constraint():
    commonMetrics = CommonMetrics()

    qc =  QualityConstraint(Context("C1"), commonMetrics.SECONDS, 15, 'LESS_THAN')
    assert True == qc.abidesByQC(13, commonMetrics.SECONDS)
    assert False == qc.abidesByQC(16, commonMetrics.SECONDS)

def test_should_select_stricter_constraint():
    commonMetrics = CommonMetrics()

    lessStrictQC = QualityConstraint(Context("C1"), commonMetrics.SECONDS, 15, 'LESS_THAN')
    moreStrictQC = QualityConstraint(Context("C2"), commonMetrics.SECONDS, 10, 'LESS_THAN')

    assert moreStrictQC == lessStrictQC.stricterQC(moreStrictQC)
    assert moreStrictQC == moreStrictQC.stricterQC(lessStrictQC)



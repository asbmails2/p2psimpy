from goald.quality.pragmatic.model.quality_constraint import QualityConstraint
from goald.quality.pragmatic.model.common_metrics import CommonMetrics
from goald.quality.pragmatic.model.context import Context
from goald.quality.pragmatic.model.comparison import Comparison


def test_quality_constraint():
    qc = QualityConstraint(
        Context("C1"), CommonMetrics.SECONDS, 15, Comparison.LESS_THAN)
    assert True is qc.abidesByQC(13, CommonMetrics.SECONDS)
    assert False is qc.abidesByQC(16, CommonMetrics.SECONDS)


def test_should_select_stricter_constraint():
    lessStrictQC = QualityConstraint(
        Context("C1"), CommonMetrics.SECONDS, 15, Comparison.LESS_THAN)
    moreStrictQC = QualityConstraint(
        Context("C2"), CommonMetrics.SECONDS, 10, Comparison.LESS_THAN)

    assert moreStrictQC is lessStrictQC.stricterQC(moreStrictQC)
    assert moreStrictQC is moreStrictQC.stricterQC(lessStrictQC)


def test_should_get_correct_threshold():
    qc = QualityConstraint(
        Context("C1"), CommonMetrics.SECONDS, 15, Comparison.LESS_THAN)
    print(qc.value)
    assert 15 == qc.value


def test_should_get_correct_comparison():
    qc = QualityConstraint(
        Context("C1"), CommonMetrics.SECONDS, 15, Comparison.LESS_THAN)
    assert Comparison.LESS_THAN is qc.comparison


def should_get_correct_metric():
    qc = QualityConstraint(
        Context("C1"), CommonMetrics.SECONDS, 15, Comparison.LESS_THAN)
    assert CommonMetrics.SECONDS is qc.metric

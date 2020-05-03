from goald.quality.pragmatic.model.quality_constraint import QualityConstraint
from goald.quality.pragmatic.model.common_metrics import CommonMetrics
from goald.quality.pragmatic.model.context import Context
from goald.quality.pragmatic.model.comparison import Comparison


def test_shouldBeBetterThan():
    qc = QualityConstraint(
        Context("C1"), CommonMetrics.SECONDS, 15, Comparison.LESS_THAN)
    assert True is qc.abidesByQC(13, CommonMetrics.SECONDS)
    assert False is qc.abidesByQC(16, CommonMetrics.SECONDS)


def test_shouldBeWorseThan():
    qc = QualityConstraint(
        Context("C2"), CommonMetrics.SECONDS, 15, Comparison.LESS_THAN)
    assert False is qc.abidesByQC(16, CommonMetrics.SECONDS)


def test_qualityConstraint():
    qc = QualityConstraint(
        Context("C1"), CommonMetrics.SECONDS, 15, Comparison.LESS_THAN)
    assert True is qc.abidesByQC(13, CommonMetrics.SECONDS)
    assert False is qc.abidesByQC(16, CommonMetrics.SECONDS)


def test_shouldSelectStricterConstraint():
    lessStrictQC = QualityConstraint(
        Context("C1"), CommonMetrics.SECONDS, 15, Comparison.LESS_THAN)
    moreStrictQC = QualityConstraint(
        Context("C2"), CommonMetrics.SECONDS, 10, Comparison.LESS_THAN)

    assert moreStrictQC is lessStrictQC.stricterQC(moreStrictQC)
    assert moreStrictQC is moreStrictQC.stricterQC(lessStrictQC)


def test_shouldGetCorrectThreshold():
    qc = QualityConstraint(
        Context("C1"), CommonMetrics.SECONDS, 15, Comparison.LESS_THAN)
    print(qc.value)
    assert 15 == qc.value


def test_shouldGetCorrectComparison():
    qc = QualityConstraint(
        Context("C1"), CommonMetrics.SECONDS, 15, Comparison.LESS_THAN)
    assert Comparison.LESS_THAN is qc.comparison


def test_shouldGetCorrectMetric():
    qc = QualityConstraint(
        Context("C1"), CommonMetrics.SECONDS, 15, Comparison.LESS_THAN)
    assert CommonMetrics.SECONDS is qc.metric


def test_shouldGetCorrectContexts():
    qc = QualityConstraint(
        Context("C1"), CommonMetrics.SECONDS, 15, Comparison.LESS_THAN)
    Context("C1") is qc.getApplicableContext()


def shouldAbideByQcIfMetricIsNotAffected():
    qc = QualityConstraint(
        Context("C1"), CommonMetrics.SECONDS, 15, Comparison.LESS_THAN)
    assert True is qc.abidesByQC(15, CommonMetrics.METERS)


def shouldCorrectlyCompareMetrics():

    qc = QualityConstraint(Context("C1"), CommonMetrics.SECONDS, 15,
                           Comparison.LESS_THAN)
    assert True is qc.abidesByQC(14, CommonMetrics.SECONDS)

    qc = QualityConstraint(Context("C1"), CommonMetrics.SECONDS, 15,
                           Comparison.LESS_OR_EQUAL_TO)
    assert True is qc.abidesByQC(14, CommonMetrics.SECONDS)

    qc = QualityConstraint(Context("C1"), CommonMetrics.SECONDS, 15,
                           Comparison.LESS_OR_EQUAL_TO)
    assert True is qc.abidesByQC(15, CommonMetrics.SECONDS)

    qc = QualityConstraint(Context("C1"), CommonMetrics.SECONDS, 15,
                           Comparison.EQUAL_TO)
    assert True is qc.abidesByQC(15, CommonMetrics.SECONDS)

    qc = QualityConstraint(Context("C1"), CommonMetrics.SECONDS, 15,
                           Comparison.GREATER_OR_EQUAL_TO)
    assert True is qc.abidesByQC(15, CommonMetrics.SECONDS)

    qc = QualityConstraint(Context("C1"), CommonMetrics.SECONDS, 15,
                           Comparison.GREATER_OR_EQUAL_TO)
    assert True is qc.abidesByQC(16, CommonMetrics.SECONDS)

    qc = QualityConstraint(Context("C1"), CommonMetrics.SECONDS, 15,
                           Comparison.GREATER_THAN)
    assert True is qc.abidesByQC(16, CommonMetrics.SECONDS)

    qc = QualityConstraint(Context("C1"), CommonMetrics.SECONDS, 15,
                           Comparison.LESS_THAN)
    assert False is qc.abidesByQC(16, CommonMetrics.SECONDS)

    qc = QualityConstraint(Context("C1"), CommonMetrics.SECONDS, 15,
                           Comparison.LESS_OR_EQUAL_TO)
    assert False is qc.abidesByQC(16, CommonMetrics.SECONDS)

    qc = QualityConstraint(Context("C1"), CommonMetrics.SECONDS, 15,
                           Comparison.EQUAL_TO)
    assert False is qc.abidesByQC(16, CommonMetrics.SECONDS)

    qc = QualityConstraint(Context("C1"), CommonMetrics.SECONDS, 15,
                           Comparison.GREATER_OR_EQUAL_TO)
    assert False is qc.abidesByQC(14, CommonMetrics.SECONDS)

    qc = QualityConstraint(Context("C1"), CommonMetrics.SECONDS, 15,
                           Comparison.GREATER_THAN)
    assert False is qc.abidesByQC(14, CommonMetrics.SECONDS)


def test_shouldComplainAboutDifferentMetrics():
    lessStrictQC = QualityConstraint(Context("C1"), CommonMetrics.SECONDS, 15,
                                     Comparison.LESS_THAN)
    moreStrictQC = QualityConstraint(Context("C2"), CommonMetrics.METERS, 10,
                                     Comparison.LESS_THAN)

    lessStrictQC.stricterQC(moreStrictQC)

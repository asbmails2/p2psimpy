from goald.quality.pragmatic.quality_evaluator import PragmaticQualityEvaluator
from goald.quality.pragmatic.model.context import Context
from goald.quality.pragmatic.model.quality_constraint import QualityConstraint
from goald.quality.pragmatic.model.common_metrics import CommonMetrics
from goald.quality.pragmatic.model.pragmatic import Pragmatic
from goald.quality.pragmatic.model.comparison import Comparison

pqe = PragmaticQualityEvaluator()

# def test_evaluate_empty():
#    quality = pqe.evaluateQuality("", {})
#    assert quality is None


def test_shouldGetDifferentQualityConstraintsForDifferentContexts():
    aContext = Context("c1")
    anotherContext = Context("c2")

    aQC = QualityConstraint(aContext, CommonMetrics.METERS,
                            30, Comparison.LESS_OR_EQUAL_TO)
    anotherQC = QualityConstraint(
        anotherContext, CommonMetrics.METERS, 60, Comparison.LESS_OR_EQUAL_TO)

    goal = Pragmatic(False)

    goal.interp.addQualityConstraint(aQC)
    goal.interp.addQualityConstraint(anotherQC)

    fullContext = []
    fullContext.append(aContext)

    assert aQC in goal.interp.getQualityConstraints(fullContext)

    anotherFullContext = []
    anotherFullContext.append(anotherContext)

    assert anotherQC in goal.interp.getQualityConstraints(anotherFullContext)

from goald.quality.pragmatic.quality_evaluator import PragmaticQualityEvaluator
from goald.quality.pragmatic.model.context import Context
from goald.quality.pragmatic.model.qualityConstraint import QualityConstraint
from goald.quality.pragmatic.model.interpretation import Interpretation
from goald.quality.pragmatic.model.metric import CommonMetrics
from goald.quality.pragmatic.model.pragmatic import Pragmatic

pqe = PragmaticQualityEvaluator()

def test_evaluate_empty():
    quality = pqe.evaluateQuality("", {})
    assert quality == None

def test_shouldGetDifferentQualityConstraintsForDifferentContexts():
    commonMetrics = CommonMetrics()
    aContext = Context("c1")
    anotherContext = Context("c2")

    aQC = QualityConstraint(aContext, commonMetrics.METERS, 30, 'LESS_OR_EQUAL_TO')
    anotherQC = QualityConstraint(anotherContext, commonMetrics.METERS, 60, 'LESS_OR_EQUAL_TO')

    goal = Pragmatic(False)

    goal.getInterpretation().addQualityConstraint(aQC)
    goal.getInterpretation().addQualityConstraint(anotherQC)

    fullContext = []
    fullContext.append(aContext)
    
    assert aQC in goal.getInterpretation().getQualityConstraints(fullContext)

    anotherFullContext = []
    anotherFullContext.append(anotherContext)    

    assert anotherQC in goal.getInterpretation().getQualityConstraints(anotherFullContext)
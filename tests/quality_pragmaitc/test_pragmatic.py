from goald.quality.pragmatic.quality_evaluator import PragmaticQualityEvaluator

pqe = PragmaticQualityEvaluator()

def test_evaluate_empty():
    quality = pqe.evaluateQuality("", {})
    assert quality == None


from goald.quality.pragmatic.model.qualityConstraint import QualityConstraint
from goald.quality.pragmatic.model.metric import Metrics
from goald.quality.pragmatic.model.context import Context

def test_quality_constraint():
    qc =  QualityConstraint(Context("C1"), Metrics(('SECONDS', True)), 15, 'LESS_THAN')
    assert True == qc.abidesByQC(13, Metrics(('SECONDS',True)))
    assert False == qc.abidesByQC(16, Metrics(('SECONDS', True)))

def test_should_select_stricter_constraint():
    lessStrictQC = QualityConstraint(Context("C1"), Metrics(('SECONDS', True)), 15, 'LESS_THAN')
    moreStrictQC = QualityConstraint(Context("C2"), Metrics(('SECONDS', True)), 10, 'LESS_THAN')
    print()
    assert moreStrictQC == lessStrictQC.stricterQC(moreStrictQC)
    assert moreStrictQC == moreStrictQC.stricterQC(lessStrictQC)

def test_should_get_correct_threshold():
		qc = QualityConstraint(Context("C1"), Metrics(('SECONDS', True)), 15, 'LESS_THAN')
		print(qc.value)
		assert 15 == qc.value

def test_should_get_correct_comparison():
		qc = QualityConstraint(Context("C1"), Metrics(('SECONDS', True)), 15, 'LESS_THAN')
		assert  'LESS_THAN' == qc.comparison
#find a way to fix the enum transformation
def should_get_correct_metric():
        qc = QualityConstraint(Context("C1"), Metrics(('SECONDS', True)), 15, 'LESS_THAN')
        assert 'SECONDS' == qc.metric
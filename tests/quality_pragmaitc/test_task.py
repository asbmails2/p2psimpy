from goald.quality.pragmatic.model.task import Task
from goald.quality.pragmatic.model.context import Context
from goald.quality.pragmatic.model.decomposition import Decomposition
from goald.quality.pragmatic.model.comparison import Comparison
from goald.quality.pragmatic.model.quality_constraint import QualityConstraint
from tests.test_data.mpers_metric import MpersMetrics
from goald.quality.pragmatic.model.pragmatic import Pragmatic
import pytest

c1 = Context("c1")
c2 = Context("c2")
c3 = Context("c3")
c4 = Context("c4")
c5 = Context("c5")
c6 = Context("c6")
c7 = Context("c7")
c8 = Context("c8")
c9 = Context("c9")
c10 = Context("c10")
c11 = Context("c11")
c12 = Context("c12")

notifyByMobileVibrationTask = Task("notifyByMobileVibrationTask")
notifyBySoundAlertTask = Task("notifyBySoundAlertTask")
notifyByLightAlertTask = Task("notifyByLightAlertTask")
centralCallTask = Task("centralCallsPTask")

notifyByMobileVibrationTask.setProvidedQuality(None, MpersMetrics.NOISE, 2)
notifyBySoundAlertTask.setProvidedQuality(None, MpersMetrics.NOISE, 9)
notifyByLightAlertTask.setProvidedQuality(None, MpersMetrics.NOISE, 0)
centralCallTask.setProvidedQuality(None, MpersMetrics.NOISE, 7)
centralCallTask.setProvidedQuality(c7, MpersMetrics.NOISE, 1)


@pytest.fixture
def isNotifiedAboutEmergencyGoal():

    isNotifiedAboutEmergencyGoal = Pragmatic(
        Decomposition.OR, "isNotifiedAboutEmergencyGoal")

    isNotifiedAboutEmergencyGoal.addDependency(notifyByMobileVibrationTask)
    isNotifiedAboutEmergencyGoal.addDependency(notifyBySoundAlertTask)
    isNotifiedAboutEmergencyGoal.addDependency(notifyByLightAlertTask)
    isNotifiedAboutEmergencyGoal.addDependency(centralCallTask)

    notifyByMobileVibrationTask.addApplicableContext(c1)

    notifyBySoundAlertTask.addApplicableContext(c6)

    notifyByLightAlertTask.addApplicableContext(c7)

    centralCallTask.addApplicableContext(c8)

    baseline = QualityConstraint(None, MpersMetrics.NOISE, 10,
                                 Comparison.LESS_OR_EQUAL_TO)
    qc1 = QualityConstraint(c9, MpersMetrics.NOISE, 3,
                            Comparison.LESS_OR_EQUAL_TO)

    isNotifiedAboutEmergencyGoal.interp.addQualityConstraint(baseline)
    isNotifiedAboutEmergencyGoal.interp.addQualityConstraint(qc1)

    return isNotifiedAboutEmergencyGoal


considerLastKnownLocationTask = Task("considerLastKnownLocationTask")
identifyLocationByVoiceCallTask = Task("identifyLocationByVoiceCallTask")
accessLocationFromTriangulationTask = Task(
    "accessLocationFromTriangulationTask")
accessLocationFromGPSTask = Task("accessLocationFromGPSTask")
accessDataFromDatabaseTask = Task("accessDataFromDatabaseTask")

considerLastKnownLocationTask.setProvidedQuality(
    None, MpersMetrics.DISTANCE_ERROR, 900)
considerLastKnownLocationTask.setProvidedQuality(
    None, MpersMetrics.SECONDS, 15)

identifyLocationByVoiceCallTask.setProvidedQuality(
    None, MpersMetrics.DISTANCE_ERROR, 100)
identifyLocationByVoiceCallTask.setProvidedQuality(
    c11, MpersMetrics.DISTANCE_ERROR, 300)
identifyLocationByVoiceCallTask.setProvidedQuality(
    None, MpersMetrics.SECONDS, 45)

accessLocationFromTriangulationTask.setProvidedQuality(
    None, MpersMetrics.DISTANCE_ERROR, 40)
accessLocationFromTriangulationTask.setProvidedQuality(
    c11, MpersMetrics.DISTANCE_ERROR, 300)
accessLocationFromTriangulationTask.setProvidedQuality(
    None, MpersMetrics.SECONDS, 30)

accessLocationFromGPSTask.setProvidedQuality(
    None, MpersMetrics.DISTANCE_ERROR, 20)
accessLocationFromGPSTask.setProvidedQuality(
    c11, MpersMetrics.DISTANCE_ERROR, 30)
accessLocationFromGPSTask.setProvidedQuality(
    None, MpersMetrics.SECONDS, 50)


@pytest.fixture
def locationIsIdentifiedGoal():

    locationIsIdentifiedGoal = Pragmatic(
        Decomposition.OR, "locationIsIdentifiedGoal")

    qc4 = QualityConstraint(None, MpersMetrics.DISTANCE_ERROR, 1000,
                            Comparison.LESS_OR_EQUAL_TO)
    qc6 = QualityConstraint(c5, MpersMetrics.DISTANCE_ERROR,
                            20, Comparison.LESS_OR_EQUAL_TO)
    qc5 = QualityConstraint(c10, MpersMetrics.DISTANCE_ERROR,
                            200, Comparison.LESS_OR_EQUAL_TO)
    qc1 = QualityConstraint(None, MpersMetrics.SECONDS, 120,
                            Comparison.LESS_OR_EQUAL_TO)
    qc3 = QualityConstraint(c9, MpersMetrics.SECONDS, 240,
                            Comparison.LESS_OR_EQUAL_TO)
    qc2 = QualityConstraint(c10, MpersMetrics.SECONDS, 20,
                            Comparison.LESS_OR_EQUAL_TO)

    locationIsIdentifiedGoal.interp.addQualityConstraint(qc1)
    locationIsIdentifiedGoal.interp.addQualityConstraint(qc2)
    locationIsIdentifiedGoal.interp.addQualityConstraint(qc3)
    locationIsIdentifiedGoal.interp.addQualityConstraint(qc4)
    locationIsIdentifiedGoal.interp.addQualityConstraint(qc5)
    locationIsIdentifiedGoal.interp.addQualityConstraint(qc6)

    locationIsIdentifiedGoal.addDependency(considerLastKnownLocationTask)
    locationIsIdentifiedGoal.addDependency(identifyLocationByVoiceCallTask)
    locationIsIdentifiedGoal.addDependency(accessLocationFromGPSTask)
    locationIsIdentifiedGoal.addDependency(accessLocationFromTriangulationTask)

    return locationIsIdentifiedGoal


def test_shouldProvideCorrectValueForMetric():
    task = Task("T1")
    currentContext = Context("C1")
    fullContext = set()

    fullContext.add(currentContext)

    task.setProvidedQuality(currentContext, MpersMetrics.METERS, 30)

    assert 30 == task.myProvidedQuality(MpersMetrics.METERS, fullContext)


def text_shouldProvideMetricForBaseline():
    task = Task("t1")

    current = Context("C1")
    fullContext = []
    fullContext.append(current)

    task.setProvidedQuality(None, MpersMetrics.METERS, 30.0)

    assert 30.0 == task.myProvidedQuality(MpersMetrics.METERS, fullContext)


def metricNotFound():
    task = Task()
    currentContext = Context("C1")
    fullContext = set()

    fullContext.add(currentContext)

    task.setProvidedQuality(currentContext, MpersMetrics.METERS, 30.0)

    result = task.myProvidedQuality(MpersMetrics.SECONDS, fullContext)
    assert result is None


def test_OnlyBaselineDefined():
    task = Task()
    baseline = Context(None)
    fullContext = set()

    fullContext.add(baseline)

    task.setProvidedQuality(baseline, MpersMetrics.METERS, 50.0)

    assert 50.0 == task.myProvidedQuality(MpersMetrics.METERS, fullContext)


def test_shouldProvideSpecificContextMetric():
    task = Task()
    currentContext = Context("C1")
    baseline = None
    fullContext = set()

    fullContext.add(currentContext)
    fullContext.add(baseline)

    task.setProvidedQuality(currentContext, MpersMetrics.METERS, 50)
    task.setProvidedQuality(baseline, MpersMetrics.METERS, 30)

    assert 50 == task.myProvidedQuality(MpersMetrics.METERS, fullContext)


def test_abidesByInterpretation_passing_baseline(isNotifiedAboutEmergencyGoal):
    context = [c1]
    result = notifyByMobileVibrationTask.abidesByInterpretation(
        isNotifiedAboutEmergencyGoal.interp, context)
    assert result == True

    context = [c9]
    result = notifyByMobileVibrationTask.abidesByInterpretation(
        isNotifiedAboutEmergencyGoal.interp, context)
    assert result == True


def test_abidesByInterpretation_not_passing_baseline(isNotifiedAboutEmergencyGoal):
    context = [c6]
    result = notifyBySoundAlertTask.abidesByInterpretation(
        isNotifiedAboutEmergencyGoal.interp, context)
    assert result == True

    context = [c9]
    result = notifyBySoundAlertTask.abidesByInterpretation(
        isNotifiedAboutEmergencyGoal.interp, context)
    assert result == False


def test_abidesByInterpretation_only_baseline(locationIsIdentifiedGoal):
    context = []

    result = considerLastKnownLocationTask.abidesByInterpretation(
        locationIsIdentifiedGoal.interp, context)
    assert result == True


def test_abidesByInterpretation_only_baseline_context(locationIsIdentifiedGoal):
    context = [c1, c2, c3]

    result = considerLastKnownLocationTask.abidesByInterpretation(
        locationIsIdentifiedGoal.interp, context)
    assert result == True


def test_abidesByInterpretation_context_not_passing(locationIsIdentifiedGoal):
    context = []

    result = identifyLocationByVoiceCallTask.abidesByInterpretation(
        locationIsIdentifiedGoal.interp, context)
    assert result == True

    context.append(c5)

    result = identifyLocationByVoiceCallTask.abidesByInterpretation(
        locationIsIdentifiedGoal.interp, context)
    assert result == False


def test_abidesByInterpretation_only_baseline_not_passing(locationIsIdentifiedGoal):
    context = []

    LongSecondsTask = Task("LongSecondsTask")
    LongSecondsTask.setProvidedQuality(
        None, MpersMetrics.SECONDS, 1500)

    result = LongSecondsTask.abidesByInterpretation(
        locationIsIdentifiedGoal.interp, context)
    assert result == False


def test_myQualityBaseline(locationIsIdentifiedGoal):
    context = [c2]
    result = accessLocationFromTriangulationTask.myProvidedQuality(
        MpersMetrics.DISTANCE_ERROR, context)
    assert result == 40

    context.append(c11)
    result = accessLocationFromTriangulationTask.myProvidedQuality(
        MpersMetrics.DISTANCE_ERROR, context)
    assert result == 300


def test_myQualityStrict(locationIsIdentifiedGoal):
    context = []
    result = centralCallTask.myProvidedQuality(MpersMetrics.NOISE, context)
    assert result == 7

    context.append(c7)
    result = centralCallTask.myProvidedQuality(MpersMetrics.NOISE, context)
    assert result == 7

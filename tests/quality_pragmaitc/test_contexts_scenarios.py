from goald.quality.pragmatic.model.context import Context
from goald.quality.pragmatic.model.pragmatic import Pragmatic
from goald.quality.pragmatic.model.goal import Goal
from goald.quality.pragmatic.model.decomposition import Decomposition
from goald.quality.pragmatic.model.task import Task
from goald.quality.pragmatic.model.metric import Metric
from goald.quality.pragmatic.model.quality_constraint import QualityConstraint
from goald.quality.pragmatic.model.comparison import Comparison
from goald.quality.pragmatic.model.interpretation import Interpretation
from goald.utils.context_generator import ContextGenerator
from goald.utils.print import print_context
from tests.utils.assert_util import assertPlan
from tests.test_data.mpers_metric import MpersMetrics

import pytest

# Contexts
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

# Tasks
notifyCentralBySMSTask = Task("notifyCentralBySMSTask")
notifyCentralByInternetTask = Task("notifyCentralByInternetTask")
acceptEmergencyTask = Task("acceptEmergencyTask")
confirmEmergencyByCallTask = Task("confirmEmergencyByCallTask")
processDataFromSensorsTask = Task("processDataFromSensorsTask")
identifySituationTask = Task("identifySituationTask")
collectDataFromSensorsTask = Task("collectDataFromSensorsTask")
persistDataToDatabaseTask = Task("persistDataToDatabaseTask")
notifyByMobileVibrationTask = Task("notifyByMobileVibrationTask")
notifyBySoundAlertTask = Task("notifyBySoundAlertTask")
notifyByLightAlertTask = Task("notifyByLightAlertTask")
centralCallTask = Task("centralCallsPTask")
sendInfoBySMSTask = Task("sendInfoBySMSTask")
sendInfoByInternetTask = Task("sendInfoByInternetTask")
considerLastKnownLocationTask = Task("considerLastKnownLocationTask")
identifyLocationByVoiceCallTask = Task("identifyLocationByVoiceCallTask")
accessLocationFromTriangulationTask = Task(
    "accessLocationFromTriangulationTask")
accessLocationFromGPSTask = Task("accessLocationFromGPSTask")
accessDataFromDatabaseTask = Task("accessDataFromDatabaseTask")
getInfoFromResponsibleTask = Task("getInfoFromResponsibleTask")
ambulanceDispatchDelegationTask = Task("ambulanceDispatchDelegationTask")


@pytest.fixture
def rootGoal():

    # Goals
    respondToEmergencyGoal = Pragmatic(Decomposition.AND, "respondToEmergency")
    emergencyIsDetectedGoal = Pragmatic(
        Decomposition.OR, "emergencyIsDetected")
    centralReceivesInfoGoal = Pragmatic(
        Decomposition.AND, "centralReceivesInfo")
    locationIsIdentifiedGoal = Pragmatic(
        Decomposition.OR, "locationIsIdentified")
    infoIsPreparedGoal = Pragmatic(Decomposition.OR, "infoIsPrepared")
    isNotifiedAboutEmergencyGoal = Pragmatic(
        Decomposition.OR, "isNotifiedAboutEmergency")
    callForHelpIsAcceptedGoal = Goal(
        Decomposition.AND, "callForHelpIsAccepted")
    falseAlarmIsCheckedGoal = Goal(Decomposition.OR, "falseAlarmIsChecked")
    pIsContactedGoal = Goal(Decomposition.AND, "pIsContacted")
    receivesEmergencyButtonCallGoal = Goal(
        Decomposition.OR, "receivesEmergencyButtonCall")
    situationsAreIdentifiedGoal = Goal(
        Decomposition.AND, "situationsAreIdentified")
    vitalSignsAreMonitoredGoal = Goal(
        Decomposition.AND, "vitalSignsAreMonitored")
    infoIsSentToEmergencyGoal = Goal(Decomposition.OR, "infoIsSentToEmergency")
    setupAutomatedInfoGoal = Goal(Decomposition.AND, "setupAutomatedInfo")
    situationDataIsRecoveredGoal = Goal(
        Decomposition.AND, "situationDataIsRecovered")
    contactResponsibleGoal = Goal(Decomposition.AND, "contactResponsible")
    medicalCareReachesGoal = Goal(Decomposition.AND, "medicalCareReaches")
    ambulanceIsDispatchedToLocationGoal = Goal(
        Decomposition.AND, "ambulanceIsDispatchedToLocation")

    # Refinements
    respondToEmergencyGoal.addDependency(emergencyIsDetectedGoal)
    respondToEmergencyGoal.addDependency(isNotifiedAboutEmergencyGoal)
    respondToEmergencyGoal.addDependency(centralReceivesInfoGoal)
    respondToEmergencyGoal.addDependency(medicalCareReachesGoal)

    emergencyIsDetectedGoal.addDependency(callForHelpIsAcceptedGoal)
    emergencyIsDetectedGoal.addDependency(situationsAreIdentifiedGoal)

    callForHelpIsAcceptedGoal.addDependency(
        receivesEmergencyButtonCallGoal)
    callForHelpIsAcceptedGoal.addDependency(falseAlarmIsCheckedGoal)

    receivesEmergencyButtonCallGoal.addDependency(notifyCentralBySMSTask)
    receivesEmergencyButtonCallGoal.addDependency(
        notifyCentralByInternetTask)

    falseAlarmIsCheckedGoal.addDependency(acceptEmergencyTask)
    falseAlarmIsCheckedGoal.addDependency(pIsContactedGoal)

    pIsContactedGoal.addDependency(confirmEmergencyByCallTask)

    situationsAreIdentifiedGoal.addDependency(processDataFromSensorsTask)
    situationsAreIdentifiedGoal.addDependency(vitalSignsAreMonitoredGoal)
    situationsAreIdentifiedGoal.addDependency(identifySituationTask)

    vitalSignsAreMonitoredGoal.addDependency(collectDataFromSensorsTask)
    vitalSignsAreMonitoredGoal.addDependency(persistDataToDatabaseTask)

    isNotifiedAboutEmergencyGoal.addDependency(notifyByMobileVibrationTask)
    isNotifiedAboutEmergencyGoal.addDependency(notifyBySoundAlertTask)
    isNotifiedAboutEmergencyGoal.addDependency(notifyByLightAlertTask)
    isNotifiedAboutEmergencyGoal.addDependency(centralCallTask)

    centralReceivesInfoGoal.addDependency(infoIsSentToEmergencyGoal)
    centralReceivesInfoGoal.addDependency(infoIsPreparedGoal)

    infoIsSentToEmergencyGoal.addDependency(sendInfoBySMSTask)
    infoIsSentToEmergencyGoal.addDependency(sendInfoByInternetTask)

    infoIsPreparedGoal.addDependency(setupAutomatedInfoGoal)
    infoIsPreparedGoal.addDependency(contactResponsibleGoal)

    setupAutomatedInfoGoal.addDependency(locationIsIdentifiedGoal)
    setupAutomatedInfoGoal.addDependency(situationDataIsRecoveredGoal)

    locationIsIdentifiedGoal.addDependency(considerLastKnownLocationTask)
    locationIsIdentifiedGoal.addDependency(identifyLocationByVoiceCallTask)
    locationIsIdentifiedGoal.addDependency(accessLocationFromGPSTask)
    locationIsIdentifiedGoal.addDependency(
        accessLocationFromTriangulationTask)

    situationDataIsRecoveredGoal.addDependency(accessDataFromDatabaseTask)

    contactResponsibleGoal.addDependency(getInfoFromResponsibleTask)

    medicalCareReachesGoal.addDependency(
        ambulanceIsDispatchedToLocationGoal)

    ambulanceIsDispatchedToLocationGoal.addDependency(
        ambulanceDispatchDelegationTask)

    # Applicable Contexts

    notifyCentralBySMSTask.addApplicableContext(c2)

    notifyCentralByInternetTask.addApplicableContext(c3)
    notifyCentralByInternetTask.addApplicableContext(c4)

    acceptEmergencyTask.addNonapplicableContext(c2)

    confirmEmergencyByCallTask.addApplicableContext(c2)

    notifyByMobileVibrationTask.addApplicableContext(c1)

    notifyBySoundAlertTask.addApplicableContext(c6)

    notifyByLightAlertTask.addApplicableContext(c7)

    centralCallTask.addApplicableContext(c8)

    sendInfoBySMSTask.addApplicableContext(c2)

    sendInfoByInternetTask.addApplicableContext(c3)
    sendInfoByInternetTask.addApplicableContext(c4)

    identifyLocationByVoiceCallTask.addApplicableContext(c2)

    accessLocationFromTriangulationTask.addApplicableContext(c2)

    accessLocationFromGPSTask.addApplicableContext(c5)

    # Goal Interpretations

    qc1 = QualityConstraint(None, MpersMetrics.SECONDS,
                            180, Comparison.LESS_THAN)
    qc2 = QualityConstraint(
        c10, MpersMetrics.SECONDS, 90, Comparison.LESS_THAN)
    qc3 = QualityConstraint(c9, MpersMetrics.SECONDS,
                            240, Comparison.LESS_THAN)
    respondToEmergencyGoal.interp.addQualityConstraint(qc1)
    respondToEmergencyGoal.interp.addQualityConstraint(qc2)
    respondToEmergencyGoal.interp.addQualityConstraint(qc3)

    qc1 = QualityConstraint(None, MpersMetrics.FALSE_NEGATIVE_PERCENTAGE, 30,
                            Comparison.LESS_THAN)
    qc2 = QualityConstraint(c3, MpersMetrics.FALSE_NEGATIVE_PERCENTAGE, 10,
                            Comparison.LESS_THAN)
    qc3 = QualityConstraint(
        c9, MpersMetrics.FALSE_NEGATIVE_PERCENTAGE, 5, Comparison.LESS_THAN)
    emergencyIsDetectedGoal.interp.addQualityConstraint(qc1)
    emergencyIsDetectedGoal.interp.addQualityConstraint(qc2)
    emergencyIsDetectedGoal.interp.addQualityConstraint(qc3)

    qc1 = QualityConstraint(None, MpersMetrics.SECONDS, 60, Comparison.LESS_THAN)
    centralReceivesInfoGoal.interp.addQualityConstraint(qc1)

    qc4 = QualityConstraint(None, MpersMetrics.DISTANCE_ERROR,
                            1000, Comparison.LESS_THAN)
    qc6 = QualityConstraint(
        c5, MpersMetrics.DISTANCE_ERROR, 20, Comparison.LESS_THAN)
    qc5 = QualityConstraint(
        c10, MpersMetrics.DISTANCE_ERROR, 200, Comparison.LESS_THAN)
    qc1 = QualityConstraint(None, MpersMetrics.SECONDS,
                            120, Comparison.LESS_THAN)
    qc3 = QualityConstraint(c9, MpersMetrics.SECONDS, 240, Comparison.LESS_THAN)
    qc2 = QualityConstraint(c10, MpersMetrics.SECONDS, 20, Comparison.LESS_THAN)
    locationIsIdentifiedGoal.interp.addQualityConstraint(qc1)
    locationIsIdentifiedGoal.interp.addQualityConstraint(qc2)
    locationIsIdentifiedGoal.interp.addQualityConstraint(qc3)
    locationIsIdentifiedGoal.interp.addQualityConstraint(qc4)
    locationIsIdentifiedGoal.interp.addQualityConstraint(qc5)
    locationIsIdentifiedGoal.interp.addQualityConstraint(qc6)

    qc1 = QualityConstraint(None, MpersMetrics.SECONDS, 900, Comparison.LESS_THAN)
    qc2 = QualityConstraint(c10, MpersMetrics.SECONDS,
                            600, Comparison.LESS_THAN)
    infoIsPreparedGoal.interp.addQualityConstraint(qc1)
    infoIsPreparedGoal.interp.addQualityConstraint(qc2)

    qc1 = QualityConstraint(None, MpersMetrics.NOISE, 10, Comparison.LESS_THAN)
    qc2 = QualityConstraint(c1, MpersMetrics.NOISE, 3, Comparison.LESS_THAN)
    isNotifiedAboutEmergencyGoal.interp.addQualityConstraint(qc1)
    isNotifiedAboutEmergencyGoal.interp.addQualityConstraint(qc2)

    # Provided Task QoS

    notifyCentralBySMSTask.setProvidedQuality(
        None, MpersMetrics.FALSE_NEGATIVE_PERCENTAGE, 10)

    notifyCentralByInternetTask.setProvidedQuality(
        None, MpersMetrics.FALSE_NEGATIVE_PERCENTAGE, 5)

    acceptEmergencyTask.setProvidedQuality(
        None, MpersMetrics.FALSE_NEGATIVE_PERCENTAGE, 30)

    confirmEmergencyByCallTask.setProvidedQuality(
        None, MpersMetrics.FALSE_NEGATIVE_PERCENTAGE, 5)

    processDataFromSensorsTask.setProvidedQuality(
        None, MpersMetrics.FALSE_NEGATIVE_PERCENTAGE, 15)

    collectDataFromSensorsTask.setProvidedQuality(
        None, MpersMetrics.SECONDS, 120)
    collectDataFromSensorsTask.setProvidedQuality(
        c3, MpersMetrics.SECONDS, 60)

    persistDataToDatabaseTask.setProvidedQuality(
        None, MpersMetrics.SECONDS, 5)

    identifySituationTask.setProvidedQuality(
        None, MpersMetrics.FALSE_NEGATIVE_PERCENTAGE, 20)

    notifyByMobileVibrationTask.setProvidedQuality(
        None, MpersMetrics.NOISE, 2)
    notifyBySoundAlertTask.setProvidedQuality(None, MpersMetrics.NOISE, 9)
    notifyByLightAlertTask.setProvidedQuality(None, MpersMetrics.NOISE, 0)
    centralCallTask.setProvidedQuality(None, MpersMetrics.NOISE, 7)

    sendInfoBySMSTask.setProvidedQuality(None, MpersMetrics.SECONDS, 65)
    sendInfoBySMSTask.setProvidedQuality(c8, MpersMetrics.SECONDS, 45)

    sendInfoByInternetTask.setProvidedQuality(None, MpersMetrics.SECONDS, 40)

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
        c11, MpersMetrics.DISTANCE_ERROR, 400)
    accessLocationFromTriangulationTask.setProvidedQuality(
        None, MpersMetrics.SECONDS, 30)

    accessLocationFromGPSTask.setProvidedQuality(
        None, MpersMetrics.DISTANCE_ERROR, 20)
    accessLocationFromGPSTask.setProvidedQuality(
        c11, MpersMetrics.DISTANCE_ERROR, 30)
    accessLocationFromGPSTask.setProvidedQuality(
        None, MpersMetrics.SECONDS, 50)

    accessDataFromDatabaseTask.setProvidedQuality(
        None, MpersMetrics.SECONDS, 20)

    getInfoFromResponsibleTask.setProvidedQuality(
        None, MpersMetrics.SECONDS, 25)
    getInfoFromResponsibleTask.setProvidedQuality(
        c11, MpersMetrics.SECONDS, 50)

    ambulanceDispatchDelegationTask.setProvidedQuality(
        None, MpersMetrics.SECONDS, 30)

    rootGoal = Goal(Decomposition.AND, "rootGoal")
    rootGoal = respondToEmergencyGoal

    return rootGoal


def test_C1(rootGoal):
    fullContext = [c1, c2, c4, c5, c7, c8, c10, c12]
    plan = rootGoal.isAchievable(fullContext, None)

    assert plan is not None

    assert False is assertPlan(
        plan, [accessLocationFromGPSTask, centralCallTask])



def test_C2(rootGoal):
    fullContext = [c1, c2, c4, c6, c7, c8, c10, c12]
    tasks = rootGoal.isAchievable(fullContext, None)

    assert tasks is not None

    for task in rootGoal.isAchievable(fullContext, None).getTasks():
        found = 0

        if task.getIdentifier() == "acceptEmergency":
            found = 1
        if task.getIdentifier() == "notifyBySoundAlert":
            found = 1

        assert found == 0
    

def test_C3(rootGoal):
    fullContext = [c1, c2, c3, c4, c5, c6, c7, c8]

    tasks = rootGoal.isAchievable(fullContext, None)

    assert tasks is not None

    for task in rootGoal.isAchievable(fullContext, None).getTasks():
        found = 0

        if task.getIdentifier() == "acceptEmergency":
            found = 1

        assert found == 0


def test_C4(rootGoal):
    print("=========== Test C4 ================")
    fullContext = [c1, c4, c6, c7, c8, c10, c12]
    tasks = rootGoal.isAchievable(fullContext, None)

    assert tasks is not None

    for task in rootGoal.isAchievable(fullContext, None).getTasks():
        found = 0

        if task.getIdentifier() == "notifyCentralBySMS":
            found = 1
        if task.getIdentifier() == "confirmEmergencyByCall":
            found = 1
        if task.getIdentifier() == "notifyBySoundAlert":
            found = 1
        if task.getIdentifier() == "sendInfoBySMS":
            found = 1
        if task.getIdentifier() == "identifyLocationByVoiceCall":
            found = 1
        if task.getIdentifier() == "accessLocationFromTriangulation":
            found = 1

        assert found == 0


def test_C5(rootGoal):
    print("=========== Test C5 ================")
    fullContext = [c1, c4, c5, c7, c8, c10, c12]
    tasks = rootGoal.isAchievable(fullContext, None)

    assert tasks is not None

    for task in rootGoal.isAchievable(fullContext, None).getTasks():
        found = 0

        if task.getIdentifier() == "notifyCentralBySMS":
            found = 1
        if task.getIdentifier() == "notifyBySoundAlert":
            found = 1
        if task.getIdentifier() == "sendInfoBySMS":
            found = 1
        if task.getIdentifier() == "confirmEmergencyByCall":
            found = 1

        assert found == 0


def test_C6(rootGoal):
    print("=========== Test C6 ================")
    fullContext = [c1, c4, c5, c6, c7, c8, c10, c12]
    tasks = rootGoal.isAchievable(fullContext, None)

    assert tasks is not None

    for task in rootGoal.isAchievable(fullContext, None).getTasks():
        found = 0

        if task.getIdentifier() == "notifyCentralBySMS":
            found = 1
        if task.getIdentifier() == "sendInfoBySMS":
            found = 1
        if task.getIdentifier() == "confirmEmergencyByCall":
            found = 1

        assert found == 0


def test_C7(rootGoal):
    print("=========== Test C7 ================")
    fullContext = [c1, c4, c6, c7, c8, c10, c12]
    tasks = rootGoal.isAchievable(fullContext, None)

    assert tasks is not None

    for task in rootGoal.isAchievable(fullContext, None).getTasks():
        found = 0

        if task.getIdentifier() == "notifyCentralBySMS":
            found = 1
        if task.getIdentifier() == "confirmEmergencyByCall":
            found = 1
        if task.getIdentifier() == "notifyBySoundAlert":
            found = 1
        if task.getIdentifier() == "sendInfoBySMS":
            found = 1
        if task.getIdentifier() == "identifyLocationByVoiceCall":
            found = 1
        if task.getIdentifier() == "accessLocationFromTriangulation":
            found = 1
        if task.getIdentifier() == "accessLocationFromGPS":
            found = 1

        assert found == 0


def test_C8(rootGoal):
    print("=========== Test C8 ================")
    fullContext = [c1, c4, c5, c7, c8, c10, c12]
    tasks = rootGoal.isAchievable(fullContext, None)

    assert tasks is not None

    for task in rootGoal.isAchievable(fullContext, None).getTasks():
        found = 0

        if task.getIdentifier() == "notifyCentralBySMS":
            found = 1
        if task.getIdentifier() == "confirmEmergencyByCall":
            found = 1
        if task.getIdentifier() == "notifyBySoundAlert":
            found = 1
        if task.getIdentifier() == "sendInfoBySMS":
            found = 1
        if task.getIdentifier() == "identifyLocationByVoiceCall":
            found = 1
        if task.getIdentifier() == "accessLocationFromTriangulation":
            found = 1

        assert found == 0


def test_C9(rootGoal):
    print("=========== Test C9 ================")
    fullContext = [c1, c2, c4, c5, c6, c9]
    tasks = rootGoal.isAchievable(fullContext, None)

    assert tasks is not None

    for task in rootGoal.isAchievable(fullContext, None).getTasks():
        found = 0

        if task.getIdentifier() == "notifyByLightAlert":
            found = 1
        if task.getIdentifier() == "acceptsEmergency":
            found = 1

        assert found == 0


def test_C10(rootGoal):
    print("=========== Test C10 ================")
    fullContext = [c1, c2, c3, c5, c6, c8, c10, c12]
    tasks = rootGoal.isAchievable(fullContext, None)

    assert tasks is not None

    for task in rootGoal.isAchievable(fullContext, None).getTasks():
        found = 0

        if task.getIdentifier() == "notifyByLightAlert":
            found = 1
        if task.getIdentifier() == "acceptEmergency":
            found = 1

        assert found == 0


def test_C11(rootGoal):
    fullContext = [c1, c4, c5, c10, c11, c12]
    tasks = rootGoal.isAchievable(fullContext, None)

    assert tasks is not None

    for task in rootGoal.isAchievable(fullContext, None).getTasks():
        found = 0

        if task.getIdentifier() == "notifyCentralBySMS":
            found = 1
        if task.getIdentifier() == "confirmEmergencyByCall":
            found = 1
        if task.getIdentifier() == "notifyByLightAlert":
            found = 1
        if task.getIdentifier() == "sendInfoBySMS":
            found = 1

        assert found == 0


def test_C12(rootGoal):
    print("=========== Test C12 ================")
    fullContext = [c1, c4, c5, c7, c8, c10, c12]
    tasks = rootGoal.isAchievable(fullContext, None)

    assert tasks is not None

    for task in rootGoal.isAchievable(fullContext, None).getTasks():
        found = 0

        if task.getIdentifier() == "notifyCentralBySMS":
            found = 1
        if task.getIdentifier() == "confirmEmergencyByCall":
            found = 1
        if task.getIdentifier() == "sendInfoBySMS":
            found = 1

        assert found == 0


def test_All(rootGoal):
    print("=========== Test ALL ================")
    fullContext = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12]
    tasks = rootGoal.isAchievable(fullContext, None)

    assert tasks

    for task in rootGoal.isAchievable(fullContext, None).getTasks():
        found = 0

        if task.getIdentifier() == "acceptEmergency":
            found = 1

        assert found == 0


def test_None(rootGoal):
    print("=========== Test None ================")
    fullContext = []
    tasks = rootGoal.isAchievable(fullContext, None)

    assert tasks is None

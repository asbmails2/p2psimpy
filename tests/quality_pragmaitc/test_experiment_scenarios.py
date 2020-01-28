from goald.quality.pragmatic.model.context import Context
from goald.quality.pragmatic.model.pragmatic import Pragmatic
from goald.quality.pragmatic.model.goal import Goal
from goald.quality.pragmatic.model.decomposition import Decomposition
from goald.quality.pragmatic.model.task import Task
from goald.quality.pragmatic.model.metric import Metric
from goald.quality.pragmatic.model.quality_constraint import QualityConstraint
from goald.quality.pragmatic.model.comparison import Comparison
from goald.utils.context_generator import ContextGenerator


class MpersMetrics:
    FALSE_NEGATIVE_PERCENTAGE = Metric("False Negative", True)
    NOISE = Metric('Noise', True)
    TIME = Metric('Time', True)
    ERROR = Metric('Error', True)
    DISTANCE_ERROR = Metric('Distance', True)


def test_contexts():
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

    rootGoal = Goal(Decomposition.AND, "rootGoal")
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

    notifyCentralBySMSTask = Task("notifyCentralBySMS")
    notifyCentralByInternetTask = Task("notifyCentralByInternet")
    acceptEmergencyTask = Task("acceptEmergency")
    confirmEmergencyByCallTask = Task("confirmEmergencyByCall")
    processDataFromSensorsTask = Task("processDataFromSensors")
    identifySituationTask = Task("identifySituationTask")
    collectDataFromSensorsTask = Task("collectDataFromSensorsTask")
    persistDataToDatabaseTask = Task("persistDataToDatabaseTask")
    notifyByMobileVibrationTask = Task("notifyByMobileVibrationTask")
    notifyBySoundAlertTask = Task("notifyBySoundAlert")
    notifyByLightAlertTask = Task("notifyByLightAlert")
    centralCallTask = Task("centralCallsP")
    sendInfoBySMSTask = Task("sendInfoBySMS")
    sendInfoByInternetTask = Task("sendInfoByInternet")
    considerLastKnownLocationTask = Task("considerLastKnownLocation")
    identifyLocationByVoiceCallTask = Task("identifyLocationByVoiceCall")
    accessLocationFromTriangulationTask = Task(
        "accessLocationFromTriangulation")
    accessLocationFromGPSTask = Task("accessLocationFromGPS")
    accessDataFromDatabaseTask = Task("accessDataFromDatabase")
    getInfoFromResponsibleTask = Task("getInfoFromResponsible")
    ambulanceDispatchDelegation = Task("ambulanceDispatchDelegation")

    rootGoal = respondToEmergencyGoal

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
        ambulanceDispatchDelegation)

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
        ambulanceDispatchDelegation)

    qc1 = QualityConstraint(None, MpersMetrics.TIME,
                            180, Comparison.LESS_THAN)
    qc2 = QualityConstraint(
        c10, MpersMetrics.TIME, 90, Comparison.LESS_THAN)
    qc3 = QualityConstraint(c9, MpersMetrics.TIME,
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

    qc1 = QualityConstraint(None, MpersMetrics.TIME, 60, Comparison.LESS_THAN)
    centralReceivesInfoGoal.interp.addQualityConstraint(qc1)

    qc4 = QualityConstraint(None, MpersMetrics.DISTANCE_ERROR,
                            1000, Comparison.LESS_THAN)
    qc6 = QualityConstraint(
        c5, MpersMetrics.DISTANCE_ERROR, 20, Comparison.LESS_THAN)
    qc5 = QualityConstraint(
        c10, MpersMetrics.DISTANCE_ERROR, 200, Comparison.LESS_THAN)
    qc1 = QualityConstraint(None, MpersMetrics.TIME,
                            120, Comparison.LESS_THAN)
    qc3 = QualityConstraint(c9, MpersMetrics.TIME, 240, Comparison.LESS_THAN)
    qc2 = QualityConstraint(c10, MpersMetrics.TIME, 20, Comparison.LESS_THAN)
    locationIsIdentifiedGoal.interp.addQualityConstraint(qc1)
    locationIsIdentifiedGoal.interp.addQualityConstraint(qc2)
    locationIsIdentifiedGoal.interp.addQualityConstraint(qc3)
    locationIsIdentifiedGoal.interp.addQualityConstraint(qc4)
    locationIsIdentifiedGoal.interp.addQualityConstraint(qc5)
    locationIsIdentifiedGoal.interp.addQualityConstraint(qc6)

    qc1 = QualityConstraint(None, MpersMetrics.TIME, 900, Comparison.LESS_THAN)
    qc2 = QualityConstraint(c10, MpersMetrics.TIME,
                            600, Comparison.LESS_THAN)
    infoIsPreparedGoal.interp.addQualityConstraint(qc1)
    infoIsPreparedGoal.interp.addQualityConstraint(qc2)
    qc1 = QualityConstraint(None, MpersMetrics.NOISE, 10, Comparison.LESS_THAN)
    qc2 = QualityConstraint(c1, MpersMetrics.NOISE, 3, Comparison.LESS_THAN)
    isNotifiedAboutEmergencyGoal.interp.addQualityConstraint(qc1)
    isNotifiedAboutEmergencyGoal.interp.addQualityConstraint(qc2)

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
        None, MpersMetrics.TIME, 120)
    collectDataFromSensorsTask.setProvidedQuality(
        c3, MpersMetrics.TIME, 60)

    persistDataToDatabaseTask.setProvidedQuality(
        None, MpersMetrics.TIME, 5)

    identifySituationTask.setProvidedQuality(
        None, MpersMetrics.FALSE_NEGATIVE_PERCENTAGE, 20)

    notifyByMobileVibrationTask.setProvidedQuality(
        None, MpersMetrics.NOISE, 2)
    notifyBySoundAlertTask.setProvidedQuality(None, MpersMetrics.NOISE, 9)
    notifyByLightAlertTask.setProvidedQuality(None, MpersMetrics.NOISE, 0)
    centralCallTask.setProvidedQuality(None, MpersMetrics.NOISE, 7)

    sendInfoBySMSTask.setProvidedQuality(None, MpersMetrics.TIME, 65)
    sendInfoBySMSTask.setProvidedQuality(c8, MpersMetrics.TIME, 45)

    sendInfoByInternetTask.setProvidedQuality(None, MpersMetrics.TIME, 40)

    considerLastKnownLocationTask.setProvidedQuality(
        None, MpersMetrics.DISTANCE_ERROR, 900)
    considerLastKnownLocationTask.setProvidedQuality(
        None, MpersMetrics.TIME, 15)

    identifyLocationByVoiceCallTask.setProvidedQuality(
        None, MpersMetrics.DISTANCE_ERROR, 100)
    identifyLocationByVoiceCallTask.setProvidedQuality(
        c11, MpersMetrics.DISTANCE_ERROR, 300)
    identifyLocationByVoiceCallTask.setProvidedQuality(
        None, MpersMetrics.TIME, 45)

    accessLocationFromTriangulationTask.setProvidedQuality(
        None, MpersMetrics.DISTANCE_ERROR, 40)
    accessLocationFromTriangulationTask.setProvidedQuality(
        c11, MpersMetrics.DISTANCE_ERROR, 400)
    accessLocationFromTriangulationTask.setProvidedQuality(
        None, MpersMetrics.TIME, 30)

    accessLocationFromGPSTask.setProvidedQuality(
        None, MpersMetrics.DISTANCE_ERROR, 20)
    accessLocationFromGPSTask.setProvidedQuality(
        c11, MpersMetrics.DISTANCE_ERROR, 30)
    accessLocationFromGPSTask.setProvidedQuality(
        None, MpersMetrics.TIME, 50)

    accessDataFromDatabaseTask.setProvidedQuality(
        None, MpersMetrics.TIME, 20)

    getInfoFromResponsibleTask.setProvidedQuality(
        None, MpersMetrics.TIME, 25)
    getInfoFromResponsibleTask.setProvidedQuality(
        c11, MpersMetrics.TIME, 50)

    ambulanceDispatchDelegation.setProvidedQuality(
        None, MpersMetrics.TIME, 30)

    generator = ContextGenerator(
        [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12])
    generatorIter = iter(generator)

    counter = 0

    for context in generatorIter:
        counter = counter + 1
        if rootGoal.isAchievable(context, None) is not None:
            print("Achievable")
            print("[")
            for task in rootGoal.isAchievable(context, None):
                print(task.identifier + " ")

            print("]")
        else:
            print("Not achievable")

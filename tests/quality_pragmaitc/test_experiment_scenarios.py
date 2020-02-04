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


class MpersMetrics:
    FALSE_NEGATIVE_PERCENTAGE = Metric("False Negative", True)
    NOISE = Metric('Noise', True)
    TIME = Metric('Time', True)
    ERROR = Metric('Error', True)
    DISTANCE_ERROR = Metric('Distance', True)


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

# Tasks
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
    ambulanceDispatchDelegation)

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

rootGoal = Goal(Decomposition.AND, "rootGoal")
rootGoal = respondToEmergencyGoal


def createFullContext(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12):
    fullContext = []

    print("Contexto: [")
    if (t1 == 1):
        fullContext.append(c1)
        print("c1")
    if (t2 == 1):
        fullContext.append(c2)
        print("c2")
    if (t3 == 1):
        fullContext.append(c3)
        print("c3")
    if (t4 == 1):
        fullContext.append(c4)
        print("c4")
    if (t5 == 1):
        fullContext.append(c5)
        print("c5")
    if (t6 == 1):
        fullContext.append(c6)
        print("c6")
    if (t7 == 1):
        fullContext.append(c7)
        print("c7")
    if (t8 == 1):
        fullContext.append(c8)
        print("c8")
    if (t9 == 1):
        fullContext.append(c9)
        print("c9")
    if (t10 == 1):
        fullContext.append(c10)
        print("c10")
    if (t11 == 1):
        fullContext.append(c11)
        print("c11")
    if (t12 == 1):
        fullContext.append(c12)
        print("c12")

    print("]")
    return fullContext


def test_MPEARS():

    generator = ContextGenerator(
        [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12])
    generatorIter = iter(generator)

    counter = 0

    for context in generatorIter:
        counter = counter + 1
        print("INIT IN TEST FOR CONTEXT: ", counter)
        print_context(context)
        if rootGoal.isAchievable(context, None) is not None:
            print("Achievable")
            print("[")
            for task in rootGoal.isAchievable(context, None).getTasks():
                print(task.identifier + " ")

            print("]")
        else:
            print("Not achievable")

        print("END: ", counter)


def test_C1():
    print("=========== Test C1 ================")
    fullContext = createFullContext(1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1)
    tasks = rootGoal.isAchievable(fullContext, None)

    assert tasks is not None

    for task in rootGoal.isAchievable(fullContext, None).getTasks():
        found = 0

        if task.getIdentifier() is "accessLocationFromGPS":
            found = 1
        if task.getIdentifier() is "centralCallsP":
            found = 1

        assert found == 0

def test_C2():
    print("=========== Test C2 ================")
    fullContext = createFullContext(1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1)
    tasks = rootGoal.isAchievable(fullContext, None)

    assert tasks is not None

    for task in rootGoal.isAchievable(fullContext, None).getTasks():
        found = 0

        if task.getIdentifier() is "acceptEmergency":
            found = 1
        if task.getIdentifier() is "notifyBySoundAlert":
            found = 1

        assert found == 0        

def test_C3():
    print("=========== Test C3 ================")
    fullContext = createFullContext(1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0)
    tasks = rootGoal.isAchievable(fullContext, None)

    assert tasks is not None

    for task in rootGoal.isAchievable(fullContext, None).getTasks():
        found = 0

        if task.getIdentifier() is "acceptEmergency":
            found = 1

        assert found == 0        

def test_C4():
    print("=========== Test C4 ================")
    fullContext = createFullContext(1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1)
    tasks = rootGoal.isAchievable(fullContext, None)

    assert tasks is not None

    for task in rootGoal.isAchievable(fullContext, None).getTasks():
        found = 0

        if task.getIdentifier() is "notifyCentralBySMS":
            found = 1
        if task.getIdentifier() is "confirmEmergencyByCall":
            found = 1
        if task.getIdentifier() is "notifyBySoundAlert":
            found = 1
        if task.getIdentifier() is "sendInfoBySMS":
            found = 1
        if task.getIdentifier() is "identifyLocationByVoiceCall":
            found = 1
        if task.getIdentifier() is "accessLocationFromTriangulation":
            found = 1
        
        assert found == 0        

def test_C5():
    print("=========== Test C5 ================")
    fullContext = createFullContext(1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1)
    tasks = rootGoal.isAchievable(fullContext, None)

    assert tasks is not None

    for task in rootGoal.isAchievable(fullContext, None).getTasks():
        found = 0

        if task.getIdentifier() is "notifyCentralBySMS":
            found = 1
        if task.getIdentifier() is "notifyBySoundAlert":
            found = 1
        if task.getIdentifier() is "sendInfoBySMS":
            found = 1
        if task.getIdentifier() is "confirmEmergencyByCall":
            found = 1
        
        assert found == 0 


def test_C6():
    print("=========== Test C6 ================")
    fullContext = createFullContext(1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1)
    tasks = rootGoal.isAchievable(fullContext, None)

    assert tasks is not None

    for task in rootGoal.isAchievable(fullContext, None).getTasks():
        found = 0

        if task.getIdentifier() is "notifyCentralBySMS":
            found = 1
        if task.getIdentifier() is "sendInfoBySMS":
            found = 1
        if task.getIdentifier() is "confirmEmergencyByCall":
            found = 1
        
        assert found == 0 

def test_C7():
    print("=========== Test C7 ================")
    fullContext = createFullContext(1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1)
    tasks = rootGoal.isAchievable(fullContext, None)

    assert tasks is not None

    for task in rootGoal.isAchievable(fullContext, None).getTasks():
        found = 0

        if task.getIdentifier() is "notifyCentralBySMS":
            found = 1
        if task.getIdentifier() is "confirmEmergencyByCall":
            found = 1
        if task.getIdentifier() is "notifyBySoundAlert":
            found = 1
        if task.getIdentifier() is "sendInfoBySMS":
            found = 1
        if task.getIdentifier() is "identifyLocationByVoiceCall":
            found = 1
        if task.getIdentifier() is "accessLocationFromTriangulation":
            found = 1
        if task.getIdentifier() is "accessLocationFromGPS":
            found = 1
        
        assert found == 0


def test_C8():
    print("=========== Test C8 ================")
    fullContext = createFullContext(1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1)
    tasks = rootGoal.isAchievable(fullContext, None)

    assert tasks is not None

    for task in rootGoal.isAchievable(fullContext, None).getTasks():
        found = 0

        if task.getIdentifier() is "notifyCentralBySMS":
            found = 1
        if task.getIdentifier() is "confirmEmergencyByCall":
            found = 1
        if task.getIdentifier() is "notifyBySoundAlert":
            found = 1
        if task.getIdentifier() is "sendInfoBySMS":
            found = 1
        if task.getIdentifier() is "identifyLocationByVoiceCall":
            found = 1
        if task.getIdentifier() is "accessLocationFromTriangulation":
            found = 1
        
        assert found == 0

    
def test_C9():
    print("=========== Test C9 ================")
    fullContext = createFullContext(1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0)
    tasks = rootGoal.isAchievable(fullContext, None)

    assert tasks is not None

    for task in rootGoal.isAchievable(fullContext, None).getTasks():
        found = 0

        if task.getIdentifier() is "notifyByLightAlert":
            found = 1
        if task.getIdentifier() is "acceptsEmergency":
            found = 1
        
        assert found == 0


def test_C10():
    print("=========== Test C10 ================")
    fullContext = createFullContext(1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1)
    tasks = rootGoal.isAchievable(fullContext, None)

    assert tasks is not None

    for task in rootGoal.isAchievable(fullContext, None).getTasks():
        found = 0

        if task.getIdentifier() is "notifyByLightAlert":
            found = 1
        if task.getIdentifier() is "acceptEmergency":
            found = 1
        
        assert found == 0


def test_C11():
    print("=========== Test C11 ================")
    fullContext = createFullContext(1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1)
    tasks = rootGoal.isAchievable(fullContext, None)

    assert tasks is not None

    for task in rootGoal.isAchievable(fullContext, None).getTasks():
        found = 0

        if task.getIdentifier() is "notifyCentralBySMS":
            found = 1
        if task.getIdentifier() is "confirmEmergencyByCall":
            found = 1
        if task.getIdentifier() is "notifyByLightAlert":
            found = 1
        if task.getIdentifier() is "sendInfoBySMS":
            found = 1
        
        assert found == 0


def test_C12():
    print("=========== Test C12 ================")
    fullContext = createFullContext(1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1)
    tasks = rootGoal.isAchievable(fullContext, None)

    assert tasks is not None

    for task in rootGoal.isAchievable(fullContext, None).getTasks():
        found = 0

        if task.getIdentifier() is "notifyCentralBySMS":
            found = 1
        if task.getIdentifier() is "confirmEmergencyByCall":
            found = 1
        if task.getIdentifier() is "sendInfoBySMS":
            found = 1
        
        assert found == 0


def test_All():
    print("=========== Test ALL ================")
    fullContext = createFullContext(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    tasks = rootGoal.isAchievable(fullContext, None)

    assert tasks is not None

    for task in rootGoal.isAchievable(fullContext, None).getTasks():
        found = 0

        if task.getIdentifier() is "acceptEmergency":
            found = 1

        assert found == 0


def test_None():
    print("=========== Test None ================")
    fullContext = createFullContext(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    tasks = rootGoal.isAchievable(fullContext, None)

    assert tasks is None



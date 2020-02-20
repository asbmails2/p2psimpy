from goald.utils.context_generator import ContextGenerator
from goald.utils.print import print_context
from tests.utils.assert_util import assertPlan
from tests.test_data.mpers_model import MpersModel

import pytest


@pytest.fixture
def mpers():
    mpers = MpersModel()

    return mpers


def test_MPEARS(mpers):
    generator = ContextGenerator(
        [mpers.contexts.c1,
         mpers.contexts.c2,
         mpers.contexts.c3,
         mpers.contexts.c4,
         mpers.contexts.c5,
         mpers.contexts.c6,
         mpers.contexts.c7,
         mpers.contexts.c8,
         mpers.contexts.c9,
         mpers.contexts.c10,
         mpers.contexts.c12])

    generatorIter = iter(generator)

    counter = 0

    for context in generatorIter:
        counter = counter + 1
        print("INIT IN TEST FOR CONTEXT: ", counter)
        print_context(context)
        if mpers.rootGoal.isAchievable(context, None) is not None:
            print("Achievable")
            print("[")
            for task in mpers.rootGoal.isAchievable(context, None).getTasks():
                print(task.identifier + " ")

            print("]")
        else:
            print("Not achievable")

        print("END: ", counter)


def test_ContextSet1(mpers):
    fullContext = [mpers.contexts.c1,
                   mpers.contexts.c2,
                   mpers.contexts.c3,
                   mpers.contexts.c4,
                   mpers.contexts.c5,
                   mpers.contexts.c6,
                   mpers.contexts.c7,
                   mpers.contexts.c8,
                   mpers.contexts.c9,
                   mpers.contexts.c10]

    plan = mpers.rootGoal.isAchievable(fullContext, None)

    assert assertPlan(
        plan,
        [mpers.tasks.ambulanceDispatchDelegationTask,
         mpers.tasks.notifyCentralByInternetTask,
         mpers.tasks.confirmEmergencyByCallTask,
         mpers.tasks.getInfoFromResponsibleTask,
         mpers.tasks.notifyByLightAlertTask,
         mpers.tasks.sendInfoByInternetTask])


def test_contextSet1_not_found(mpers):
    fullContext = [mpers.contexts.c1,
                   mpers.contexts.c2,
                   mpers.contexts.c3,
                   mpers.contexts.c4,
                   mpers.contexts.c5,
                   mpers.contexts.c6,
                   mpers.contexts.c7,
                   mpers.contexts.c8,
                   mpers.contexts.c9,
                   mpers.contexts.c10]

    plan = mpers.rootGoal.isAchievable(fullContext, None)

    assert plan is not None

    for task in plan.getTasks():
        found = 0
        if task is mpers.tasks.acceptEmergencyTask:
            found = 1
        if task.identifier is mpers.tasks.notifyCentralBySMSTask:
            found = 1
        if task.identifier is mpers.tasks.notifyBySoundAlertTask:
            found = 1
        if task.identifier is mpers.tasks.identifyLocationByVoiceCallTask:
            found = 1
        if task.identifier is mpers.tasks.accessLocationFromTriangulationTask:
            found = 1
        if task.identifier is mpers.tasks.accessLocationFromGPSTask:
            found = 1
        if task.identifier is mpers.tasks.considerLastKnownLocationTask:
            found = 1

        assert found == 0


def test_ContextSet2(mpers):
    fullContext = [mpers.contexts.c9,
                   mpers.contexts.c10,
                   mpers.contexts.c11]

    plan = mpers.rootGoal.isAchievable(fullContext, None)

    assert assertPlan(plan, None)


def test_ContextSet3(mpers):
    fullContext = [mpers.contexts.c4, mpers.contexts.c8, mpers.contexts.c11]

    plan = mpers.rootGoal.isAchievable(fullContext, None)

    assert assertPlan(
        plan,
        [mpers.tasks.ambulanceDispatchDelegationTask,
         mpers.tasks.acceptEmergencyTask,
         mpers.tasks.centralCallTask,
         mpers.tasks.considerLastKnownLocationTask,
         mpers.tasks.accessDataFromDatabaseTask,
         mpers.tasks.sendInfoByInternetTask,
         mpers.tasks.notifyCentralByInternetTask])


def test_contextSet3_not_found(mpers):
    fullContext = [mpers.contexts.c4, mpers.contexts.c8, mpers.contexts.c11]

    plan = mpers.rootGoal.isAchievable(fullContext, None)

    assert plan is not None

    for task in plan.getTasks():
        found = 0
        # if task is mpers.tasks.acceptEmergencyTask:
        #     found = 1
        if task.identifier is mpers.tasks.confirmEmergencyByCallTask:
            found = 1
        if task.identifier is mpers.tasks.notifyCentralBySMSTask:
            found = 1
        if task.identifier is mpers.tasks.getInfoFromResponsibleTask:
            found = 1
        if task.identifier is mpers.tasks.notifyBySoundAlertTask:
            found = 1
        if task.identifier is mpers.tasks.notifyByLightAlertTask:
            found = 1
        if task.identifier is mpers.tasks.notifyByMobileVibrationTask:
            found = 1
        if task.identifier is mpers.tasks.sendInfoBySMSTask:
            found = 1

        assert found == 0

def test_ContextSet4(mpers):
    fullContext = [mpers.contexts.c1,
                   mpers.contexts.c2,
                   mpers.contexts.c3,
                   mpers.contexts.c6,
                   mpers.contexts.c7]

    plan = mpers.rootGoal.isAchievable(fullContext, None)

    assert assertPlan(
        plan,
        [mpers.tasks.notifyCentralBySMSTask,
         mpers.tasks.notifyByLightAlertTask,
         mpers.tasks.getInfoFromResponsibleTask,
         mpers.tasks.sendInfoByInternetTask,
         mpers.tasks.confirmEmergencyByCallTask,
         mpers.tasks.ambulanceDispatchDelegationTask])


def test_contextSet4_not_found(mpers):
    fullContext = [mpers.contexts.c1,
                   mpers.contexts.c2,
                   mpers.contexts.c3,
                   mpers.contexts.c6,
                   mpers.contexts.c7]

    plan = mpers.rootGoal.isAchievable(fullContext, None)

    assert plan is not None

    for task in plan.getTasks():
        found = 0
        
        if task.identifier is mpers.tasks.acceptEmergencyTask:
            found = 1
        if task.identifier is mpers.tasks.centralCallTask:
            found = 1
        if task.identifier is mpers.tasks.accessLocationFromGPSTask:
            found = 1

        assert found == 0
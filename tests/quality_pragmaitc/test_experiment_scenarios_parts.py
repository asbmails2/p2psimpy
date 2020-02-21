from tests.utils.assert_util import assertPlan
from tests.test_data.mpers_model import MpersModel

import pytest


@pytest.fixture
def mpers():
    mpers = MpersModel()

    return mpers


def test_ContextSet1_emergencyIsDetected(mpers):
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

    plan = mpers.goals.emergencyIsDetectedGoal.isAchievable(fullContext, None)

    assert assertPlan(
        plan,
        [mpers.tasks.notifyCentralByInternetTask,
         mpers.tasks.confirmEmergencyByCallTask])


def test_ContextSet1_isNotifiedAboutEmergencyGoal(mpers):
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

    plan = mpers.goals.isNotifiedAboutEmergencyGoal.isAchievable(
        fullContext, None)

    assert assertPlan(
        plan,
        [mpers.tasks.notifyByLightAlertTask])


def test_ContextSet1_centralReceivesInfoGoal(mpers):
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

    plan = mpers.goals.centralReceivesInfoGoal.isAchievable(fullContext, None)

    assert assertPlan(
        plan,
        [mpers.tasks.getInfoFromResponsibleTask,
         mpers.tasks.sendInfoByInternetTask])


def test_ContextSet1_medicalCareReachesGoal(mpers):
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

    plan = mpers.goals.medicalCareReachesGoal.isAchievable(fullContext, None)

    assert assertPlan(
        plan,
        [mpers.tasks.ambulanceDispatchDelegationTask])


def test_ContextSet3_emergencyIsDetectedGoal(mpers):
    fullContext = [mpers.contexts.c4,
                   mpers.contexts.c8,
                   mpers.contexts.c11]

    plan = mpers.goals.emergencyIsDetectedGoal.isAchievable(fullContext, None)

    assert assertPlan(
        plan,
        [mpers.tasks.notifyCentralByInternetTask,
         mpers.tasks.acceptEmergencyTask])


def test_ContextSet3_isNotifiedAboutEmergencyGoal(mpers):
    fullContext = [mpers.contexts.c4,
                   mpers.contexts.c8,
                   mpers.contexts.c11]

    plan = mpers.goals.isNotifiedAboutEmergencyGoal.isAchievable(
        fullContext, None)

    assert assertPlan(
        plan,
        [mpers.tasks.centralCallTask])


def test_ContextSet3_centralReceivesInfoGoal(mpers):
    fullContext = [mpers.contexts.c4,
                   mpers.contexts.c8,
                   mpers.contexts.c11]

    plan = mpers.goals.centralReceivesInfoGoal.isAchievable(fullContext, None)

    assert assertPlan(
        plan,
        [mpers.tasks.considerLastKnownLocationTask,
         mpers.tasks.accessDataFromDatabaseTask,
         mpers.tasks.sendInfoByInternetTask])


def test_ContextSet1_medicalCareReachesGoal(mpers):
    fullContext = [mpers.contexts.c4,
                   mpers.contexts.c8,
                   mpers.contexts.c11]

    plan = mpers.goals.medicalCareReachesGoal.isAchievable(fullContext, None)

    assert assertPlan(
        plan,
        [mpers.tasks.ambulanceDispatchDelegationTask])


def test_ContextSet4_emergencyIsDetectedGoal(mpers):
    fullContext = [mpers.contexts.c1,
                   mpers.contexts.c2,
                   mpers.contexts.c3,
                   mpers.contexts.c6,
                   mpers.contexts.c7]

    plan = mpers.goals.emergencyIsDetectedGoal.isAchievable(fullContext, None)

    assert assertPlan(
        plan,
        [mpers.tasks.notifyCentralBySMSTask,
         mpers.tasks.confirmEmergencyByCallTask])


def test_ContextSet4_isNotifiedAboutEmergencyGoal(mpers):
    fullContext = [mpers.contexts.c1,
                   mpers.contexts.c2,
                   mpers.contexts.c3,
                   mpers.contexts.c6,
                   mpers.contexts.c7]

    plan = mpers.goals.isNotifiedAboutEmergencyGoal.isAchievable(
        fullContext, None)

    assert assertPlan(
        plan,
        [mpers.tasks.notifyByLightAlertTask])


def test_ContextSet4_centralReceivesInfoGoal(mpers):
    fullContext = [mpers.contexts.c1,
                   mpers.contexts.c2,
                   mpers.contexts.c3,
                   mpers.contexts.c6,
                   mpers.contexts.c7]

    plan = mpers.goals.centralReceivesInfoGoal.isAchievable(fullContext, None)

    assert assertPlan(
        plan,
        [mpers.tasks.accessLocationFromTriangulationTask,
         mpers.tasks.accessDataFromDatabaseTask,
         mpers.tasks.sendInfoByInternetTask])


def test_ContextSet4_medicalCareReachesGoal(mpers):
    fullContext = [mpers.contexts.c1,
                   mpers.contexts.c2,
                   mpers.contexts.c3,
                   mpers.contexts.c6,
                   mpers.contexts.c7]

    plan = mpers.goals.medicalCareReachesGoal.isAchievable(fullContext, None)

    assert assertPlan(
        plan,
        [mpers.tasks.ambulanceDispatchDelegationTask])

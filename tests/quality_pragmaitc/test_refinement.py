from goald.quality.pragmatic.model.refinement import Refinement
from goald.quality.pragmatic.model.task import Task
from goald.quality.pragmatic.model.delegation import Delegation
from goald.quality.pragmatic.model.context import Context
from goald.quality.pragmatic.model.common_metrics import CommonMetrics
from goald.quality.pragmatic.model.goal import Goal
from goald.quality.pragmatic.model.interpretation import Interpretation
from goald.quality.pragmatic.model.quality_constraint import QualityConstraint
from goald.quality.pragmatic.model.comparison import Comparison


def test_refinement():
    refinement = Refinement()
    task = Task()
    delegation = Delegation()
    goal = Goal()

    assert task.myType() is refinement.TASK
    assert delegation.myType() is refinement.DELEGATION
    assert goal.myType() is refinement.GOAL


def test_shouldBeApplicable():
    goal = Goal()
    task = Task()
    delegation = Delegation()

    contextCurrent = Context("C1")
    fullContext = []

    fullContext.append(contextCurrent)

    goal.addApplicableContext(contextCurrent)
    task.addApplicableContext(contextCurrent)
    delegation.addApplicableContext(contextCurrent)

    assert True is goal.isApplicable(fullContext)
    assert True is task.isApplicable(fullContext)
    assert True is delegation.isApplicable(fullContext)


def test_shouldBeNotApplicable():
    goal = Goal()
    task = Task()
    delegation = Delegation()

    context = Context("C1")

    task.addApplicableContext(context)

    goal.addApplicableContext(context)

    delegation.addApplicableContext(context)

    wrongContext = Context("C2")
    fullContext = []
    fullContext.append(wrongContext)

    assert False is goal.isApplicable(fullContext)
    assert False is task.isApplicable(fullContext)
    assert False is delegation.isApplicable(fullContext)


def test_aTaskShouldBeAchievable():
    task = Task()

    currentContext = Context("C1")
    fullContext = []
    fullContext.append(currentContext)

    qc = QualityConstraint(
        currentContext, CommonMetrics.SECONDS, 15, 'LESS_OR_EQUAL_TO')

    task.addApplicableContext(currentContext)
    task.setProvidedQuality(currentContext, CommonMetrics.SECONDS, 12)

    interp = Interpretation()
    interp.addQualityConstraint(qc)

    assert True is task in task.isAchievable(
        fullContext, interp).getTasks()


def test_shouldAddSeveralContextsAtOnce():
    context1 = Context("C1")
    context2 = Context("C2")

    task = Task()
    originalSize = len(task.getApplicableContext())
    set = []

    set.append(context1)
    set.append(context2)

    task.addApplicableContext(set)

    assert 2 == len(task.getApplicableContext()) - originalSize


def aNonApplicableRootGoalIsNotAchievable():
    goal = Goal(False)
    current = Context("C1")
    fullContext = []

    qc = QualityConstraint(current, CommonMetrics.SECONDS,
                           15, Comparison.LESS_OR_EQUAL_TO)
    goal.addApplicableContext(Context("C2"))

    interp = Interpretation()
    interp.addQualityConstraint(qc)

    assert goal.isAchievable(fullContext, interp) is None


def aGoalWithATaskMayBeAchievable():
    goal = Goal(False)

    task = Task()

    current = Context("C1")
    fullContext = []
    fullContext.append(current)

    qc = QualityConstraint(current, CommonMetrics.SECONDS,
                           15, Comparison.LESS_OR_EQUAL_TO)
    interp = Interpretation()
    interp.addQualityConstraint(qc)

    task.addApplicableContext(current)
    task.setProvidedQuality(current, CommonMetrics.SECONDS, 13)

    goal.addDependency(task)
    #goal.setIdentifier("Root")
    goal.addApplicableContext(current)

    plan = goal.isAchievable(fullContext, interp)
    assert len(plan.getTasks()) == 1

from goald.quality.pragmatic.model.refinement import Refinement
from goald.quality.pragmatic.model.task import Task
from goald.quality.pragmatic.model.delegation import Delegation
from goald.quality.pragmatic.model.context import Context
from goald.quality.pragmatic.model.common_metrics import CommonMetrics
from goald.quality.pragmatic.model.decomposition import Decomposition
from goald.quality.pragmatic.model.goal import Goal
from goald.quality.pragmatic.model.interpretation import Interpretation
from goald.quality.pragmatic.model.quality_constraint import QualityConstraint
from goald.quality.pragmatic.model.comparison import Comparison
from goald.quality.pragmatic.model.pragmatic import Pragmatic


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
        currentContext, CommonMetrics.SECONDS, 15, Comparison.LESS_OR_EQUAL_TO)

    task.addApplicableContext(currentContext)
    task.setProvidedQuality(currentContext, CommonMetrics.SECONDS, 12)

    interp = Interpretation()
    interp.addQualityConstraint(qc)

    assert task in task.isAchievable(
        fullContext, interp).getTasks()


def test_shouldAddSeveralContextsAtOnce():
    context1 = Context("C1")
    context2 = Context("C2")

    task = Task()
    originalSize = 0

    if None is task.getApplicableContext():
        originalSize = len(task.getApplicableContext())

    set = []

    set.append(context1)
    set.append(context2)

    task.addApplicableContext(set)

    assert 2 == len(task.getApplicableContext()) - originalSize


def test_aNonApplicableRootGoalIsNotAchievable():
    goal = Goal(False)
    current = Context("C1")
    fullContext = []

    qc = QualityConstraint(current, CommonMetrics.SECONDS,
                           15, Comparison.LESS_OR_EQUAL_TO)
    goal.addApplicableContext(Context("C2"))

    interp = Interpretation()
    interp.addQualityConstraint(qc)

    assert goal.isAchievable(fullContext, interp) is None


def test_aGoalWithATaskMayBeAchievable():
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
    goal.setIdentifier("Root")
    goal.addApplicableContext(current)

    plan = goal.isAchievable(fullContext, interp)
    assert len(plan.getTasks()) == 1


def test_aGoalAndDecomposedWithTwoTasksMayBeAchievable():
    goal = Goal(Decomposition.AND)
    assert not goal.isOrDecomposition

    task1 = Task()
    task2 = Task()

    current = Context("C1")
    fullContext = []
    fullContext.append(current)

    qc = QualityConstraint(current, CommonMetrics.SECONDS,
                           15, Comparison.LESS_OR_EQUAL_TO)

    task1.addApplicableContext(current)
    task1.setProvidedQuality(current, CommonMetrics.SECONDS, 13)

    task2.addApplicableContext(current)
    task2.setProvidedQuality(current, CommonMetrics.SECONDS, 11)

    goal.addDependency(task1)
    goal.addDependency(task2)

    goal.setIdentifier("Root")
    goal.addApplicableContext(current)

    interp = Interpretation()
    interp.addQualityConstraint(qc)

    plan = goal.isAchievable(fullContext, interp)
    assert 2 == len(plan.getTasks())


def test_aGoalAndDecomposedWithTwoTasksMayNotBeAchievable():
    goal = Goal(Decomposition.AND)

    assert not goal.decomposition

    task1 = Task()
    task2 = Task()

    current = Context("C1")
    fullContext = []
    fullContext.append(current)

    qc = QualityConstraint(current, CommonMetrics.SECONDS,
                           15, Comparison.LESS_OR_EQUAL_TO)

    task1.addApplicableContext(current)
    task1.setProvidedQuality(current, CommonMetrics.SECONDS, 16)

    task2.addApplicableContext(current)
    task2.setProvidedQuality(current, CommonMetrics.SECONDS, 11)

    goal.addDependency(task1)
    goal.addDependency(task2)

    goal.setIdentifier("Root")
    goal.addApplicableContext(current)

    interp = Interpretation()
    interp.addQualityConstraint(qc)

    plan = goal.isAchievable(fullContext, interp)

    assert plan is None


def test_aGoalOrDecomposedWithTwoTasksMayBeAchievable():
    goal = Goal(Decomposition.OR)
    assert goal.decomposition

    task1 = Task()
    task2 = Task()

    current = Context("C1")
    fullContext = []
    fullContext.append(current)

    qc = QualityConstraint(current, CommonMetrics.SECONDS,
                           15, Comparison.LESS_OR_EQUAL_TO)

    task1.addApplicableContext(current)
    task1.setProvidedQuality(current, CommonMetrics.SECONDS, 13)

    task2.addApplicableContext(current)
    task2.setProvidedQuality(current, CommonMetrics.SECONDS, 11)

    goal.addDependency(task1)
    goal.addDependency(task2)

    goal.setIdentifier("Root")
    goal.addApplicableContext(current)

    interp = Interpretation()
    interp.addQualityConstraint(qc)

    plan = goal.isAchievable(fullContext, interp)
    assert len(plan.getTasks()) == 1


def test_aGoalOrDecomposedWithTwoTasksMayBeAchievableAtOnlyOneBranch():
    goal = Goal(Decomposition.OR)
    assert goal.decomposition

    task1 = Task()
    task2 = Task()

    current = Context("C1")
    fullContext = []
    fullContext.append(current)

    qc = QualityConstraint(current, CommonMetrics.SECONDS,
                           15, Comparison.LESS_OR_EQUAL_TO)

    task1.addApplicableContext(current)
    task1.setProvidedQuality(current, CommonMetrics.SECONDS, 16)

    task2.addApplicableContext(current)
    task2.setProvidedQuality(current, CommonMetrics.SECONDS, 11)

    goal.addDependency(task1)
    goal.addDependency(task2)

    goal.setIdentifier("Root")
    goal.addApplicableContext(current)

    interp = Interpretation()
    interp.addQualityConstraint(qc)

    plan = goal.isAchievable(fullContext, interp)
    assert plan.getTasks().contains(task2)
    assert plan.getTasks().contains(task1)


def test_aGoalOrDecomposedWithTwoTasksMayNotBeAchievable():
    goal = Goal(Decomposition.OR)

    task1 = Task()
    task2 = Task()
    current = Context("C1")
    fullContext = []
    fullContext.append(current)

    qc = QualityConstraint(current, CommonMetrics.SECONDS,
                           15, Comparison.LESS_OR_EQUAL_TO)

    task1.addApplicableContext(current)
    task1.setProvidedQuality(current, CommonMetrics.SECONDS, 16)

    task2.addApplicableContext(current)
    task2.setProvidedQuality(current, CommonMetrics.SECONDS, 17)

    goal.addDependency(task1)
    goal.addDependency(task2)

    goal.setIdentifier("Root")
    goal.addApplicableContext(current)

    interp = Interpretation()
    interp.addQualityConstraint(qc)

    plan = goal.isAchievable(fullContext, interp)
    assert goal.decomposition
    assert plan is None


def test_ApplicableDeps():
    goal = Pragmatic()

    task = Task()
    context = Context("C1")
    wrongContext = Context("C2")
    current = []

    qc = QualityConstraint(context, CommonMetrics.SECONDS,
                           15, Comparison.LESS_OR_EQUAL_TO)

    task.addApplicableContext(context)
    task.setProvidedQuality(context, CommonMetrics.SECONDS, 13)

    goal.addDependency(task)
    goal.setIdentifier("Root")
    goal.addApplicableContext(context)
    goal.getInterpretation().addQualityConstraint(qc)

    interp = Interpretation()
    interp.addQualityConstraint(qc)

    current.append(wrongContext)
    assert goal.isAchievable(current, interp) is None

    current.append(context)
    assert len(goal.isAchievable(current, interp).getTasks()) == 1


def testGetApplicableQC():
    goal = Pragmatic(Decomposition.AND)

    task = Task()
    context = Context("C1")
    anotherContext = Context("C2")

    fullContext = []

    qc = QualityConstraint(context, CommonMetrics.SECONDS,
                           15, Comparison.LESS_OR_EQUAL_TO)
    stricter = QualityConstraint(
        anotherContext, CommonMetrics.SECONDS, 10, Comparison.LESS_OR_EQUAL_TO)

    goal.addDependency(task)
    goal.setIdentifier("Root")
    goal.addApplicableContext(context)
    goal.getInterpretation().addQualityConstraint(qc)
    goal.getInterpretation().addQualityConstraint(stricter)

    interp = Interpretation()
    interp.addQualityConstraint(qc)

    fullContext.append(context)
    # assertEquals(null, goal.isAchievable(fullContext, interp))

    assert qc in goal.getInterpretation().getQualityConstraints(
        fullContext)

    fullContext.append(anotherContext)
    assert qc in goal.getInterpretation().getQualityConstraints(
        fullContext)
    assert stricter in goal.getInterpretation().getQualityConstraints(
        fullContext)

    fullContext.pop(context)
    assert qc not in goal.getInterpretation().getQualityConstraints(
        fullContext)

    assert stricter in goal.getInterpretation().getQualityConstraints(
        fullContext)


def shouldThereBeMoreThanOneApplicableQCreturnTheStricterOne():
    goal = Pragmatic(Decomposition.AND)

    task = Task()
    context = Context("C1")
    anotherContext = Context("C2")

    fullContext = []

    qc = QualityConstraint(context, CommonMetrics.SECONDS,
                           15, Comparison.LESS_OR_EQUAL_TO)
    stricter = QualityConstraint(
        anotherContext, CommonMetrics.SECONDS, 10, Comparison.LESS_OR_EQUAL_TO)

    goal.addDependency(task)
    goal.setIdentifier("Root")
    goal.addApplicableContext(context)
    goal.getInterpretation().addQualityConstraint(qc)
    goal.getInterpretation().addQualityConstraint(stricter)

    assert stricter == qc.stricterQC(stricter)

    fullContext.append(context)
    assert qc in goal.getInterpretation().getQualityConstraints(fullContext)

    fullContext.append(anotherContext)
    assert stricter in goal.getInterpretation().getQualityConstraints(fullContext)


def shouldIncludeNonApplicableContexts():
    goal = Pragmatic(False)

    task = Task()
    context = Context("C1")
    wrongContext = Context("C2")
    current = []

    qc = QualityConstraint(context, CommonMetrics.SECONDS,
                           15, Comparison.LESS_OR_EQUAL_TO)

    task.addApplicableContext(context)
    task.setProvidedQuality(context, CommonMetrics.SECONDS, 13)

    goal.addDependency(task)
    goal.setIdentifier("Root")
    #goal.addNonApplicableContext(wrongContext)
    goal.getInterpretation().addQualityConstraint(qc)

    interp = Interpretation()
    interp.addQualityConstraint(qc)

    current.append(wrongContext)
    #assert goal.isAchievable(current, interp) is None

    current.append(context)
    assert goal.isAchievable(current, interp) is None

    current.pop(wrongContext)
    assert goal.isAchievable(current, interp) is not None
    assert goal.isAchievable(current, interp).getTasks() is not None
    assert 1 == len(goal.isAchievable(current, interp).getTasks())


def shouldAddSeveralContextsAtOnce():
    context1 = Context("C1")
    context2 = Context("C2")

    task = Task()
    originalSize = len(task.getApplicableContext())
    set = []

    set.append(context1)
    set.append(context2)

    task.addApplicableContext(set)
    # null is always an applicable context
    assert 2 == (len(task.getApplicableContext()) - originalSize)

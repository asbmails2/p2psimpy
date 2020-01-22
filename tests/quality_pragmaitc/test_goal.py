from goald.quality.pragmatic.model.task import Task
from goald.quality.pragmatic.model.goal import Goal
from goald.quality.pragmatic.model.context import Context
from goald.quality.pragmatic.model.delegation import Delegation
from goald.quality.pragmatic.model.decomposition import Decomposition
from goald.quality.pragmatic.model.common_metrics import CommonMetrics
from goald.quality.pragmatic.model.quality_constraint import QualityConstraint
from goald.quality.pragmatic.model.interpretation import Interpretation
from goald.quality.pragmatic.model.comparison import Comparison


def test_shouldBeAchievable():
    root = Goal(Decomposition.AND)

    context = Context("c1")
    current = []
    current.append(context)

    task1 = Task()
    task2 = Task()

    task1.addApplicableContext(context)

    root.addDependency(task1)
    root.addDependency(task2)

    plan = root.isAchievable(current, None)
    assert plan is not None

    assert task2 in plan.getTasks()


def test_shouldGetApplicableDependencies():
    root = Goal(Decomposition.AND)

    context = Context("c1")
    current = []
    current.append(context)

    task = Task()
    goal = Goal(Decomposition.AND)
    delegation = Delegation()

    task.addApplicableContext(context)

    root.addDependency(task)
    root.addDependency(goal)
    root.addDependency(delegation)

    deps = []
    deps.append(task)

    assert 1 == len(deps)
    assert task in deps


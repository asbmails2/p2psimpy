from goald.quality.pragmatic.model.task import Task
from goald.quality.pragmatic.model.goal import Goal
from goald.quality.pragmatic.model.context import Context
from goald.quality.pragmatic.model.refinement import Refinement

def test_shouldBeAchievable():
    root = Goal(False)

    context = Context("c1")
    current = []
    current.append(context)

    task1 = Task()
    task2 = Task()

    task1.addApplicableContext(context)

    root.addDependency(task1)
    root.addDependency(task2)

    deps = []
    deps.append(task1)
    deps.append(task2)

    plan = root.isAchievable(current, None)
    assert plan != None
    
    assert task1 in plan.getTasks()
    assert task2 in plan.getTasks()


from goald.quality.pragmatic.model.plan import Plan
from goald.quality.pragmatic.model.task import Task

def test_plan():
    task1 = Task()
    task2 = Task()
    task3 = Task()

    plan1 = Plan(task1)
    plan2 = Plan(task2)
    plan3 = Plan(task3)
    plan4 = Plan()

    plan1.add(plan2)
    plan2.add(plan1)

    plan3.addTask(task2)
    
    assert set(plan1.getTasks()) == set(plan2.getTasks())
    assert set(plan3.getTasks()) != set(plan2.getTasks())


    

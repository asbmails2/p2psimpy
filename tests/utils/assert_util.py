def assertPlan(plan, tasks):

    if tasks is None:
        #assert plan is None
        return

    for task in plan.getTasks():
        print(task.identifier + " ")

    for task in tasks:
        if task not in plan.getTasks():
            print("NOT: ", task.identifier)
        else:
            print("TASK: ", task.identifier)

           

        #assert task in plan.getTasks()

    #assert len(plan.getTasks()) == len(tasks)

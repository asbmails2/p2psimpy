def assertPlan(plan, tasks):
    
    if tasks is None:
        if plan is None:
            return True
        else:
            return False

    if plan is None:
        return False

    planTasks = plan.getTasks()

    print("======== Tasks ========")

    for a in tasks:
        print(a.identifier)

    print("======== Plan Tasks ========")

    for b in planTasks:
        print(b.identifier)

    success = True

    for task in tasks:
        if task not in planTasks:
            success = False
            print(f"Task {task.identifier} should be in Plan")                
        
    for pTask in planTasks:
        if pTask not in tasks:
            success = False
            print(f"Task {pTask.identifier} should not be in Plan")

    return success

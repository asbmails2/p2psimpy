class Plan:
    def __init__(self):
        self.tasks = []

    def __init__(self, *task):
        self.tasks = []
        if task:
            self.tasks.append(task)

    def add(self, plan):
        for task in plan.getTasks():
            if task not in self.tasks:
                self.tasks.append(task)
    
    def addTask(self, task):
        self.tasks.append(task)

    def getTasks(self):
        return self.tasks

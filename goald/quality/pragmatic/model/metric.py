class Metric():
    def __init__(self, name, lessIsBetter):
        self.name = name
        self.lessIsBetter = lessIsBetter

    def getLessIsBetter(self):
        return self.lessIsBetter
        
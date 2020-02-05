class VE:
    def __init__(self, definition,
                 parentAlt,
                 alternatives,
                 chosenAlternative,
                 isAchievable,
                 satisfy,
                 restrictions):

        self.definition = definition
        self.parentAlt = parentAlt
        self.alternatives = alternatives
        self.chosenAlternative = chosenAlternative
        self.isAchievable = isAchievable
        self.satisfy = satisfy
        self.restrictions = restrictions

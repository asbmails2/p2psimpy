from goald.utils.arrange_generator import ArrangeGenerator


class ContextGenerator(ArrangeGenerator):

    def __init__(self, contexts):
        ArrangeGenerator.__init__(self, len(contexts))
        self.contexts = contexts

    def __next__(self):
        nextValue = ArrangeGenerator.__next__(self)
        arrange = []

        for i in range(0, len(self.contexts)):
            if nextValue[i] == 1:
                arrange.append(self.contexts[i])

        return arrange

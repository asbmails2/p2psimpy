class ArrangeGenerator:

    def __init__(self, arrangeSize):
        self.arrangeSize = arrangeSize
        self.last = 2**arrangeSize

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        tempValue = self.value
        self.value = self.value + 1

        if self.value > self.last:
            raise StopIteration

        arrange = []
        for _ in range(0, self.arrangeSize):
            element = tempValue % 2
            tempValue = tempValue >> 1
            arrange.append(element)

        return arrange

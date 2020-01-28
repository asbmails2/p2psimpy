from goald.utils.arrange_generator import ArrangeGenerator
from goald.utils.context_generator import ContextGenerator
from goald.quality.pragmatic.model.context import Context


def test_arrange_gen():

    generator = ArrangeGenerator(2)
    generatorIter = iter(generator)

    assert [0, 0] == next(generatorIter)


def test_arrange_for():

    generator = ArrangeGenerator(2)
    generatorIter = iter(generator)
    lastContext = None
    numberOfContexts = 0

    for context in generatorIter:
        lastContext = context
        numberOfContexts = numberOfContexts + 1

    assert lastContext == [1, 1]
    assert numberOfContexts == 4


def test_context_gen():
    c1 = Context("c1")
    c2 = Context("c2")

    generator = ContextGenerator([c1, c2])
    generatorIter = iter(generator)

    assert [] == next(generatorIter)

    lastContext = None
    numberOfContexts = 0

    for context in generatorIter:
        lastContext = context
        numberOfContexts = numberOfContexts + 1

    assert lastContext == [c1, c2]
    assert numberOfContexts == 4
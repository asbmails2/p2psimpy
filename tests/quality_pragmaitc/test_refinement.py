from goald.quality.pragmatic.model.refinement import Refinement
from goald.quality.pragmatic.model.task import Task
from goald.quality.pragmatic.model.delegation import Delegation
from goald.quality.pragmatic.model.context import Context
from goald.quality.pragmatic.model.metric import CommonMetrics

def test_refinement():
    refinement = Refinement()
    task = Task()
    delegation = Delegation()
    #goal = Goal()

    assert task.myType() == refinement.TASK
    assert delegation.myType() == refinement.DELEGATION
   #assert goal.myType() == refinement.GOAL

def test_shouldBeApplicable():
    #goal = Goal()
    task = Task()
    delegation = Delegation()

    contextCurrent = Context("C1")
    fullContext = []

    fullContext.append(contextCurrent)

    #goal.addApplicableContext(contextCurrent)
    task.addApplicableContext(contextCurrent)
    delegation.addApplicableContext(contextCurrent)

    #assert True == goal.isApplicable(fullContext)
    assert True == task.isApplicable(fullContext)
    assert True == delegation.isApplicable(fullContext)

    def test_shouldBeNotApplicable():
        #goal = Goal()
        task = Task()
        delegation = Delegation()

        context = Context("C1")

        task.addApplicableContext(context)
        #goal.addApplicableContext(context)
        delegation.addApplicableContext(context)

        wrongContext = Context("C2")
        fullContext = []
        fullContext.add(wrongContext)

        #assert False == goal.isApplicable(fullContext)
        assert False == task.isApplicable(fullContext)
        assert False == delegation.isApplicable(fullContext)

    def test_aTaskShouldBeAchievable():
        commonMetrics = CommonMetrics()
        task = Task()

        currentContext = Context("C1")
        fullContext = []
        fullContext.append(currentContext)

        qc = QualityConstraint(currentContext, commonMetrics.SECONDS, 15, 'LESS_OR_EQUAL_TO')

        task.addApplicableContext(currentContext)
        task.setProvidedQuality(currentContext, commonMetrics.SECONDS, 12)

        interp = Interpretation()
        interp.addQualityConstraint(qc)

        assert True == task in task.isAchievable(fullContext, interp).getTasks()

    def test_shouldAddSeveralContextsAtOnce():
        context1 = Context("C1")
        context2 = Context("C2")

        task = Task()
        originalSize = task.getApplicableContext().len()
        set = []

        set.append(context1)
        set.append(context2)

        task.addApplicableContext(set)

        #null is always an applicable context
        assert 2 == task.getApplicableContext().len() - originalSize
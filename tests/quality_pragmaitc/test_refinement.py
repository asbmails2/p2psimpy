from goald.quality.pragmatic.model.refinement import Refinement
from goald.quality.pragmatic.model.task import Task

def test_refinement():
    task = Task()
    refinement = Refinement()
    assert task.myType() == refinement.TASK


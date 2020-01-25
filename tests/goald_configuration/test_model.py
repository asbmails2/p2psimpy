from goald.config.model.alternative import Alternative
from goald.config.model.component import Component
from goald.config.model.context_change import ContextChange, OP
from goald.config.model.context_conditions import ContextCondition
from goald.config.model.dependency import Dependency
from goald.config.model.deployment import Deployment, Status
from goald.config.model.dependency_modifier import DependencyModifier, Type
from goald.quality.pragmatic.model.goal import Goal


def test_alternative():
    alternative = Alternative()
    assert not alternative.resolved


def test_context_change():
    context_change = ContextChange(op=OP.ADDED,
                                   label='c1',
                                   time=1)
    assert context_change.op == OP.ADDED


def test_context_conditions():
    context_conditions = ContextCondition(
        label='c1')
    assert not context_conditions.label == 'c2'


def test_dependency_modifier():
    dependency_modifier = DependencyModifier(
        type=Type.ONE,
        groupId='group 1')
    assert dependency_modifier.type == Type.ONE


def test_dependency():
    dependency = Dependency(
        identification='001',
        modifierType=Type.ONE,
        modifierGroupId='group 1')
    assert dependency.identification == '001'
    assert dependency.modifier.type == Type.ONE


def test_deployment():
    deployment = Deployment()
    assert deployment.componentStatus == []

    component = Component(bundleUuid='001')

    deployment.add(Status.ACTIVE, component)
    assert not deployment.componentStatus == []


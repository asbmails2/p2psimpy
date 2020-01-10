class DeploymentPlan:
    def __init(self, commands = []):
        self.commands = commands

class DeployOp(Enum):
    INSTALL = 1
    RESOLVE = 2
    UPDATE = 3
    REFRESH = 4
    START = 5
    STOP = 6
    UNINSTALL = 7


class Command:
    def __init__(self, op: DeployOp = DeployOp.INSTALL, bundle, component=None):
        self.op = op
        self.bundle = bundle
        self.component = component

from enum import Enum
from typing import Any

from core.logic_nodes.LogicNode import LogicNode


class IfThenElseLogicNode(LogicNode):
    class D(Enum):
        IF = 0
        THEN = 1
        ELSE = 2

    def execute(self) -> Any:
        pass
        # if_node = self.dependencies.

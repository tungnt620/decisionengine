from typing import Any

from pydot import Node as PydotNode


class LogicNode:
    dot_node: PydotNode
    dependencies: list[Any]

    def __init__(self, dot_node: PydotNode):
        self.dot_node = dot_node

    def add_dependencies(self, dependencies: list[Any]):
        self.dependencies = dependencies

    def execute(self) -> Any:
        pass

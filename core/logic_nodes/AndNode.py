from core.logic_nodes.LogicNode import LogicNode


class AndLogicNode(LogicNode):
    def execute(self) -> bool:
        return self.and_operator(self.dependencies)

    def and_operator(self, dependencies: list[LogicNode]) -> bool:
        if len(dependencies) == 1:
            return dependencies[0].execute()

        return dependencies[0].execute() and self.and_operator(dependencies[1:])

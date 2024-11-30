from core.logic_nodes.LogicNode import LogicNode


class OrLogicNode(LogicNode):
    def execute(self) -> bool:
        return self.or_operator(self.dependencies)

    def or_operator(self, dependencies: list[tuple[str, LogicNode]]) -> bool:
        if len(dependencies) == 1:
            return dependencies[0][1].execute()

        return dependencies[0][1].execute() or self.or_operator(dependencies[1:])

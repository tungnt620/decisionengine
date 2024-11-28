from core.nodes.Node import Node


class AndNode(Node):
    def execute(self) -> bool:
        return self.and_operator(self.dependencies)

    def and_operator(self, dependencies: list[Node]) -> bool:
        if len(dependencies) == 1:
            return dependencies[0].execute()

        return dependencies[0].execute() and self.and_operator(dependencies[1:])

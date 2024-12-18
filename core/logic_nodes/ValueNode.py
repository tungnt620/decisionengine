from typing import Any

from core.logic_nodes.LogicNode import LogicNode


class ValueLogicNode(LogicNode):
    def execute(self) -> Any:
        switcher = {
            "int": int,
            "float": float,
            "str": str,
            "bool": bool
        }
        data_type = switcher.get(self.dot_node.get("data_type"))

        if data_type is bool:
            return data_type(self.dot_node.get("value").lower() == "true")

        return data_type(self.dot_node.get("value"))

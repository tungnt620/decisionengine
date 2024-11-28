from pydot import Node as PydotNode

from core.logic_nodes.AndNode import AndLogicNode
from core.logic_nodes.ValueNode import ValueLogicNode


class TestValueNode:
    def test_int_data_type(self):
        dot_node = PydotNode("test")
        dot_node.set("data_type", "int")
        dot_node.set("value", "1")
        node = ValueLogicNode(dot_node)

        assert node.execute() == 1

    def test_float_data_type(self):
        dot_node = PydotNode("test")
        dot_node.set("data_type", "float")
        dot_node.set("value", "1.0")
        node = ValueLogicNode(dot_node)

        assert node.execute() == 1.0

    def test_str_data_type(self):
        dot_node = PydotNode("test")
        dot_node.set("data_type", "str")
        dot_node.set("value", "test 1")
        node = ValueLogicNode(dot_node)

        assert node.execute() == "test 1"

    def test_bool_data_type(self):
        dot_node = PydotNode("test")
        dot_node.set("data_type", "bool")
        dot_node.set("value", "true")
        node = ValueLogicNode(dot_node)

        assert node.execute() is True
        dot_node.set("value", "false")
        node = ValueLogicNode(dot_node)

        assert node.execute() is False


class TestAndNode:
    def test_one_true_operand(self):
        dot_node = PydotNode("test")
        dot_node.set("data_type", "bool")
        dot_node.set("value", "true")
        value_node = ValueLogicNode(dot_node)

        node = AndLogicNode(PydotNode("test"))
        node.add_dependencies([value_node])

        assert node.execute() is True

    def test_one_false_operand(self):
        dot_node = PydotNode("test")
        dot_node.set("data_type", "bool")
        dot_node.set("value", "false")
        value_node = ValueLogicNode(dot_node)

        node = AndLogicNode(PydotNode("test"))
        node.add_dependencies([value_node])

        assert node.execute() is False

    def test_two_operands(self):
        dot_node1 = PydotNode("test")
        dot_node1.set("data_type", "bool")
        dot_node1.set("value", "true")
        value_node1 = ValueLogicNode(dot_node1)

        dot_node2 = PydotNode("test")
        dot_node2.set("data_type", "bool")
        dot_node2.set("value", "false")
        value_node2 = ValueLogicNode(dot_node2)

        node = AndLogicNode(PydotNode("test"))
        node.add_dependencies([value_node1, value_node2])

        assert node.execute() is False

    def test_three_operands(self):
        dot_node1 = PydotNode("test")
        dot_node1.set("data_type", "bool")
        dot_node1.set("value", "true")
        value_node1 = ValueLogicNode(dot_node1)

        dot_node2 = PydotNode("test")
        dot_node2.set("data_type", "bool")
        dot_node2.set("value", "false")
        value_node2 = ValueLogicNode(dot_node2)

        dot_node3 = PydotNode("test")
        dot_node3.set("data_type", "bool")
        dot_node3.set("value", "false")
        value_node3 = ValueLogicNode(dot_node3)

        node = AndLogicNode(PydotNode("test"))
        node.add_dependencies([value_node1, value_node2, value_node3])

        assert node.execute() is False

    def test_three_true_operands(self):
        dot_node1 = PydotNode("test")
        dot_node1.set("data_type", "bool")
        dot_node1.set("value", "true")
        value_node1 = ValueLogicNode(dot_node1)

        dot_node2 = PydotNode("test")
        dot_node2.set("data_type", "bool")
        dot_node2.set("value", "true")
        value_node2 = ValueLogicNode(dot_node2)

        dot_node3 = PydotNode("test")
        dot_node3.set("data_type", "bool")
        dot_node3.set("value", "true")
        value_node3 = ValueLogicNode(dot_node3)

        node = AndLogicNode(PydotNode("test"))
        node.add_dependencies([value_node1, value_node2, value_node3])

        assert node.execute() is True

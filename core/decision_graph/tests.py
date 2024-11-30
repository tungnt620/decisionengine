import pydot
import pytest

from core.decision_graph.DecisionGraph import DecisionGraph
from core.logic_nodes.AndNode import AndLogicNode
from core.logic_nodes.ValueNode import ValueLogicNode


class TestDecisionGraph:
    def test_one_node(self):
        graph_dot = pydot.graph_from_dot_data(
            """
            digraph {
                str [node_type=ValueNode data_type=str value=hello type=root]
            }
            """
        )

        decision_graph = DecisionGraph(dot_graph=graph_dot[0], node_factory={
            "ValueNode": lambda: ValueLogicNode(None)
        })

        root_node = decision_graph.build()

        assert root_node.execute() == "hello"

    def test_three_nodes(self):
        graph_dot = pydot.graph_from_dot_data(
            """
            digraph {
                operand1 [node_type=ValueNode data_type=bool value=False]
                operand2 [node_type=ValueNode data_type=bool value=True]
                and [node_type=AndNode, type=root]
                
                operand1 -> and
                operand2 -> and
            }
            """
        )

        decision_graph = DecisionGraph(dot_graph=graph_dot[0], node_factory={
            "ValueNode": lambda: ValueLogicNode(None),
            "AndNode": lambda: AndLogicNode(None)
        })

        root_node = decision_graph.build()

        assert root_node.execute() is False

    def test_empty_graph(self):
        graph_dot = pydot.graph_from_dot_data(
            """
            digraph {
            }
            """
        )

        decision_graph = DecisionGraph(dot_graph=graph_dot[0], node_factory={})

        with pytest.raises(Exception) as e:
            decision_graph.build()

        assert str(e.value) == 'Root node not found'

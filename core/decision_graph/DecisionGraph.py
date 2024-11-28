from pydot import Node as PydotNode, Graph as PydotGraph, Edge as PydotEdge
import collections
from queue import Queue
from core.logic_nodes.LogicNode import LogicNode


class DecisionGraph:
    dot_graph: PydotGraph
    dot_nodes: list[PydotNode]

    def __init__(self, dot_graph: PydotGraph):
        self.dot_graph = dot_graph
        self.dot_nodes = dot_graph.get_nodes()
        self.dot_edges = dot_graph.get_edges()

    # def __from_dot_graph_to_graph(self):
    #     pass

    def __get_root_dot_node(self):
        root_node = next((x for x in self.dot_nodes if x.get("type") == "root"), None)
        if root_node is None:
            raise Exception("Root node not found")

        return root_node

    def __get_node_name_to_incoming_edges_dict(self):
        result: dict[str, list[PydotEdge]] = collections.defaultdict(list)

        for dot_edge in self.dot_edges:
            dest_node_name = dot_edge.get_destination()
            result[dest_node_name].append(dot_edge)

        return result

    def __get_node_name_to_node_map(self):

        pass

    def __get_bfs_transversal(self, root_node: PydotNode, node_name_to_incoming_edges_dict: dict[str, list[PydotEdge]]):
        queue: Queue[str] = Queue()
        node_name_visited_dict: dict[str, bool] = collections.defaultdict(lambda: False)
        traversal_path: list[str] = []

        queue.put(root_node.get_name())
        node_name_visited_dict[root_node.get_name()] = True

        while queue.not_empty:
            current_node_name = queue.get()
            traversal_path.append(current_node_name)
            edges = node_name_to_incoming_edges_dict[current_node_name]

            for edge in edges:
                dest_node_name: str = edge.get_destination()
                node_name_visited_dict[dest_node_name] = True
                queue.put(dest_node_name)

        return traversal_path

    def __build_decision_graph(self):
        root_dot_node = self.__get_root_dot_node()
        node_name_to_incoming_edges_dict = self.__get_node_name_to_incoming_edges_dict()

        bfs_traversal_path = self.__get_bfs_transversal(root_dot_node, node_name_to_incoming_edges_dict)

        # Reverse the traversal path to build leaf nodes first
        bfs_traversal_path_reversed_itr = reversed(bfs_traversal_path)
        for node_name in bfs_traversal_path_reversed_itr:


            node = self.__build_logic_node(node_name)


        pass

    def __build_logic_node(self, dot_node: PydotNode) -> LogicNode:
        pass

    def __get_node_dependencies(self, node: PydotNode) -> list[PydotNode]:
        pass


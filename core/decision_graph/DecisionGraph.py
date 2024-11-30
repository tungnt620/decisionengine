from collections.abc import Callable

from pydot import Node as PydotNode, Graph as PydotGraph, Edge as PydotEdge
import collections
from queue import Queue
from core.logic_nodes.LogicNode import LogicNode


class DecisionGraph:
    dot_graph: PydotGraph
    dot_nodes: list[PydotNode]
    node_factory: dict[str, Callable[[], LogicNode]]
    node_name_to_incoming_edges_dict: dict[str, list[PydotEdge]]
    node_name_to_dot_node_dict: dict[str, PydotNode]
    node_name_to_logic_node_dict: dict[str, LogicNode] = {}

    def __init__(self, dot_graph: PydotGraph, node_factory: dict[str, Callable[[], LogicNode]]):
        self.dot_graph = dot_graph
        self.dot_nodes = dot_graph.get_nodes()
        self.dot_edges = dot_graph.get_edges()
        self.node_factory = node_factory
        self.node_name_to_incoming_edges_dict = self.__get_node_name_to_incoming_edges_dict()
        self.node_name_to_dot_node_dict = self.__get_node_name_to_dot_node_dict()

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

    def __get_node_name_to_dot_node_dict(self) -> dict[str, PydotNode]:
        return {node.get_name(): node for node in self.dot_nodes}

    def __get_node_name_to_node_map(self):

        pass

    def __get_bfs_transversal(self, root_node: PydotNode):
        queue: Queue[str] = Queue()
        node_name_visited_dict: dict[str, bool] = collections.defaultdict(lambda: False)
        traversal_path: list[str] = []

        queue.put(root_node.get_name())
        node_name_visited_dict[root_node.get_name()] = True

        while not queue.empty():
            current_node_name = queue.get()
            traversal_path.append(current_node_name)
            incoming_edges = self.node_name_to_incoming_edges_dict[current_node_name]

            for edge in incoming_edges:
                source_node_name: str = edge.get_source()
                node_name_visited_dict[source_node_name] = True
                queue.put(source_node_name)

        return traversal_path

    def build(self) -> LogicNode:
        root_node: LogicNode | None = None
        root_dot_node = self.__get_root_dot_node()
        bfs_traversal_path = self.__get_bfs_transversal(root_dot_node)

        # Reverse the traversal path to build leaf nodes first
        bfs_traversal_path_reversed_itr = reversed(bfs_traversal_path)
        for node_name in bfs_traversal_path_reversed_itr:
            node = self.__build_logic_node(node_name)
            dependencies = self.__get_node_dependencies(node)
            node.add_dependencies(dependencies)
            self.node_name_to_logic_node_dict[node_name] = node

            if node_name == root_dot_node.get_name():
                root_node = node

        return root_node

    def __build_logic_node(self, node_name: str) -> LogicNode:
        dot_node = self.node_name_to_dot_node_dict.get(node_name)
        if dot_node is None:
            raise Exception("Node not found in node name to dot node dict")
        node_type = dot_node.get("node_type")
        node = self.node_factory[node_type]()
        node.set_dot_node(dot_node)

        return node

    def __get_node_dependencies(self, node: LogicNode) -> list[tuple[str, LogicNode]]:
        # Get incoming edges of this node
        incoming_edges = self.node_name_to_incoming_edges_dict.get(node.dot_node.get_name())
        if incoming_edges is None:
            raise Exception("Node not found in incoming edges dict")

        dependencies: list[tuple[str, LogicNode]] = []
        for incoming_edge in incoming_edges:
            source_dot_node = self.node_name_to_dot_node_dict.get(incoming_edge.get_source())
            if source_dot_node is None:
                raise Exception("Source node not found in node name to dot node dict")

            source_logic_node = self.node_name_to_logic_node_dict.get(source_dot_node.get_name())
            if source_logic_node is None:
                raise Exception("Source logic node not found in node name to logic node dict")

            edge_name = incoming_edge.get("name")
            dependencies.append((edge_name, source_logic_node))

        return dependencies

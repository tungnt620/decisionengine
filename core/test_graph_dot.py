import pydot


def main():
    graphs = pydot.graph_from_dot_file("./dot/examples/dg.dot")
    graph = graphs[0]

    print([edge.get_attributes() for edge in graph.get_edges()])
    print([node.get_name() for node in graph.get_nodes()])

    graph.write('dot/examples/dg2.dot')


if __name__ == '__main__':
    main()

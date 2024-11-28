import pydot


def main():
    graphs = pydot.graph_from_dot_file("./dot/examples/dg.dot")
    graph = graphs[0]

    print([edge.get_attributes() for edge in graph.get_edges()])
    print([node.get_name() for node in graph.get_nodes()])
    node = graph.get_nodes()[0]
    node.set('label', 'new label')
    print(node.get_attributes())
    edges = graph.get_edges()
    print(edges[0].get_source())
    print(edges[0].get_attributes())



    graph.write('dot/examples/dg2.dot')


if __name__ == '__main__':
    main()

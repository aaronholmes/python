from adjacencymatrix import AdjacencyMatrixGraph
from adjacencyset import AdjacencySetGraph


# Utility function
# TODO: move somewhere else/refactor
def graph_print_log(graph, vertices):
    for i in range(vertices):
        print("Adjacent to: ", i, graph.get_adjacent_vertices(i))

    for i in range(vertices):
        print("Indegree: ", i, graph.get_indegree(i))

    for i in range(vertices):
        for j in graph.get_adjacent_vertices(i):
            print("Edge weight: ", i, " ", j, " weight: ", graph.get_edge_weight(i, j))

    graph.display()


vertices = 4

graph = AdjacencyMatrixGraph(vertices)

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(2, 3)

graph_print_log(graph, vertices)

graph2 = AdjacencyMatrixGraph(vertices, True)

graph2.add_edge(0, 1)
graph2.add_edge(0, 2)
graph2.add_edge(2, 3)

graph_print_log(graph2, vertices)

graph3 = AdjacencySetGraph(vertices)
graph3.add_edge(0, 1)
graph3.add_edge(0, 2)
graph3.add_edge(2, 3)

graph_print_log(graph3, vertices)

graph4 = AdjacencySetGraph(vertices, True)

graph4.add_edge(0, 1)
graph4.add_edge(0, 2)
graph4.add_edge(2, 3)

graph_print_log(graph4, vertices)
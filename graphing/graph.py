import abc

import numpy as np

class Graph(abc.ABC):

    def __init__(self, numVertices, directed=False):
        self.numVertices = numVertices
        self.directed = directed

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        pass

    @abc.abstractmethod
    def get_indegree(self, v):
        pass

    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        pass

    @abc.abstractmethod
    def display(self):
        pass


class AdjacencyMatrixGraph(Graph):

    def __init__(self, numVertices, directed=False):
        super(AdjacencyMatrixGraph, self).__init__(numVertices, directed)
        self.matrix = np.zeros((numVertices, numVertices))

    def add_edge(self, v1, v2, weight=1):
        # Basic sanity check on parameter values
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds!" % (v1, v2))

        # Only allow positive weight for now
        if weight < 1:
            raise ValueError("An edge cannot have a weight less than 1")

        self.matrix[v1][v2] = weight

        # Undirected graph have two way relationships
        if not self.directed:
            self.matrix[v2][v1] = weight

    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex %d" % v)

        adjacent_vertices = []

        for i in range(self.numVertices):
            if self.matrix[v][i] > 0:
                adjacent_vertices.append(i)

        return adjacent_vertices

    def get_indegree(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex %d" % v)

        indegree = 0
        for i in range(self.numVertices):
            if self.matrix[v][i] > 0:
                indegree = indegree + 1

        return indegree

    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]

    def display(self):
        for i in range(self.numVertices):
            for v in self.get_adjacent_vertices(i):
                print(i, "-->", v)


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

from _collections import deque

from Vertex import Vertex
from vertex_neighbors import get_neighbours


class Graph:
    def __init__(self, base_a, base_b, dim):
        self.vertex_lst = []
        self.vertex_lst.append(Vertex(base_a, base_b))
        self.dim = dim
        self.build()

    def build(self):
        queue = deque()
        queue.append(self.vertex_lst[0])

        while queue:
            v = queue.popleft()
            v_neighbours_lst = get_neighbours(v)
            for neighbour in v_neighbours_lst:
                self.add_vertex(neighbour)
                self.add_edge(v, neighbour)
                queue.append(neighbour)

    def add_vertex(self, vertex):
        if vertex not in self.vertex_lst:
            self.vertex_lst.append(vertex)

    def add_edge(self, vertex1: Vertex, vertex2: Vertex):
        vertex1.near_lst.append(vertex2)
        vertex2.near_lst.append(vertex1)

    def print_graph(self):
        for vertex in self.vertex_lst:
            print(vertex)

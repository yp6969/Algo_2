import pickle
from _collections import deque

from AlgoUtils import color_print, Colors
from Vertex import Vertex
from vertex_neighbors import get_neighbours


class Graph:
    def __init__(self, base_a, base_b, dim):
        self.vertex_cnt = 0
        self.vertex_lst = []
        self.vertex_lst.append(Vertex(base_a, base_b, dim, self.vertex_cnt))
        self.dim = dim
        self.build()

    def has_vertex(self, vertex):
        for v in self.vertex_lst:
            if v.equals(vertex):
                return True
        return False

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

    def save_graph_to_file(self, file_path, print_info=False):
        try:
            with open(file_path, 'wb') as f:
                pickle.dump(self, f)
                if print_info:
                    color_print(f'Saved Graph to {file_path}', Colors.BLUE)
        except Exception as e:
            color_print(f'Failed to save graph to {file_path}. Reason: {e}', Colors.RED)

    def size(self):
        return len(self.vertex_lst)

    def print_graph(self):
        color_print(f'Graph has {self.size()} vertices, dim={self.dim}\n', Colors.BLUE)
        color_print(f'Printing Adjacency list and after that the vertices', Colors.BLUE + Colors.UNDERLINE)
        self.print_adjacency_list()
        color_print('\nVertices', Colors.BOLD + Colors.UNDERLINE + Colors.BLUE)
        self.print_vertices()

    def print_adjacency_list(self):
        for vertex in self.vertex_lst:
            near_lst_ids = [v.id for v in vertex.near_lst]
            print(f'{vertex.id} -> {near_lst_ids}')

    def print_vertices(self):
        for vertex in self.vertex_lst:
            print(vertex)

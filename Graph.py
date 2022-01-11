import os
import pickle
from _collections import deque

from AlgoUtils import color_print, Colors
from Vertex import Vertex
from vertex_neighbors import get_neighbours


class Graph:
    def __init__(self, base_a, base_b, dim):
        self.vertex_lst = []
        self.base_a = base_a
        self.base_b = base_b
        self.vertex_lst.append(Vertex(base_a, base_b, dim, v_id=0))
        self.vertex_cnt = 1
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
        if vertex in self.vertex_lst:
            return
        if vertex.v_id == 'NA':
            vertex.v_id = self.vertex_cnt
            self.vertex_cnt += 1
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

    def __make_plots_directory(self):
        path = './graph_plots'
        if not os.path.exists(path):
            os.mkdir(path)
        return path

    def plot_graph(self, title="", file_name=None):
        import networkx as nx
        import matplotlib.pyplot as plt
        plt.clf()
        G = nx.Graph()
        vertex_lst = self.vertex_lst
        edges = []
        for vertex in vertex_lst:
            edges += [(vertex, neighbour) for neighbour in vertex.near_lst]
        options = {'node_size': 23000, 'width': 2}
        G.add_edges_from(edges)
        plt.figure(figsize=(25, 25))
        if title:
            plt.title(title, fontdict={'size': 30})
        nx.draw(G, with_labels=True, font_weight='bold', **options)
        if file_name:
            dir_path = self.__make_plots_directory()
            file_path = os.path.join(dir_path, file_name)
            plt.savefig(file_path)
        else:
            plt.show()

    def print_graph(self):
        color_print(f'Graph has {self.size()} vertices, dim={self.dim}\n', Colors.BLUE)
        color_print(f'Printing Adjacency list and after that the vertices', Colors.BLUE + Colors.UNDERLINE)
        self.print_adjacency_list()
        color_print('\nVertices', Colors.BOLD + Colors.UNDERLINE + Colors.BLUE)
        self.print_vertices()

    def print_adjacency_list(self):
        for vertex in self.vertex_lst:
            near_lst_ids = [v.v_id for v in vertex.near_lst]
            print(f'{vertex.v_id} -> {near_lst_ids}')

    def print_vertices(self):
        for vertex in self.vertex_lst:
            print(vertex)

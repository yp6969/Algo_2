from numpy import inf as inf_value


class Vertex:
    id_cnt = 0

    def __init__(self, base_a, base_b):
        self.base_a = base_a
        self.base_b = base_b
        self.dv = inf_value
        self.id = Vertex.id_cnt
        Vertex.id_cnt += 1
        self.near_lst = []  # neighbours list

    def add_neighbour(self, new_neighbour):
        self.near_lst.append(new_neighbour)

    def get_dv(self):
        return self.dv

    def set_dv(self, d):
        self.dv = d

    def __str__(self):
        return f"Vertex with id {self.id}, neighbours = {[neighbour.id for neighbour in self.near_lst]}\n" \
               f"baseA = {self.base_a}\n" \
               f"baseB = {self.base_b}\n" \
 \
 \
"""
Vertex example:
    vertex.base_a = {vector0: switched(True/False),  vector1: switched(True/False) ... }
    vertex.base_b = {vector0: switched(True/False),  vector1: switched(True/False) ... }
    vertex.id = running index from 0 that increasing every Vertex creation
    vertex.dv = infinity_value  # prepare for BFS
    vertex.near_lst = [vertex1, vertex2, vertex3..]  # neighbour list
"""

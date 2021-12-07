from Graph import Graph
from Vertex import Vertex

base_a = '001010100'
base_b = '100110111'
print(f'base_a = {base_a}, base_b={base_b}')
g = Graph(base_a, base_b, 3)
g.print_graph()
print(g.has_vertex(Vertex(base_b, base_a, 3)))
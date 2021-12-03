from AlgoUtils import color_print, Colors
from Graph import Graph

from BinaryLinearSpace import BinaryLinearSpace
import itertools
import multiprocessing
from Vertex import Vertex
import os


class Runner:

    def __init__(self):
        self.path_for_files = None
        self.dim = None
        self.print_info = None

    def get_path_for_files(self, len_groupA, len_groupB, dim):
        curr_dir = os.getcwd()
        output_dir = os.path.join(curr_dir, 'output')
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        specific_output_dir_name = "{}_{}_dim{}".format(len_groupA, len_groupB, dim)
        specific_run_output_dir = os.path.join(output_dir, specific_output_dir_name)
        if not os.path.exists(specific_run_output_dir):
            os.mkdir(specific_run_output_dir)
        return specific_run_output_dir

    def run(self, groupA, groupB, dim, num_of_processes, print_info=False):
        color_print('@@@@@@@ Start Running @@@@@@@@@', Colors.BLUE + Colors.UNDERLINE + Colors.BOLD)
        bases_tuples = itertools.product(groupA, groupB)
        self.path_for_files = self.get_path_for_files(len(groupA), len(groupB), dim)
        self.dim = dim
        self.print_info = print_info
        pool = multiprocessing.Pool(processes=num_of_processes)
        pool.map(self.build_graph_and_save_to_file, bases_tuples)

    def get_string_base_as_list(self, base):
        num_of_vectors = (len(base) + self.dim - 1) // self.dim
        step = self.dim
        return [base[i: i + step] for i in range(0, num_of_vectors * step, step)]

    def build_graph_and_save_to_file(self, bases_tuple):
        if self.print_info:
            print("pid:{} is running {}".format(os.getpid(), bases_tuple))
        base_a, base_b = bases_tuple
        graph = Graph(base_a, base_b, self.dim)
        graph_file_name = "{}_{}.p".format(base_a, base_b)
        graph_file_path = os.path.join(self.path_for_files, graph_file_name)
        graph.save_graph_to_file(graph_file_path, self.print_info)
        dest_vertex = Vertex(base_b, base_a, self.dim)
        self.print_result(base_a, base_b, graph.has_vertex(dest_vertex))

    def print_result(self, base_a, base_b, result):
        color = Colors.GREEN if result else Colors.RED
        if self.print_info:
            base_a = self.get_string_base_as_list(base_a)
            base_b = self.get_string_base_as_list(base_b)
            color_print('----------- {} -----------'.format(result), color)
            for i in range(len(base_a)):
                color_print('{}  {}'.format(base_a[i], base_b[i]), color)
            color_print('--------------------------'.format(result), color)
        else:
            color_print('(pid {}) {} for bases: {} {}'.format(os.getpid(), result, base_a, base_b), color)

    def run_I_To_All(self, dim, num_of_processes, print_info=False):
        space = BinaryLinearSpace(dim)
        all_bases = space.get_all_bases()
        standart_base = all_bases.pop(0)
        self.run([standart_base], all_bases, dim=dim, num_of_processes=num_of_processes, print_info=print_info)
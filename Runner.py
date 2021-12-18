import json
import pickle

from AlgoUtils import color_print, Colors, timer
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
        return specific_run_output_dir

    def create_directory(self, dir_path):
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

    @timer
    def run(self, groupA, groupB, dim, num_of_processes, print_info=False, override=False):
        color_print('@@@@@@@ Start Running @@@@@@@@@', Colors.BLUE + Colors.UNDERLINE + Colors.BOLD)
        self.path_for_files = self.get_path_for_files(len(groupA), len(groupB), dim)
        self.dim = dim
        self.print_info = print_info
        pool = multiprocessing.Pool(processes=num_of_processes)
        need_to_load = os.path.exists(self.path_for_files)
        # self.create_directory(self.path_for_files)
        # if need_to_load and not override:
        #     color_print(f'Loading graphs from {self.path_for_files}', Colors.BLUE)
        #     files_names = os.listdir(self.path_for_files)
        #     results = pool.map(self.load_graph_and_check_results, files_names)
        # else:
        bases_tuples = itertools.product(groupA, groupB)
        results = pool.map(self.build_graph_and_check_results, bases_tuples)

        results_path = self.save_results_to_file(results)
        color_print(f'Results can be found at: {results_path}', Colors.BLUE)

    def load_graph_and_check_results(self, file_name):
        file_full_path = os.path.join(self.path_for_files, file_name)
        with open(file_full_path, 'rb') as f:
            graph = pickle.load(f)
        if self.print_info:
            print("pid:{} is running {}".format(os.getpid(), (graph.base_a, graph.base_b)))
            self.print_result_of_graph(graph)
        return self.get_result(graph)

    def build_graph_and_check_results(self, bases_tuple):
        """
        Building the graph for bases_tuple, saving it to file
        """
        if self.print_info:
            print("pid:{} is running {}".format(os.getpid(), bases_tuple))
        base_a, base_b = bases_tuple
        graph = Graph(base_a, base_b, self.dim)
        # graph_file_name = "{}_{}.p".format(base_a, base_b)
        # graph_file_path = os.path.join(self.path_for_files, graph_file_name)
        # graph.save_graph_to_file(graph_file_path)
        if self.print_info:
            self.print_result_of_graph(graph)
        return self.get_result(graph)

    def get_result(self, graph):
        base_a = graph.base_a
        base_b = graph.base_b
        dest_vertex = Vertex(base_b, base_a, self.dim)
        result = graph.has_vertex(dest_vertex)
        return f'[{base_a}][{base_b}]: {result}'

    def print_result_of_graph(self, graph):
        base_a = graph.base_a
        base_b = graph.base_b
        dest_vertex = Vertex(base_b, base_a, self.dim)
        result = graph.has_vertex(dest_vertex)
        color = Colors.GREEN if result else Colors.RED
        base_a = self.get_string_base_as_list(base_a)
        base_b = self.get_string_base_as_list(base_b)
        color_print('----------- {} -----------'.format(result), color)
        for i in range(len(base_a)):
            color_print('{}  {}'.format(base_a[i], base_b[i]), color)
        color_print('--------------------------'.format(result), color)

    def save_results_to_file(self, results):
        result_path = self.path_for_files + '.json'
        with open(result_path, 'w') as f:
            json.dump(results, f, indent=4, ensure_ascii=False)
        return result_path

    def get_string_base_as_list(self, base):
        num_of_vectors = (len(base) + self.dim - 1) // self.dim
        step = self.dim
        return [base[i: i + step] for i in range(0, num_of_vectors * step, step)]

    def run_I_To_All(self, dim, num_of_processes, print_info=False):
        space = BinaryLinearSpace(dim)
        all_bases = space.get_all_bases()
        standart_base = all_bases.pop(0)
        self.run([standart_base], all_bases, dim=dim, num_of_processes=num_of_processes, print_info=print_info)
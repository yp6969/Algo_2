
from Runner import *
import argparse
import platform
import json
import itertools

# Parameters for Windows running
N = 4
PROC_NUM = 1
PRINT_INFO = True
OVERRIDE = True


def get_bases(dim):
    file_name = f'bases_{dim}.json'
    if os.path.exists(file_name):
        color_print(f'Loading Bases from {file_name}', Colors.BLUE)
        with open(file_name, 'r') as f:
            return json.load(f)
    space = BinaryLinearSpace(args.dim)
    bases = space.get_all_bases()
    space.save_bases_to_files(bases)
    return bases


def exec(args):
    if platform.system() == 'Windows':
        args.dim = N
        args.proc_num = PROC_NUM
        args.print_info = PRINT_INFO
        args.override = OVERRIDE
    args.dim = int(args.dim)
    args.proc_num = int(args.proc_num)
    bases = get_bases(args.dim)
    standart_base = bases.pop(0)
    runner = Runner()
    runner.run([standart_base], bases, dim=args.dim, num_of_processes=args.proc_num, print_info=args.print_info,
               override=args.override)


def parse_args():
    parser = argparse.ArgumentParser(description='Running Algo2 question according to given flags')
    parser.add_argument('-d', '--dim', dest='dim', help='Dimension')
    parser.add_argument('-p', '--procnum', dest='proc_num', help='num of processes to run the program')
    parser.add_argument('-i', '--print_info', dest='print_info', action='store_true',
                        help='print additional info')
    parser.add_argument('--override', dest='override', action='store_true',
                        help='override the graphs directory if exists')
    return parser.parse_args()


def run_with_perms():
    runner = Runner()
    runner.run_with_perms(5, 3)


if __name__ == '__main__':
    # args = parse_args()
    # exec(args)
    run_with_perms()

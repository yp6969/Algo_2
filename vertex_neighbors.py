import numpy as np
import Global_funcs_Trees
from Vertex import Vertex
from binmatrix import BinMatrix


def isBase(list_of_strings, dim):
    """
    :param list_of_strings: represents list of vectors which given in strings.
    the func convert the vectors to int.
    :return: true if the list represent a linear space base.
    """
    if dim != len(list_of_strings):  # case: 2 same vectors (keys) in base so dictionary size will be dim-1
        return False
    int_base = []
    for string in list_of_strings:
        row = [int(x) for x in string]
        int_base.append(row)
    matrix_base = BinMatrix(int_base)
    return matrix_base.is_base()


def swapVec(baseA, baseB, vecA, vecB):
    newBaseA = {}
    newBaseB = {}
    for vec in baseA:
        if vec != vecA:
            newBaseA[vec] = baseA[vec]
        else:
            newBaseA[vecB] = True
    for vec in baseB:
        if vec != vecB:
            newBaseB[vec] = baseB[vec]
        else:
            newBaseB[vecA] = True
    return newBaseA, newBaseB


def get_neighbours(vertex):
    # Assumption - base given in list of strings
    neighbours = []
    baseA = vertex.base_a
    baseB = vertex.base_b
    dim   = len(baseB.keys())
    for a_vec, a_switched in baseA.items():
        if a_switched:
            continue
        for b_vec, b_switched in baseB.items():
            if b_switched:
                continue
            baseA, baseB = swapVec(baseA, baseB, a_vec, b_vec)
            if isBase(baseA.keys(), dim) and isBase(baseB.keys(), dim):
                neighbours.append(Vertex(baseA, baseB))
            baseA, baseB = swapVec(baseA, baseB, b_vec, a_vec)  # swap back to continue loop
            baseA[a_vec] = False
            baseB[b_vec] = False
    return neighbours

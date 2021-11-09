import numpy as np
import Global_funcs_Trees
from binmatrix import BinMatrix


def isBase(list_of_strings):
    """
    :param list_of_strings: represents list of vectors which given in strings.
    the func convert the vectors to int.
    :return: true if the list represent a linear space base.
    """
    int_base = []
    i = 0
    for string in list_of_strings:
        int_base[i] = Global_funcs_Trees.convert_str_to_uint16(string)
        i += 1

    matrix_base = BinMatrix(int_base)
    return matrix_base.is_base()


def swapVec(dictA, dictB, keyA, keyB):
    newDictA = {}
    newDictB = {}
    for key in dictA:
        if key != keyA:
            newDictA[key] = dictA[key]
        else:
            newDictA[keyB] = True
    for key in dictB:
        if key != keyB:
            newDictB[key] = dictB[key]
        else:
            newDictB[keyA] = True
    return newDictA, newDictB


def get_neighbours(vertex):
    # Assumption - base given in list of strings
    neighbours = []
    baseA = vertex.base_a
    baseB = vertex.base_b

    for a_vec, a_switched in baseA.items():
        if a_switched:
            continue
        for b_vec, b_switched in baseB.items():
            if b_switched:
                continue
            baseA, baseB = swapVec(baseA, baseB, a_vec, b_vec)
            if isBase(baseA.keys()) and isBase(baseB.keys()):
                neighbours.append(Vertex(baseA, baseB))  # TODO check how to init vertex, fix it later
            baseA, baseB = swapVec(baseA, baseB, a_vec, b_vec)  # swap back to continue loop
    return neighbours



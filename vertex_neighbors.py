import numpy as np
import Global_funcs_Trees
from Vertex import Vertex
from binmatrix import BinMatrix


def isBase(list_of_strings):
    """
    :param list_of_strings: represents list of vectors which given in strings.
    the func convert the vectors to int.
    :return: true if the list represent a linear space base.
    """
    int_base = []
    for string in list_of_strings:
        row = [int(x) for x in string]
        int_base.append(row)
    matrix_base = BinMatrix(int_base)
    return matrix_base.is_base()


def swapVec(dictA, dictB, keyA, keyB):
    # TODO shani: change variable names to something that make more sense
    # TODO shani: not need to create new dict, maybe can work on the exists ones (?)
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

            # TODO shani: sometimes one row is disappeared
            # בגלל שמתבצעת החלפה עם וקטור שכבר קיים בבסיס
            # ומדובר במילון, אז השורות הזהות לא נספרות פעמיים והן הופכות לאחת
            baseA, baseB = swapVec(baseA, baseB, a_vec, b_vec)
            if isBase(baseA.keys()) and isBase(baseB.keys()):
                neighbours.append(Vertex(baseA, baseB))  # TODO check how to init vertex, fix it later

            # TODO shani: need to turn off the flags of b_vec, a_vec
            baseA, baseB = swapVec(baseA, baseB, b_vec, a_vec)  # swap back to continue loop
    return neighbours



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
<<<<<<< HEAD
    if len(list_of_strings) != dim:  # case: 2 same vectors (keys) in base so dictionary size will be dim-1 (same keys)
=======
    if len(list_of_strings) != dim: # case: 2 same vectors (keys) in base so dictionary size will be dim-1 (same keys)
>>>>>>> b14c22b6afee0171ec2d1941881b62593e0cbc71
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


<<<<<<< HEAD
def get_neighbours(vertex, sourceVertex=None):
=======
def get_neighbours(vertex, isLastLayer=False, foundSwappedVertex=False):
>>>>>>> b14c22b6afee0171ec2d1941881b62593e0cbc71
    # Assumption - base given in list of strings
    neighbours = []
    baseA = vertex.base_a.copy()
    baseB = vertex.base_b.copy()
<<<<<<< HEAD
    foundSwappedVertex = False
=======
>>>>>>> b14c22b6afee0171ec2d1941881b62593e0cbc71
    dim = len(baseB.keys())
    for a_vec, a_switched in baseA.items():
        if a_switched:
            continue
        for b_vec, b_switched in baseB.items():
            if b_switched:
                continue
<<<<<<< HEAD
            tmpbaseA, tmpbaseB = swapVec(baseA, baseB, a_vec, b_vec)
            if isBase(tmpbaseA.keys(), dim) and isBase(tmpbaseB.keys(), dim):
                neighbours.append(Vertex(tmpbaseA, tmpbaseB, dim))
                if sourceVertex is not None:
                    if sourceVertex.base_a == tmpbaseB and sourceVertex.base_b == tmpbaseA:
                        foundSwappedVertex = True
                        break
            # baseA, baseB = swapVec(baseA, baseB, b_vec, a_vec)  # swap back to continue loop
            # baseA[a_vec] = False
            # baseB[b_vec] = False
        if foundSwappedVertex:
            break
    return neighbours if sourceVertex is None else (neighbours, foundSwappedVertex)
=======
            swapVec(baseA, baseB, a_vec, b_vec)
            if isBase(baseA.keys(), dim) and isBase(baseB.keys(), dim):
                neighbours.append(Vertex(baseA, baseB))
                if isLastLayer and vertex.base_a == baseB and vertex.base_b == baseA:
                    foundSwappedVertex = True
                    break
            swapVec(baseA, baseB, b_vec, a_vec)  # swap back to continue loop
            baseA[a_vec] = False
            baseB[b_vec] = False
        if foundSwappedVertex:
            break
    return neighbours, foundSwappedVertex
>>>>>>> b14c22b6afee0171ec2d1941881b62593e0cbc71


def is2BasesCanSwap(vertex):
    baseA = vertex.base_a
    baseB = vertex.base_b
    layer = 1
    dim = len(vertex)
    foundSwappedVertex = False
    currentLayerNeighbours, foundSwappedVertex = get_neighbours(vertex)
    while layer < dim:
        # handle last layer:
<<<<<<< HEAD
        # if layer == dim - 2:
        currentLayerNeighbours, foundSwappedVertex = get_neighbours(vertex, foundSwappedVertex)
        if foundSwappedVertex:
            return layer
        # else:
        #    currentLayerNeighbours, _ = nextLayersNeighbours(currentLayerNeighbours)
        layer += 1
    return layer


def nextLayersNeighbours(array_of_layer):
=======
        if layer == dim - 2:
            currentLayerNeighbours, foundSwappedVertex = get_neighbours(vertex, True, foundSwappedVertex)
            if foundSwappedVertex:
                return True
        else:
           currentLayerNeighbours, foundSwappedVertex = layers_neighbours(currentLayerNeighbours)
    return False


def layers_neighbours(array_of_layer):
>>>>>>> b14c22b6afee0171ec2d1941881b62593e0cbc71
    neighbours = []
    for vertex in array_of_layer:
        neighbours += get_neighbours(vertex)
    return neighbours


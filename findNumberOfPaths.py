import numpy as np
import Global_funcs_Trees
from Vertex import Vertex
from binmatrix import BinMatrix
from _collections import deque
import json


def isBase(list_of_strings, dim):
    """
    :param list_of_strings: represents list of vectors which given in strings.
    the func convert the vectors to int.
    :return: true if the list represent a linear space base.
    """

    if len(list_of_strings) != dim:  # case: 2 same vectors (keys) in base so dictionary size will be dim-1 (same keys)
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


def get_neighbours(vertex, sourceVertex=None):
    # Assumption - base given in list of strings
    neighbours = []
    baseA = vertex.base_a.copy()
    baseB = vertex.base_b.copy()
    foundSwappedVertex = False
    dim = len(baseB.keys())
    for a_vec, a_switched in baseA.items():
        if a_switched:
            continue
        for b_vec, b_switched in baseB.items():
            if b_switched:
                continue
            tmpbaseA, tmpbaseB = swapVec(baseA, baseB, a_vec, b_vec)
            if isBase(tmpbaseA.keys(), dim) and isBase(tmpbaseB.keys(), dim):
                neighbours.append(Vertex(tmpbaseA, tmpbaseB, dim))
                if sourceVertex is not None:
                    if sourceVertex.base_a == tmpbaseB and sourceVertex.base_b == tmpbaseA:
                        foundSwappedVertex = True
                        break
        if foundSwappedVertex:
            break
    return neighbours if sourceVertex is None else (neighbours, foundSwappedVertex)


def run(fileName, dim):
    try:
        basesFile = open(fileName)
        data = json.load(basesFile)
        basesFile.close()
        sBase = data[0]
        allOtherBases = data[1:]
        minimumNumPath = float("inf")
        minimumVer = 0
        maximumVer = 0
        maximumNumPath = -1
        allVerPaths = []
        for base in allOtherBases:
            testedVertex = Vertex(sBase, base, dim)
            tempResultOfPath = findAllPaths(testedVertex, dim)
            if tempResultOfPath < minimumNumPath:
                minimumNumPath = tempResultOfPath
                minimumVer = sBase + base

            if maximumNumPath < tempResultOfPath:
                maximumNumPath = tempResultOfPath
                maximumVer = sBase + base
            allVerPaths.append((sBase + base, tempResultOfPath))
        with open('allPaths{di}.json'.format(di=dim), 'w') as fp:
            json.dump(("minNum = " + minimumVer, minimumNumPath), fp)
            json.dump(("maxNum = " + maximumVer, maximumNumPath), fp)
            json.dump(allVerPaths, fp)



    except Exception as e:
        raise ValueError(e)


def findAllPaths(vertex, dim):
    target_base_a = vertex.base_b
    target_base_b = vertex.base_a
    targetVer = Vertex(target_base_a, target_base_b, dim)
    paths = 0
    layer = 0
    neighboursByLayers = deque()
    neighboursByLayers.append(vertex)
    allReadySearched = set()
    while layer < dim:
        length = len(neighboursByLayers)
        for i in range(length):
            neighbours = get_neighbours(neighboursByLayers.popleft())
            for n in neighbours:
                if compareVer(n.base_a, targetVer.base_a) and compareVer(n.base_b, targetVer.base_b):
                    paths += 1
                    continue
                if n not in allReadySearched:
                    neighboursByLayers.append(n)

            allReadySearched.update(neighbours)
        layer += 1
    return paths


def compareVer(verA, verB):
    vectorsListA = [vec for vec in verA.keys()]
    vectorsListB = [vec for vec in verB.keys()]
    vectorsListA.sort()
    vectorsListB.sort()
    return vectorsListA == vectorsListB


if __name__ == '__main__':
    run("bases_4.json", 4)

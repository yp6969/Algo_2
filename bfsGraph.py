import json
from fullGraphVertex import Vertex
from itertools import combinations
from itertools import product
from AlgoUtils import timer
from _collections import deque
from AlgoUtils import color_print, Colors


class HTMN_GRAPH:
    def __init__(self, baseFileName, dim):

        """
        vertexHash:
            A quick way to find vertices in the graph and in addition we can check using it whether we got a base,
            Key: The decimal value of the two bases connected , each base in the lexicographic order!
            Value: The vertex from the list of the graph
        """
        self.__dim = dim
        self.__vertex_lst = []
        self.__vertexHash = {}  # עשינו רשימה ע׳׳מ לחבר את הקוקדים המקוריים של הגרף
        self.__targetsVertex = []   # This are the vertex's that we need to check if their distance from the opposite vertex
        self.createAllVertices(baseFileName)
        self.build()

    @timer
    def build(self):
        for vertex in self.__vertex_lst:
            # This method will return for us the original vertex from the vertex list field.
            v_neighbours_lst = self.findAllNeighbours(vertex)
            for neighbour in v_neighbours_lst:
                self.add_edge(vertex, neighbour)

    def add_edge(self, vertex1: Vertex, vertex2: Vertex):
        vertex1.near_lst.append(vertex2)

    @timer
    def buildBases(self, basesStringsArray, dimension):
        # Split the base line into vectors in the dim length.
        chunks, chunk_size = len(basesStringsArray[0]), len(basesStringsArray[0]) // dimension
        basesResult = []
        for baseString in basesStringsArray:
            vectors = [baseString[i: i + chunk_size] for i in range(0, chunks, chunk_size)]
            basesResult.append(self.buildBase(vectors))
        return basesResult

    def buildBase(self, vectorsList):
        baseResult = {}
        for vector in vectorsList:
            baseResult[vector] = False
        return baseResult

    @timer
    def buildAllBaseCombinations(self, basesList):
        """
        Will return to us all the combinations of two bases a, b
        And then we will delete all the pairs that contain the same value: aa / bb ...
        """
        allCombinations = list(product(basesList, basesList))
        for base in basesList:
            # Deleting all the tuples with the same base (a, a)
            allCombinations.remove((base, base))
        return allCombinations

    @timer
    def createAllVertices(self, baseFileName):
        firstVertexCreated = False
        standardBase = 0
        try:
            basesFile = open(baseFileName)
            data = json.load(basesFile)
            basesFile.close()
            allBaseCombinations = self.buildAllBaseCombinations(self.buildBases(data, self.__dim))
            # Until this stage we create all the bases combinations
            for tupleBases in allBaseCombinations:
                if not firstVertexCreated:
                    standardBase = tupleBases[0]
                    firstVertexCreated = True
                newVertex = Vertex(tupleBases[0], tupleBases[1])
                if standardBase == tupleBases[0]:
                    self.__targetsVertex.append(newVertex)
                self.__vertex_lst.append(newVertex)
                self.__vertexHash[self.getVertexAsInt(tupleBases[0], tupleBases[1])] = newVertex
            color_print(f'{len(self.__vertex_lst)} Vertices created, now need to create edges between neighbors',
                        Colors.YELLOW + Colors.UNDERLINE + Colors.BOLD)
        except Exception as e:
            raise ValueError(f'createAllVertices failed according to : {e} \n')

    def getVertexAsInt(self, baseA, baseB):
        # We need that because we cant use dictionary as key in hash
        stringRes = ""
        for key in baseA:
            stringRes += key
        for key in baseB:
            stringRes += key
        return int(stringRes, 2)

    def findAllNeighbours(self, vertex):
        """
        This method may be improved in terms of efficiency,
        But it is the simplest way to return all the neighbors of a particular vertex in the graph.
        In addition we take care here to return the vertices from the original list of data structure.  ;D

        We will take all the vectors to two separate lists and make head-to-head exchanges,
        Each time for a particular vector and then we will check if we got a valid bases with help of our hash table,
        If we got a valid bases we will add the vertex we found using the hash table to the neighbors list
        and make sure for a true connection too! because we are getting from the hash table the original vertex.
        """
        neighbours = []
        baseAVecs = []  # hold all the vectors from baseA
        baseBVecs = []  # hold all the vectors from baseB
        for key in vertex.base_a:
            baseAVecs.append(key)
        for key in vertex.base_b:
            baseBVecs.append(key)

        for i in range(self.__dim):  # Head to head exchange logic
            for j in range(self.__dim):
                copyBaseA_Vecs = baseAVecs.copy()  # Need copy because we do not want to edit the original values.
                copyBaseB_Vecs = baseBVecs.copy()
                vecToSwap = copyBaseA_Vecs[i]  # Simple swap logic
                copyBaseA_Vecs[i] = copyBaseB_Vecs[j]
                copyBaseB_Vecs[j] = vecToSwap
                try:
                    # Case 1: we got the same vertex
                    if vertex == self.findVertexByLists(copyBaseA_Vecs, copyBaseB_Vecs):
                        continue
                    neighbours.append(self.findVertexByLists(copyBaseA_Vecs, copyBaseB_Vecs))  # Will add in good case.
                # Case 2: the exchange we made for the vectors did not create a valid base for us.
                except KeyError:
                    continue
                except Exception as e:
                    raise ValueError(f'findAllNeighbours failed according to : {e} \n')
        return neighbours

    def findVertexByLists(self, baseA_VectorsList, baseB_VectorsLists):
        """
        This method receives two lists of vectors from each base,
        And returns whether both are bases by looking for their vertex in the hash table.
        """
        baseA_VectorsList.sort()
        baseB_VectorsLists.sort()
        stringOfBases = "".join(baseA_VectorsList) + "".join(baseB_VectorsLists)
        return self.__vertexHash[int(stringOfBases, 2)]

    def getV(self, index):
        return self.__vertex_lst[index]

    def getAllV(self):
        return self.__vertex_lst

    def getVertexHash(self):
        return self.__vertexHash

    def getOppositeVertex(self, vertex):
        baseAVecs = []
        baseBVecs = []
        for key in vertex.base_a:
            baseAVecs.append(key)
        for key in vertex.base_b:
            baseBVecs.append(key)
        stringOfBases = "".join(baseBVecs) + "".join(baseAVecs)
        return self.__vertexHash[int(stringOfBases, 2)]

    def getTargetsVertices(self):
        return self.__targetsVertex



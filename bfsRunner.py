# Written by : Mor & Tom & Hen & Niv

from queue import Queue
from bfsGraph import *
from AlgoUtils import color_print, Colors


class BFS:

    def __init__(self, g):
        """
        infVer:
            hash table that will help us to determine if we already add a vertex with 'inf' distance to the queue
            when we need to add one like that [ when bfs run ends for a particular route...]
        """
        self.__graph = g
        self.__root = 0
        self.__asBeenScanned = []
        self.__firstScan = True

    @timer
    def run(self, start):
        """
        First we will reset the old values of the distances and the pi's fields,
        afterwards we will run the BFS methodology with the help of the 'Queue' data structure and will be assisted
        with the 'findDiffVec' method that we build that help us to determine if we can move forward to
        neighbour vertex.

        ~~~Important!!~~~
        We will find the path of the main vertex to its destination and not for all the vertices!
        Because we depend here on the vertex where we started in the scan to determine whether
        we have already visited a  particular vertex or not

        To get a the route for a specific vertex it must be provided to the method! [via the 'start' arg]
        """
        q = Queue()
        if self.__firstScan:
            self.resetGraph()
            self.__firstScan = False
        else:
            self.resetScannedVertices()
            self.__asBeenScanned = []
        self.__root = start  # This variable will help us to determine the route.
        self.__asBeenScanned.append(start)
        start.set_dv(0)
        q.put(start)
        while not q.empty():
            currentVertex = q.get()
            for neighbour in currentVertex.near_lst:
                keyA, keyB = self.findDiffVec(currentVertex, neighbour)
                if neighbour.base_a[keyA] or neighbour.base_b[keyB]:
                    continue
                if neighbour.get_dv() > currentVertex.get_dv() + 1:
                    self.__asBeenScanned.append(neighbour)
                    neighbour.base_a[keyA] = True
                    neighbour.base_b[keyB] = True
                    neighbour.set_dv(currentVertex.get_dv() + 1)
                    neighbour.set_pi(currentVertex)
                    q.put(neighbour)
        return 0

    def resetGraph(self):
        # Reset all the distances first, and the boolean flags & pi's.
        for vertex in self.__graph.getAllV():
            vertex.set_dv(float('inf'))
            vertex.set_pi(0)
            self.resetBooleanFlags(vertex)

    def resetScannedVertices(self):
        for vertex in self.__asBeenScanned:
            vertex.set_dv(float('inf'))
            vertex.set_pi(0)
            self.resetBooleanFlags(vertex)

    def resetBooleanFlags(self, vertex):
        for key in vertex.base_a:
            vertex.base_a[key] = False
        for key in vertex.base_b:
            vertex.base_b[key] = False

    def findDiffVec(self, vertex, vertex_Dest):
        """
        This method will return for us the 2 vectors which have been replaced between the current vertex to the
        neighbour vertex and with them we will check if the transition is valid before we check the distance.
        """
        keyA = keyB = 0
        for key, value in vertex_Dest.base_a.items():
            if key not in vertex.base_a:
                keyA = key

        for key, value in vertex_Dest.base_b.items():
            if key not in vertex.base_b:
                keyB = key

        return keyA, keyB

    def retAllVertexWithDistance(self, d):
        """
        Side method that need to be removed in final stage, we use her to detect bugs.
        """
        res = []
        for vertex in self.__graph.getAllV():
            if vertex.get_dv() == d:
                res.append(vertex)
        return res

    def findVerWithInfVal(self):
        for vertex in self.__graph.getAllV():
            if vertex.get_dv() == float('inf'):
                try:
                    exists = self.__infVer[vertex]
                    continue
                except KeyError:
                    self.__infVer[vertex] = True
                    vertex.set_dv(0)
                    return vertex
        return 0


if __name__ == "__main__":
    """
    For graphs of base 5 and above it's impossible to generate a graph due to the sheer number of bases
    formula : {k = number of bases} => (knCr2) * 2
    """
    color_print('Start running: First lets build the graph', Colors.YELLOW + Colors.UNDERLINE + Colors.BOLD)
    graph__test = HTMN_GRAPH("bases_4.json", 4)
    color_print('The graph is ready: Start bfs runs on the target vertices',
                Colors.YELLOW + Colors.UNDERLINE + Colors.BOLD)
    BFS__test = BFS(graph__test)
    counter = 1
    for target in graph__test.getTargetsVertices():
        BFS__test.run(target)
        BA_Vertex = graph__test.getOppositeVertex(target)
        color_print(f'Opposite Vertex dv = {BA_Vertex.dv}, {counter} Target vertices performed a bfs scan',
                    Colors.GREEN + Colors.BOLD)
        counter += 1
    color_print('The scan is complete.', Colors.YELLOW + Colors.UNDERLINE + Colors.BOLD)

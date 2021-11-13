# Written by : Mor & Tom & Hen & Niv

from queue import Queue


class BFS:

    def __init__(self, g):
        self.__graph = g

    def run(self, start):
        q = Queue()
        for vertex in self.__graph.getVertices(): # Reset all the distances first, and the boolean flags.
            vertex.setDistance(float('inf'))
            vertex.resetBooleanFlags()

        start.setDistance(0)
        q.put(start)
        while not q.empty():
            currentVertex = q.get()
            for neighbour in currentVertex.getValidNeighbours(): # This function need to return for us only the valid base that we can move to.
                if neighbour.getDistance() > currentVertex.getDistance() + 1:
                    neighbour.setDistance(currentVertex.getDistance() + 1)
                    q.put(neighbour)
                    neighbour.setParent(currentVertex)
        return 0


"""
 TODO:
 Validation of neighbors visitation status requires more work. Implementation pending graph, required methods will be implemented afterwards.
"""







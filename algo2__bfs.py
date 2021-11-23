# Written by : Mor & Tom & Hen & Niv

from queue import Queue
from Vertex import Vertex
from Graph import Graph
from vertex_neighbors import get_neighbours


class BFS:

    def __init__(self, g):
        self.__graph = g

    def run(self, start):
        """
        First we will reset the old values of the distances and the pi's fields [pi update temporarily removed],
        afterwards we will run the BFS methodology with the help of the 'Queue' data structure and will be assisted
        with the 'findDiffVec' method that we build that help us to determine if we can move forward to neighbour vertex.

        """
        q = Queue()
        self.resetGraph()

        start.set_dv(0)
        q.put(start)
        while not q.empty():
            currentVertex = q.get()
            for neighbour in currentVertex.near_lst:
                keyA, keyB = self.findDiffVec(currentVertex, neighbour)
                if neighbour.base_a[keyA] or neighbour.base_b[keyB]:
                    continue
                neighbour.base_a[keyA] = True
                neighbour.base_b[keyB] = True
                if neighbour.get_dv() > currentVertex.get_dv() + 1:
                    neighbour.set_dv(currentVertex.get_dv() + 1)
                    q.put(neighbour)
                    # neighbour.set_pi(currentVertex) TODO: Maybe in the future ...
        return 0

    def resetGraph(self):
        # Reset all the distances first, and the boolean flags.
        for vertex in self.__graph.vertex_lst:
            vertex.set_dv(float('inf'))
            # vertex.set_pi(0) TODO: Maybe in the future ...
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
        for vertex in self.__graph.vertex_lst:
            if vertex.get_dv() == d:
                res.append(vertex)
        return res


if __name__ == "__main__":
    baseA__test = {"0001": False, "0010": False, "0100": False, "1000": False}
    baseB__test = {"1011": False, "1101": False, "1110": False, "1111": False}
    # baseA__test = {"001": False, "010": False, "100": False}
    # baseB__test = {"011": False, "101": False, "110": False}
    graph_test = Graph(baseA__test, baseB__test, 4)
    graph_test.print_graph()
    # TODO :
    """
    המימוש תקין, השינוי של הדגלים מתרחש, הסריקה גם כן מתרחשת כמו שצריך, אבל יש בעיה כרגע במבנה נתונים של הגרף
    שהוא לא מייצר בכלל את כל הקודקודים. ראו דוג׳ ששמנו פה לשתי הדרכים לייצור הגרף
    בבסיס 4 אנחנו מקבלים בכלל גרף עם 2 קודקודים כולל הבסיס שהוכנס, ובדוג׳ השניה אנחנו מקבלים 5 קודקודים,
    כמו כן עבור בסיסים עם וקטורים זהים הבניה של הגרף נכשלת [ראו דוג׳ בסוף הפונקציה],
    הסריקה שבנינו צריכה לעבוד עם גרף מלא כפי שרן תיאר במצב הנוכחי שהוא גם כנראה לא תקין היא לא תעבוד.
    """

    # TODO: שימו לב שבדוג׳ הנוכחית יש לנו רק 2 קודקודים בגרף לכן הסריקה לא תעבוד
    print('starting..')
    graph__test = Graph(baseA__test, baseB__test, 4)
    print("We have only 2 vertex here read the print that come afterward:\n")
    graph__test.print_graph()
    BFS__test = BFS(graph__test)
    BFS__test.run(graph__test.vertex_lst[0])
    x = BFS__test.retAllVertexWithDistance(3)
    y = 2

    """
    דוג׳ לקריסה של הבנאי
    """
    badBuild_baseA = {"10": False, "01": False}
    badBuild_baseB = {"10": False, "11": False}
    try:
        graphCollapse = Graph(badBuild_baseA, badBuild_baseB, 2)
    except:
        print("Need To Be Fixed.")
    # graph__test = Graph(baseA__test, baseB__test, 4)
    # print("We have only 2 vertex here read the print that come afterward:\n")
    # graph__test.print_graph()
    # BFS__test = BFS(graph__test)
    # BFS__test.run(graph__test.vertex_lst[0])
    # x = BFS__test.retAllVertexWithDistance(3)
    # y = 2
    #
    # """
    # דוג׳ לקריסה של הבנאי
    # """
    # badBuild_baseA = {"10": False, "01": False}
    # badBuild_baseB = {"10": False, "11": False}
    # try:
    #     graphCollapse = Graph(badBuild_baseA, badBuild_baseB, 2)
    # except:
    #     print("Need To Be Fixed.")


class Graph:

    def __init__(self):
        self.adjancyList = {}

    def addVertex(self,vertex):
        if not self.adjancyList[vertex] :
            self.adjancyList[vertex] = [];



if __name__ == '__main__':
    g = Graph()

    g.addVertex('bala')




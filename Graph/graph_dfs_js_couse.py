class Graph:
    def __init__(self):
        self.adjacentList =  {}

    def addVertex(self,vertex):
        if vertex not in self.adjacentList:
            self.adjacentList[vertex] = []

    def addEdge(self,u,v):
        self.adjacentList[u].append(v)
        self.adjacentList[v].append(u)

    def removeEdge(self,u,v):

        self.adjacentList[u] = [x for x in self.adjacentList[u] if x != v ]
        self.adjacentList[v] = [x for x in self.adjacentList[v] if x != u ]

    def removeVertex(self,vertex):

        connectedVertex = self.adjacentList[vertex]

        # print(connectedVertex)

        del self.adjacentList[vertex]

        # print(self.adjacentList)

        for key , value in self.adjacentList.items():
            for i in value:
                if i  == vertex:
                    self.adjacentList[key].remove(i)


if __name__ == '__main__':

    g = Graph()

    g.addVertex('A')
    g.addVertex('B')
    g.addVertex('C')
    g.addVertex('D')
    g.addVertex('E')
    g.addVertex('F')

    g.addEdge('A','B')
    g.addEdge("A",'C')
    g.addEdge("B","D")
    g.addEdge("C","E")
    g.addEdge("D","E")
    g.addEdge("D","F")
    g.addEdge("E","F")

    print(g.adjacentList)


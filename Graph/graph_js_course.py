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

        # for key, value in self.adjacentList.items():
        #     for x in self.adjacentList[vertex]:
        #         if x == vertex:
        #             self.adjacentList[key].remove(x)



if __name__ == '__main__':

    g = Graph()
    g.addVertex(1)
    g.addVertex(2)
    g.addVertex(1)
    g.addVertex(3)
    print("the graph is")
    print(g.adjacentList)

    g.addEdge(1,2)
    g.addEdge(1,3)

    print(g.adjacentList)

    # g.removeEdge(1,2)
    g.removeEdge(1,3)

    print("after removing edges")
    print(g.adjacentList)

    g.removeVertex(2)

    print(g.adjacentList)

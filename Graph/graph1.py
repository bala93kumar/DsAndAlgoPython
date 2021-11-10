class Graph:

    def __init__(self,Nodes):
        self.nodes = Nodes
        self.adj_list = {}

        for i in self.nodes:
            self.adj_list[i] = []

    def printList(self):
        for i in self.nodes:
            print(i , "->", self.adj_list[i])


if __name__ == '__main__':

    nodes = ['a','b','c','d','e']
    g = Graph(nodes)

    g.printList()







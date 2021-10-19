class Node :
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enque(self, data):

        new_node = Node(data)

        if not self.first:
            self.first = new_node
            self.last = new_node
        else :
            self.last.next = new_node
            self.last = new_node

        self.size += 1

        return

    def deque(self):

        if self.first is None :
            return None
        else  :
            temp = self.first
            self.first = self.first.next
            self.size -= 1

    def printValues(self):

        currentNode = self.first

        while currentNode is not None :
            print(currentNode.data , end="-->")
            currentNode  = currentNode.next


if __name__ == '__main__':

    q1 = Queue()

    q1.enque(10)
    q1.enque(11)
    q1.enque(12)

    q1.printValues()

    q1.deque()

    print(end='\n')

    q1.printValues()
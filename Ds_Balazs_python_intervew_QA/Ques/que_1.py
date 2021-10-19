class Node :
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = None

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
        pass
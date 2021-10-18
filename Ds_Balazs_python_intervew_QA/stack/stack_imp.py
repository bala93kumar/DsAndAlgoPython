
class Node :
    def __init__(self, data):
        self.data = data
        self.next  = None


class Stack:

    def __init__(self):
        self.first = None
        self.size = 0

    def isEmpty(self):

        if self.first == None :
            return True
        else:
            return False

    def push(self, data):

        new_node = Node(data)

        current_node =  self.first

        if  not self.first:
            self.first = new_node
        else :

            new_node.next = self.first
            # self.first = new_node

        self.size += 1

        return

    def pop(self):




        poppedNode  =  self.first.data
        self.first = self.first.next

        self.size -= 1








    def printValues(self):

        current_node = self.first

        while current_node is not None:

            print(current_node.data)
            current_node = current_node.next


if __name__ == '__main__':

    stack_1 = Stack()

    print(stack_1.__dict__)

    stack_1.push(10)
    stack_1.push(11)
    # stack_1.push(12)
    # print(stack_1.size)
    #
    # # print(stack_1.last.data)
    #
    # stack_1.pop()
    # print(stack_1.size)
    #
    # stack_1.printValues()








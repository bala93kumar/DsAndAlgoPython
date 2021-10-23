class Node :
    def __init__(self,data):
        self.data = data
        self.next = None


class List :
    def __init__(self):
        self.head = None
        self.size = 0

    def insertLast(self,data):
        new_node = Node(data)

        if not self.head :
            self.head = new_node
        else:
            currentNode = self.head



            while currentNode.next is not None :
                currentNode = currentNode.next

            currentNode.next = new_node


    def print_obj_values(self):

        current_node = self.head


        while current_node is not None:

            print(current_node.data)

            current_node = current_node.next

        return

    def print_from_tail(self,head,position_from_tail):
        psr1 = head
        psr2 = head


        for i in range(position_from_tail):
            psr1 =  psr1.next

        while psr1.next is not None :
            psr2 =  psr2.next
            psr1  = psr1.next

        return psr2.data

    def hasCycle(self):

        visited = set()
        f = self.head

        while f :
            if  id(f) in visited:
                return 0
            else:
                visited.add(id(f))
                f = f.next
        return 0




if __name__ == "__main__":

    list1 = List()

    list1.insertLast(10)
    list1.insertLast(11)
    list1.insertLast(12)
    list1.insertLast(13)
    list1.insertLast(14)
    list1.insertLast(15)
    list1.insertLast(16)

    list1.print_obj_values()

    # 10->11-> 12-> 13-> 14-> 15->

    print("The the value at the position is  {}".format( list1.print_from_tail(list1.head, 2)))

    print( list1.hasCycle())





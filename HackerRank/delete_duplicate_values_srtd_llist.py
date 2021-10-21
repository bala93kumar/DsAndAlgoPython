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

            print(current_node.data, end="-->")

            current_node = current_node.next

        return

    def delete_duplicates(self):

        temp = self.head

        while temp.next is not None:
            if temp.data == temp.next.data:
                temp.next = temp.next.next
                temp = temp.next
            else :
                temp = temp.next

        return



if __name__  ==  '__main__':

    list1 = List()

    list1.insertLast(10)
    list1.insertLast(10)
    list1.insertLast(12)
    list1.insertLast(13)
    list1.insertLast(13)
    list1.insertLast(15)
    list1.insertLast(16)

    list1.print_obj_values()

    print('\n')

    list1.delete_duplicates()

    list1.print_obj_values()



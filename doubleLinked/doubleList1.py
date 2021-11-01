
def printList(head):

    currentNode = head

    while currentNode:
        print(currentNode.data , end=' ')
        currentNode = currentNode.next

def reverse(list):

    temp = None
    current = list

    while current is not None:
        temp = current.prev
        current.prev = current.next
        current.next = temp
        current = current.prev

    list = temp.prev

    while list is not None:
        print(list.data, end=' ')
        list = list.next




def insertSorted(list,data):

    prev = list
    next  = list.next


    newNode = Node(data)

    while next is not None :
        if data < prev.data:
            newNode.next = prev
            prev.prev = newNode
            list = newNode
            break
        elif data > prev.data and  data < next.data or data == next.data or data == prev.data:
            temp = prev.next
            prev.next = newNode
            newNode.next = temp
            break
        else:
            prev = prev.next
            next = next.next

    if data > prev.data:
        prev.next = newNode
        newNode.prev = prev

    currentNode = list
    while currentNode is not None:
        print(currentNode.data, end=' ')
        currentNode = currentNode.next



class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self,data):

        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail

        self.tail = newNode





if __name__ == '__main__':

    list1 = DoubleList()

    # list1.insert(1)
    list1.insert(2)
    list1.insert(3)
    list1.insert(5)

    printList(list1.head)

    print('\n')


    insertSorted(list1.head,6)

    print('\n')

    reverse(list1.head)


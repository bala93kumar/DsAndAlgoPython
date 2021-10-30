
def printList(head):

    currentNode = head

    while currentNode:
        print(currentNode.data , end=' ')
        currentNode = currentNode.next

def insertSorted(list,data):

    prev = list
    next  = list.next

    # print(prev.__dict__)
    # print(next.__dict__)

    newNode = Node(data)

    while next is not None :
        if data > prev.data and  data < next.data:
            temp = prev.next
            prev.next = newNode
            newNode.next = temp
            break
        else:
            prev = prev.next
            next = next.next

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

    list1.insert(1)
    list1.insert(3)
    list1.insert(4)

    printList(list1.head)

    print('\n')


    insertSorted(list1.head,2)


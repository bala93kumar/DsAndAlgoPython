import math
import os
import random
import re
import sys
#
# def print_singly_linked_list(node, sep, fptr):
#     while node:
#         fptr.write(str(node.data))
#
#         node = node.next
#
#         if node:
#             fptr.write(sep)

def merge_list(list1,list2,mergedList):

    if list1.head.data < list2.head.data:
        currentFirst= list1.head
        mergedList.head  = list1.head
    else :
        mergedList.head = list2.head


    print(mergedList.head.__dict__)
    print(mergedList.head.next.__dict__)


    # 1 -> 3-> -> 5
    #
    # 2 -> 4





def merge_list_old(list1, list2, mergedList):
    currentFist = list1.head
    currentSecond =  list2.head

    while True:
        if currentFist is None:
            mergedList.insert_node_last(currentSecond.data)
            break
        if currentSecond is None:
            mergedList.insert_node_last(currentFist.data)
            break
        if currentFist.data <= currentSecond.data:
            currentFirstNext = currentFist.next
            currentFist.next = None
            mergedList.insert_node_last(currentFist.data)
            currentFist = currentFirstNext
        else :
            currentSecondNext = currentSecond.next
            currentSecond.next = None
            mergedList.insert_node_last(currentSecond.data)
            currentSecond = currentSecondNext




class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node_last(self, data):

        new_node = Node(data)

        if self.head == None:
            self.head = new_node
        else:
            self.tail.next = new_node

        return

    def print_obj_values(self):

        current_node = self.head


        while current_node is not None:

            print(current_node.data)

            current_node = current_node.next

        return






class Node :
    def __init__(self, data):
        self.data = data
        self.next = None





if __name__ == '__main__':

    list_1 = SinglyLinkedList()

    list_1.insert_node_last(1)
    list_1.insert_node_last(3)
    list_1.insert_node_last(5)

    # list_1.print()

    # print(list_1.head.next.__dict__)

    list_1.print_obj_values()

    print("list 2------------------")

    list_2 = SinglyLinkedList()

    # list_2.insert_node_last(1)
    list_2.insert_node_last(2)
    list_2.insert_node_last(4)

    list_2.print_obj_values()

    print("------------------------------")

    list_3 = SinglyLinkedList()

    merge_list(list_1, list_2, list_3)
    #
    # list_3.print_obj_values()

    # print(list_3.__dict__)
    # print(list_3.__dict__)


    print(list_1.head.data)

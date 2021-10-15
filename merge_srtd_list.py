import math
import os
import random
import re
import sys

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def print_obj_value(node):

    while node is not None:
        print(node.data)
        node = node.next

def mergeList(head1, head2):
    if head1 is None :
        print(head2)

    if head2 is None:
        print(head1)

    if head1.data <= head2.data:
        head =  head1
        head1 = head1.next

    if head2.data <= head1.data:
        head = head2
        head2 = head2.next

    current = head

    while head1 != None  and head2 != None :
        if head1.data <=  head2.data:
            head.next  = head1
            head1 = head1.next
        else :
            head.next = head2
            head2 = head2.next

    return



class Node :
    def __init__(self, data):
        self.data = data
        self.next = None



class   SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def  insert_node_last(self, data):

        new_node = Node(data)

        if self.head == None:
            self.head = new_node
        else :
            self.tail.next = new_node


        self.tail =  new_node

        return

    def print(self):

        current_node = self.head

        while current_node is not None :

            print(current_node.data)

            current_node = current_node.next

        return

    def print_obj_value(self):

        current_node = self.head

        while current_node  is not None :
            print(current_node.__dict__)
            current_node = current_node.next

        return




if __name__ == '__main__':

    list_1 =  SinglyLinkedList()

    list_1.insert_node_last(1)
    list_1.insert_node_last(3)
    list_1.insert_node_last(5)

    list_1.print()

    # print(list_1.head.next.__dict__)

    list_1.print_obj_value()

    print("list 2------------------")

    list_2 = SinglyLinkedList()

    list_2.insert_node_last(1)
    list_2.insert_node_last(2)
    list_2.insert_node_last(4)

    list_2.print()



    list_3 = Node(mergeList(list_1.head, list_2.head))

    print_obj_value(list_3)

from collections import deque

def inorder(root):

    if root is None:
        return

    if root:
        inorder(root.left)
        print(root.element, end=' ')
        inorder(root.right)

def isempty(queue):

    if  len(queue) > 0:
        return False
    else :
        return True


def levelOrder(root):

    if root is None:
        return None

    q = deque()
    q.append(root)
    # result = isempty(q)

    while q:
        print('in while')
        t = q.popleft()
        if t.left:
            print(t.left.element)
            q.append(t.left)
        if t.right:
            print(t.right.element)
            q.append(t.right)












class Node:
    __slots__ = 'element','left','right'

    def __init__(self,data):
        self.element = data
        self.left = None
        self.right = None

class Tree:

    def __init__(self):

        self.root = None

    def makeTree(self,data):

        if self.root is None:
            self.root = Node(data)
            return

        if self.root.element == data:
            return None


        if data < self.root.element:
            if self.root.left:
                self.root.left.makeTree(data)
            else:
                self.root.left = Node(data)
        elif data > self.root.element:
            if self.root.right:
                self.root.right.makeTree(data)
            else:
                self.root.right = Node(data)





if __name__ == '__main__':

    bst1 = Tree()
    bst1.makeTree(10)
    bst1.makeTree(5)
    bst1.makeTree(15)

    inorder(bst1.root)

    print('\n')
    levelOrder(bst1.root)

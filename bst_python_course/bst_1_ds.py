from collections import deque


def height(root):


    if root:
        x = height(root.left)
        y = height(root.right)

        if x > y:
            return x + 1
        else:
            return y + 1

    return 0

def inorder(root):

    if root is None:
        return

    if root:
        inorder(root.left)
        print(root.element, end=' ')
        inorder(root.right)


def count_ite(root):

    if root is None:
        return None

    q = deque()
    q.append(root)
    count = 0

    while len(q) > 0:
        t = q.popleft()

        if t.right is not None and t.left is not None:
            count = count + 1

        if t.right is not None:
            q.append(t.right)

        if t.left is not None:
            q.append(t.left)
    return count

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

    # print(len(q))

    while len(q) > 0:
        t = q.popleft()
        print(t.element)
        if t.left:
            # print(t.left.element)
            q.append(t.left)
        if t.right:
            # print(t.right.element)
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

    print(count_ite(bst1.root))

    print(height(bst1.root) - 1)

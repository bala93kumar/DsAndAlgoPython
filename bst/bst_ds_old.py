from collections import deque

class Node :
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def swap()


def lca1(p,q,root):

    if root is None:
        return None

    while root:
        if p > root.data and q  > root.data :
            root = root.right
        elif p < root.data and q <root.data:
            root = root.left
        else :
            break

    return  root



def lca(p,q,root):

    if root is None:
        return None

    if root.data == p or root.data == q:
        return root

    left = lca(p,q,root.left)
    right = lca(p,q,root.right)

    if left is not None and right is not None:
        return root

    if left is not None:
        return left
    else :
        return right







def vertical_order(root):
    if root is not None:
        dict = {}
        node_dict = {}
        que = list()
        que.append(root)
        node_dict[root.data] = 0
        while len(que) > 0:
            temp = []
            curr = que.pop(0)
            if curr is not None:
                level = node_dict[curr.data]
                if level in dict:
                    temp = dict.get(level)
                    temp.append(curr.data)
                else:
                    temp.append(curr.data)
                    dict[level] = temp

                if curr.left is not None:
                    left_node = curr.left
                    que.append(left_node)
                    node_dict[left_node.data] = node_dict[curr.data] - 1
                if curr.right is not None:
                    right_node = curr.right
                    que.append(right_node)
                    node_dict[right_node.data] = node_dict[curr.data] + 1
        print(dict)


def verticalOrder_1(root):

    if root is None:
        return

    d = {}
    q = deque()

    q.append((root,0))

    # print(q)

    while len(q) > 0:

        node,dist = q.popleft()
        d.setdefault(dist,[]).append(node.data)

        if node.left:
            q.append((node.left, dist -1))

        if node.right:
            q.append((node.right, dist + 1))

    #print vertical order
    # for i in sorted(d.items()):
    #     print(i)

    #print top view
    for i in sorted(d.keys()):
        print(d[i][0])

def height(root):

    if root is None:
        return 0

    if root.left is None and root.right is None:
       return 0
    elif root.left is not None and root.right is None:
        return 1 + height(root.left)
    elif root.right is not None and root.left is  None:
        return 1 + height(root.right)
    else :
        return 1 + max(height(root.left), height(root.right))

def inorder(root):

    if root is None:
        return None

    if  root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)


def preorder(root):

    if root is None:
        return None

    if root:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.right)

def postorder(root):

    if root is None:
        return

    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=' ')


def find(root, value):

    if root is None:
        print('No values found')
        return

    if root.data == value:
        print(root.data)
        return
    else :
         if value < root.data:
             root = root.left
             find(root, value)
         else :
             if value > root.data:

                root = root.right
                find(root, value)

def find_new(root, value):
    if root :
        if root.data == value:
            return True
        elif value < root.data :
            return find_new(root.left ,value)
        elif value > root.data:
            return find_new(root.right,value)
    else :
        return False



    
class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):

        new_node= Node(data)

        if not self.root:
            self.root = new_node
            return
        else :
            currentNode = self.root

            while True:
                if  currentNode.data  == new_node.data:
                    return None
                if new_node.data < currentNode.data:
                    if not currentNode.left :
                        currentNode.left = new_node
                        return
                    else:
                        currentNode = currentNode.left
                else :
                    if new_node.data > currentNode.data:
                        if not currentNode.right:
                            currentNode.right = new_node
                            return
                        else :
                            currentNode = currentNode.right

    #following recursive insert failed

    # def recursive_insert(self, data):
    #
    #     if self.root is None :
    #         self.root = Node(data)
    #         return
    #     if self.root.data == data:
    #         return
    #     if data > self.root.data:
    #         if self.root.right:
    #             self.root.right.recursive_insert(data)
    #         else:
    #             self.root.right = Node(data)
    #     elif data < self.root.data:
    #         if self.root.left:
    #             self.root.left.recursive_insert(data)
    #         else:
    #             self.root.left = Node(data)





if __name__ == '__main__':


    bst1 = BST()
    bst1.insert(10)
    bst1.insert(5)
    bst1.insert(13)
    bst1.insert(11)
    bst1.insert(12)
    bst1.insert(2)
    # bst1.insert(2)

    inorder(bst1.root)
    print('\n')
    preorder(bst1.root)
    print('\n')
    postorder(bst1.root)
    print('\n')
    print(find(bst1.root,17))
    print('\n')
    print(find_new(bst1.root, 5))

    bst2 = BST()

    bst2.insert(10)
    bst2.insert(5)
    bst2.insert(13)
    bst2.insert(14)

    inorder(bst2.root)

    print('\n')

    print(height(bst2.root))

    print('\n')

    verticalOrder_1(bst1.root)

    print(lca(5,13,bst2.root))

    print('\n')

    print('lca new method')

    bst3 = BST()

    bst3.insert(20)
    bst3.insert(8)
    bst3.insert(22)
    bst3.insert(4)
    bst3.insert(12)
    bst3.insert(10)
    bst3.insert(14)

    print("preorder bst3")

    preorder(bst3.root)

    print('\n', 'inorder')

    inorder(bst3.root)

    print('\n')

    returnd_root  = lca1(10,22,bst3.root)

    print(returnd_root.data)

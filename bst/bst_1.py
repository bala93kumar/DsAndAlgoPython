class Node :
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):

    if  root is None:
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





if __name__ == '__main__':


    bst1 = BST()
    bst1.insert(10)
    bst1.insert(5)
    bst1.insert(13)
    bst1.insert(11)
    bst1.insert(2)
    bst1.insert(2)

    inorder(bst1.root)
    print('\n')
    preorder(bst1.root)
    print('\n')
    postorder(bst1.root)
    print('\n')
    print(find(bst1.root,17))



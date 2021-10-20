class Node :
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


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
    print(bst1.root.__dict__)



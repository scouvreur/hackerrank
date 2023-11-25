class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# left -> root -> right
def inOrder(root):
    if root.left:
        preOrder(root.left)
    print(root.info, end=" ")
    if root.right:
        preOrder(root.right)


# root -> left -> right
def preOrder(root):
    print(root.info, end=" ")
    if root.left:
        preOrder(root.left)
    if root.right:
        preOrder(root.right)


# left -> right -> root
def postOrder(root):
    if root.left:
        preOrder(root.left)
    if root.right:
        preOrder(root.right)
    print(root.info, end=" ")

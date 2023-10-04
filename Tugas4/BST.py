class Node:
    def __init__(self,root):
        self.root = root
        self.left = None
        self.right = None

def insert(node,root):

    if node is None:
        return Node(root)

    if root < node.root:
        node.left = insert(node.left, root)
    elif root > node.root:
        node.right = insert(node.right, root)

    return node

def inorder(node):
    if node:
        inorder(node.left)
        print(node.root,end=" ")
        inorder(node.right)

r = Node(50)
r = insert(r,30)
r = insert(r,20)
r = insert(r,40)
r = insert(r,70)
r = insert(r,60)
r = insert(r,80)

inorder(r)


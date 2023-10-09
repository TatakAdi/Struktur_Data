class Node:
    def __init__(self,root):
        self.root = root
        self.left = None
        self.right = None

def insert(node,root):
    if isinstance(root, int):
        if node is None:
            return Node(root)
        if root < node.root:
            node.left = insert(node.left, root)
        elif root > node.root:
            node.right = insert(node.right, root)
        return node
    else:
        raise IndexError ("Masukkan data bertipe interger")

def Preorder(node):
    if node:
        print(node.root,end=" ")
        Preorder(node.left)
        Preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.root,end=" ")
        inorder(node.right)

def Postorder(node):
    if node:
        Postorder(node.left)
        Postorder(node.right)
        print(node.root,end=" ")
    else : 
        return "Ini bukan BST"

def remove(node,k):
    if node is None:
        return node
    if k < node.root:
        node.left = remove(node.left,k)
        return node
    elif k > node.root:
        node.right = remove(node.right, k)
        return node

    if node.left is None:
        temp = node.right
        del node
        return temp
    elif node.right is None:
        temp = node.left
        del node
        return temp
    else:
        suksesor = node

        succ = node.right
        while succ.left is not None:
            suksesor = succ
            succ = succ.left

        if suksesor != node:
            suksesor.left = succ.right
        else:
            suksesor.right = succ.right
        
        node.root = succ.root

        del succ
        return node

def order(root):
    print("BST saat Preorder : ")
    Preorder(root)
    print("\nBST saat inorder : ")
    inorder(root)
    print("\nBST saat Postorder : ")
    Postorder(root)

r = None
r = insert(r,50)
r = insert(r,30)
r = insert(r,20)
r = insert(r,40)
r = insert(r,70)
r = insert(r,60)
r = insert(r,80)
r = insert(r,35)
r = insert(r,65)
r = insert(r,90)

order(r)

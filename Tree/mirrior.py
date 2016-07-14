# Python Program to find the size of binary tree
 
# A binary tree node
class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None
 
# Computes the number of nodes in tree
def mirror(root):
    if root is None:
        return None
    else:
        root1 = root
        left = root.left
        right = root.right
        root1.left = mirror(right)
        root1.right = mirror(left)
    return root1     
 
 
def preorder(root):
    if not root:
        return
    print root.data,
    preorder(root.left)
    preorder(root.right)

# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left  = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.left.left.left = Node(7)

preorder(root)
root1 = mirror(root)
#preorder(root)
print ""
preorder(root1)
#print root1.data, root1.left.data, root1.right.data


# Python Program to find the size of binary tree
 
# A binary tree node
class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None
 
# Computes the number of nodes in tree
def height(node):
    if node is None:
        return 0
    else:
        return max(height(node.left) + 1, height(node.right) + 1)
 
 
# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left  = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.left.left.left = Node(7)
 
print "Height of the tree is %d" %(height(root))

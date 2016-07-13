# Python Program to find the size of binary tree
 
# A binary tree node
class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.val = data 
        self.left = None
        self.right = None
 
def check(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif (root1 is None and root2 is not None) or (root1 is not None and root2 is None):
        return False
        
    return root1.val==root2.val and check(root1.left, root2.left) and check(root1.right, root2.right)

 
 
# Driver program to test above function
#input 1
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left  = Node(4)
root1.left.right = Node(5)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left  = Node(4)
 
print  check(root1, root2)

#input 2
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
root1.left.left.left = Node(6)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)
root2.left.left.left = Node(6)

print  check(root1, root2)

# input 3
root1 = Node(None)
root2 = Node(None)
print check(root1, root2)


class Node:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left  = None

def min_depth(root):
    if not root.left and not root.right:
        return 1
    if not root.left:
        return  min_depth(root.right) + 1
    if not root.right:
        return min_depth(root_.left) + 1
    return min(min_depth(root.left) + 1, min_depth(root.right) + 1)    


'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)        
'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)

print min_depth(root)

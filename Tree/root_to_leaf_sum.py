class Node:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left  = None

def path(root, path_sum):
    if not root.left and not root.right:
        print path_sum+ root.val
        return    
    if root.left:
        path(root.left, path_sum+root.val)  
    if root.right:
        path(root.right, path_sum+root.val)      
          
          

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

print path(root, 0)


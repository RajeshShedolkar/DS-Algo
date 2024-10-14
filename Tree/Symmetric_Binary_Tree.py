# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
'''
    1
   / \
  2   2     
 / \ / \
3  4 4  3
The above binary tree is symmetric. 
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def mirror(A, B):
    if A is None and B is None:
        return 1
    elif (A is None and B) or (A and B is None):
        return 0
    return A.val==B.val and mirror(A.left, B.right) and mirror(A.right, B.left)   

def isSymmetric(A):
   return mirror(A.left, A.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print isSymmetric(root) and True



root =  TreeNode(1)
root.left =  TreeNode(2)
root.right =  TreeNode(3)

print isSymmetric(root)

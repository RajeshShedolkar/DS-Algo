
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print root.val,
    inorder(root.right)       

root = TreeNode(5)

root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
        
inorder(root)        

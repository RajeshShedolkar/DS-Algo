
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

def preorder(root):
    if not root:
        return
    print root.val,
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print root.val,

root = TreeNode(5)

root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

print "Inorder"        
inorder(root)
print "\nPreorder"
preorder(root)
print "\nPostorder"
postorder(root)

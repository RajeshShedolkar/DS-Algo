class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isValidBST(self, node):
    return int(self.checkBST(node, float('-inf'), float('inf')))

def checkBST(self, node, lower, upper):
    if node is None:
        return True

    return (lower < node.val < upper and
            self.checkBST(node.left, lower, node.val) and
            self.checkBST(node.right, node.val, upper))




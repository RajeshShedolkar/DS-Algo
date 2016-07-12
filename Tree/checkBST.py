class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isValidBST(node):
    return int(checkBST(node, float('-inf'), float('inf')))

def checkBST(node, lower, upper):
    if node is None:
        return True

    return (lower < node.val < upper and
            checkBST(node.left, lower, node.val) and
            checkBST(node.right, node.val, upper))


root = Node(2)
root.left = Node(1)
root.right = Node(3)
print isValidBST(root)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left  = None

def inorder(A):
    stack = []
    ret = []
    curr = A
    done = 0
    while not done:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            if len(stack)>0:
                curr = stack.pop()
                ret.append(curr.val)
                curr = curr.right
            else:
                done = 1
    return ret


def bst(A):
    n = len(A)
    if not A:
        return None
    if len(A)==1:
        root = TreeNode(A[n/2])
        return root
    mid = n/2    
    node = TreeNode(A[n/2])
    node.left = bst(A[0:mid])
    node.right = bst(A[mid+1:])
    return node

A = [1, 2, 3, 4, 5, 6, 7] 
root = bst(A)
print inorder(root)


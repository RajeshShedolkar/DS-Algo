class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print inorder(root)

class Node:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left  = None

def vertical(root, dis, d):
    if not root:
        return d
    if dis not in d:
        d[dis] = [root]
    else:
        d[dis] = d[dis] + [root]
    if root.left:
        vertical(root.left, dis-1, d)
    if root.right:
        vertical(root.right, dis+1, d)
    return d          


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
print "Vertical order traversal is"



ret = vertical(root, 0, {})
t = sorted(ret)

for i in t:
    for node in ret[i]:
        print node.val,
    print ""     

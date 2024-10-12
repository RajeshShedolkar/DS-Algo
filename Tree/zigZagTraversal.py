# Python Program to traverse a binary
# tree in zigzag manner.

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

# function to print the zigzag traversal
def zigZagTraversal(root):
    
    ans = []
    
    # if null then return
    if root is None:
        return ans

    # declare two stacks
    currentLevel = []
    nextLevel = []

    # push the root
    currentLevel.append(root)

    # check if stack is empty   
    leftToRight = True
    while currentLevel:
        
        size = len(currentLevel)
        
        while size > 0:
            size -= 1
            
            # pop out of stack
            curr = currentLevel.pop()
    
            # push the current node 
            ans.append(curr.data)
    
            # store data according to current
            # order.
            if leftToRight:
                if curr.left:
                    nextLevel.append(curr.left)
                if curr.right:
                    nextLevel.append(curr.right)
            else:
                if curr.right:
                    nextLevel.append(curr.right)
                if curr.left:
                    nextLevel.append(curr.left)
        
        leftToRight = not leftToRight
        currentLevel, nextLevel = nextLevel, currentLevel
    
    return ans

def printList(v):
    for i in v:
        print(i, end=" ")
    print()

if __name__ == "__main__":

    # Create a hard coded tree.
    #         20
    #       /   \
    #      8     22
    #    /  \     \
    #   4   12    11
    #      /  \
    #     10   14
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.right.right = Node(11)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    
    ans = zigZagTraversal(root)
    printList(ans)

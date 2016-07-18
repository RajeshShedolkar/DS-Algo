from collections import deque

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def level(A):
    stack = Queue()
    stack.enqueue(A)
    curr = A
    done = 1
    while done:
        if stack:
            curr = stack.dequeue()
            print curr.val,
        if curr.left:
            stack.enqueue(curr.left)
        if curr.right:
            stack.enqueue(curr.right)
        if not stack.size():
            done = 0 
                  

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

#print inorder(root)
print level(root)

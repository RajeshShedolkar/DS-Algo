class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def rev(A):
    if A.next is None:
        head = A
        return head
    head = rev(A.next)
    prev = A.next
    prev.next = A
    A.next = None
    return  head

Head = Node(1) 
Head.next = Node(2)
Head.next.next = Node(3)
Head.next.next.next = Node(4)

B  = rev(Head)           
while B:
    print B.val,
    B = B.next     

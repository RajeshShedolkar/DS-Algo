class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverse(A):
    if A.next is None:
        head = A
        return head
    head = reverse(A.next)
    prev = A.next
    prev.next = A
    A.next = None
    return head   

A = ListNode(1)
A.next = ListNode(2)
A.next.next = ListNode(3)
print "Before"
a = A
while a:
    print a.val,
    a = a.next
print "\nAfter"
B = reverse(A)

while B:
    print B.val,
    B = B.next

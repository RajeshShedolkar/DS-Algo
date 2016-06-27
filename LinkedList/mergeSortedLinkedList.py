# merge two sorted linked list
# Node
# Input
# A = 1-->6-->9-->null
# B = 2-->3-->4-->10-->null
#Output
# 1 --> 2 --> 3 --> 4 --> 6 --> 9 --> 10 --> null
class ListNode:
    def  __init__(self, x):
        self.val = x
        self.next = None

def merge(A, B):
    dummy = ListNode(0)
    dummy_head = dummy

    while A and B:
        if A.val> B.val:
            dummy.next = B
            dummy = dummy.next
            B = B.next
        else:
            dummy.next = A
            dummy = dummy.next
            A = A.next
    if A is not None:
        dummy.next = A
    if B is not None:
        dummy.next = B
    dummy = dummy_head.next
    while dummy is not None:
        print dummy.val,'-->',
        dummy = dummy.next             
    print 'null'

A = ListNode(1)
B = ListNode(2)
A1 = [6,9]
B1 = [3,4,10]
Ahead = A
Bhead = B
for a in A1:
    A.next = ListNode(a)
    A = A.next
for b in B1:
    B.next = ListNode(b)
    B = B.next
merge(Ahead, Bhead)
#a=Bhead
#while a is not None:
#    print a.val
#    a=a.next

#print A.val        


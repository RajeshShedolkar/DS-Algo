class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# REVERSE Function
def reverse(A):
    a = None
    b = A
    c = A.next
    while c is not None:
        b.next = a
        a = b
        b = c
        c = c.next
    b.next = a
    a = b
    return a


def reorder(A):
    a = A
    b = A
    if  not a or not a.next :
        return A
    while b.next and b.next.next:
        a = a.next
        b = b.next.next
    b = a.next
    a.next = None
    b = reverse(b)
    a = A
    a_dummy = None
    b_dummy = None
    retHead = ListNode(0)
    dummy = retHead
    bHead = b
    while b:
        a_dummy = a
        a = a.next
        b_dummy = b
        b = b.next
        dummy.next = a_dummy
        dummy = dummy.next
        dummy.next = b_dummy
        dummy = dummy.next
    if a:
        dummy.next = a  
    
    return retHead.next


#------------------------------------------------------------------
#------  ---- -- INPUT --  --- ----------
A = [1, 2, 3, 4, 5]

dummy = ListNode(None)
Ahead = dummy
for a in A:
    Ahead.next = ListNode(a)
    Ahead = Ahead.next

#print A
p = dummy.next
dummy = dummy.next

while dummy is not None:
    print dummy.val, '-->',
    dummy = dummy.next
print 'null'
s = reorder(p)
#print palindrome(p)

while s:
    print s.val,
    s = s.next

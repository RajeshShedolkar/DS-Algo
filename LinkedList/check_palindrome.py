class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        

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

def palindrome(A):
    B = A
    a = A
    count = 0
    while a:
        count+=1
        a = a.next
    count = int(count/2)
    a = A
    while count>1:
        a = a.next
        count-=1
    B = a    
    B = reverse(B)
    while A:
        if A.val != B.val:
            return 0  
        A = A.next
        B = B.next
    return 1

#------------------------------------------------------------------
#------  ---- -- INPUT --  --- ----------
A = [1,1,2,1,1]

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

print palindrome(p)


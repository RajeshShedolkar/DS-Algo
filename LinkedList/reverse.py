# Delete Duplicates from linked list

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Example[1 1 2 3 3]
#reverse linked list
#------------------------------------------
#-------------------------------------------
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

#------------------------------------    
A = [1,1,2,3,3]

dummy = ListNode(None)
Ahead = dummy
for a in A:
    Ahead.next = ListNode(a)
    Ahead = Ahead.next

print A
p = dummy.next
dummy = dummy.next

while dummy is not None:
    print dummy.val, '-->',
    dummy = dummy.next
print 'null'


a =  reverse(p)

while a is not None:
    print a.val,
    a = a.next

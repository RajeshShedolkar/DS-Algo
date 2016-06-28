# Delete Duplicates from linked list

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Example[1 1 2 3 3]

def deleteDuplicates(A):
    head = A
    while A:
        while A.next and A.next.val == A.val:
            A.next = A.next.next
        A = A.next
    return head      
def delete(A):
    dummy = ListNode(None)
    test = ListNode(None)
    dummyHead = test
    
    while A is not None:
        if dummy.val != A.val:
            test.next = ListNode(A.val)
            test = test.next
        dummy = A
        A = A.next
    return dummyHead.next 

A = [1,1,2,3,3]

dummy = ListNode(None)
Ahead = dummy
for a in A:
    Ahead.next = ListNode(a)
    Ahead = Ahead.next
    
dummy = deleteDuplicates(dummy.next)
#dummy = delete(dummy.next)
print A
while dummy is not None:
    print dummy.val,'-->',
    dummy = dummy.next
print 'null'

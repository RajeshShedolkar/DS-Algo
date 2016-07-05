class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def detect(A):
    slow = A.next
    fast = A

    while slow!=fast:
        print slow.val,
        slow = slow.next
        fast = fast.next.next
    print slow.val, fast.val
    count = 1
    slow = slow.next
    dummy = A
    
    '''
    while fast!=slow:
        count +=1
        slow = slow.next
        dummy = dummy.next
    '''
#------------------------------------------------------------------
#------  ---- -- INPUT --  --- ----------

Ahead = ListNode(1)
dummy = Ahead
dummy.next = ListNode(2)
dummy.next.next = ListNode(3)
a = dummy.next.next
dummy.next.next.next = ListNode(4)
dummy.next.next.next.next = ListNode(5)
dummy.next.next.next.next.next = a
p = Ahead
print p.val, p.next.val, p.next.next.val, p.next.next.next.next.next.val
s = detect(p)


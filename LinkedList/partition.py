# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

def partition(head, x):
    if not head:
        return None

    less, greaterEqual = ListNode(0), ListNode(0)
    tempLess, tempGreaterEqual, temp = less, greaterEqual, head
    while temp:
        if temp.val < x:
            tempLess.next = temp
            tempLess = tempLess.next
        else:
            tempGreaterEqual.next = temp
            tempGreaterEqual = tempGreaterEqual.next

        cur = temp
        temp = temp.next
        cur.next = None

    tempLess.next = greaterEqual.next
    return less.next 

A = ListNode(4)
A.next = ListNode(5)
A.next.next = ListNode(2)
A.next.next.next = ListNode(3)
A.next.next.next.next = ListNode(7)
A.next.next.next.next.next = ListNode(1)
B = partition(A, 4)
a = B
while a:
    print a.val,
    a = a.next

import sys
def second_max(A, k):
    first = second = -1*sys.maxint
    for a in A[0:3]:
        if first<a:
            second = first
            first = a
        if second < a and a != first:
            second = a
    print  second , first
    ret = []
    ret.append(first)

    
    
A = [1,2,3,4,5,6]

second_max(A, 3)

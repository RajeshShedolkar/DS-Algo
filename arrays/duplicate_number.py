# number from numbers only from  0 t0 n-1

def find_duplicate(A):
    for i in range(len(A)):
        if A[abs(A[i])] > 0:
            A[abs(A[i])]= -A[abs(A[i])]
        else :
            return abs(A[i])         
    return 0

A = [3, 2, 3, 1, 1]


print find_duplicate(A)

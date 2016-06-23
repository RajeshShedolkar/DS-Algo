# find triplet
# this solution has O(n*n) time complexity
# idea is to sort all elements and square each element
def Triplet(A):
    A.sort()
    # A contains sorted square element
    A = [x*x for x in A]

    n = len(A)-1
    # start with biggest element and use this as sum of other two side's square
    while n>0:
        X = A[n]
        start=0
        end = n-1
        # this is simple pbm of finding of pair for given sum
        # here we are looking for X number
        while start<end:
            if A[start]+A[end]==X:
                return True
            if A[start]+A[end]<X:
                start+=1
            else:
                end-=1
        n-=1 
    return False
    
    
A = [3, 1, 4, 6, 5]
print Triplet(A)

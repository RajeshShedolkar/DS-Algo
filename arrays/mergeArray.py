# merging two arrays in O(1) space
def merge(A, B):
    m = len(A)
    n = len(B)
    i,j=m-1,0
    while i>=0 and j<n:
        if A[i]>B[j]:
            A[i],B[j] = B[j],A[i]
            i-=1
            j+=1
        else: # at certain point there is no need to comapre since arrays are sorted
            break    
    A.sort()
    B.sort()
    return A,B
    
A = [1, 5, 9, 10, 15, 20]
B = [2, 3, 8, 12, 13]
          
print merge(A, B)                

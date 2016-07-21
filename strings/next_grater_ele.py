
def next(A):
    n = len(A)
    i=n-1
    c = A[-1]
    index = -1
    while i>0:
        if c > A[i]:
            index = i
            break
        i = i-1        
             
    A = list(A)      
    if index:
        A[index], A[-1] = A[-1], A[index]
        A = A[:index + 1] + sorted(A[index + 1:])      
    
    return ''.join(A)

print '1398'
print next('1398')        

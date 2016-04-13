def maxDef(A):
    max=0
    i,j=0,1
    distance = 0
    for j in range(1, len(A)):
        #distance=0
        while j<len(A) and A[j]-A[i]>=0:
            distance = distance + A[j]-A[i]
            j+=1
        if j<len(A) and A[j]-A[i]<0:
            i=j
            distance = 0
        if max<distance:
            max = distance
    
    return max

A = [ 7, 9, 5, 6, 3, 2 ]

A =  [2, 3, 10, 6, 4, 8, 1]

print maxDef(A)

def rearrange(A):
    temp = A[0]
    i=0
    n = len(A)
    while temp>0:
        # save the previous value in temp and find out next index for current index
        j = (2*i+1) if n/2 > i else 2*(n-1-i)

        

        temp,A[j]=A[j],temp
        A[j] = -A[j]
        i=j

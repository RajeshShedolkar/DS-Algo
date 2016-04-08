def findPairs(A, sum):
    count = 0
    counti = 1
    countj = 1
    i,j = 0,len(A)-1
    while i<j:
        if A[i]+A[j]==sum:
            while A[i]==A[i+1]  and i+1<j:
                counti+=1
                i+=1
            while A[j]==A[j-1] and i<j:
                countj+=1
                j-=1
            #print i,j  if all elements are same then i=j
            if i==j:
                count = (len(A)-1)*len(A)/2
            else:
                count = count + counti*countj
                counti,countj=1,1
                i+=1
                j-=1
        elif A[i]+A[j]>sum:
            j-=1
        elif A[i]+A[j]<sum:
            i+=1
    return count
#these all are edge cases
A = [-1, 0, 0, 1, 1, 1, 2, 3, 4, 4, 5, 9, 10]
# A = [1,1,1,4,4]
# A = [2, 2, 2, 2]
# A = [1, 2, 3, 4, 5]
# A = [1,2,3,4]
# A = [2, 2, 2, 3]
# A = [1,4,4,4]
print findPairs(A, 5)

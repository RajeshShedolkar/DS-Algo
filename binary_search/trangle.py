def no_of_trangle(A):
    A.sort()
    low = 0
    high = len(A)-1
    total, index=0, 0
    for i in range(0, len(A)-2):
        for j in range(i+1, len(A)-1):
            low = j+1
            high = len(A)-1
            index = j
            while low<=high and low>j:
                mid = (low+high)/2
                if A[i]+A[j]>A[mid]:
                    index = mid
                    low = mid+1
                else:
                    high = mid-1
            total = total+index-j
    return total

A = [1, 3, 4, 5]
A = [3,1,5,4]
A = [1, 2, 2, 2, 3, 7, 8]
print no_of_trangle(A)

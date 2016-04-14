def search(A):
    low = 0
    high = len(A)-1
    N = len(A)
    while low<=high:
        mid = (low+high)/2
        prev = (mid-1+N)%N
        next = (mid+1+N)%N
        if A[low]<=A[high]:
            return low
        elif A[mid]<=A[prev] and A[mid]<=A[next]:
            return mid
        elif A[mid] < A[high] :
            high = mid-1
        else:
            low = mid+1

A = [7, 9, 10, 13, 1, 2, 3]
A = [1,2,3]
A = [3]
A = [3,2]
print A," :@index",search(A),", minimum element",A[search(A)]   
#search(A)

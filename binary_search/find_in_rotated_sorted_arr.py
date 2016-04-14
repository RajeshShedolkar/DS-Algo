def find_min(A):
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
        elif A[mid]<A[high]:
            high = mid-1
        else:
            low = mid+1


def search(A, X, low, high):
    while low<=high:
        mid = (low+high)/2
        if A[mid]==X:
            return 1 
        elif A[mid]>X:
            high = mid-1
        else:
            low = mid+1             
    return -1

def search_element(A, X):
    min_index = find_min(A)
    low = 0
    high = len(A)-1
    if A[min_index]<= X and X<= A[high]:
        low = min_index
        high = len(A)-1
        return search(A, X, low, high)
    else:
        low=0
        high = min_index -1
        return search(A, X, low, high)      
            
A = [2, 3, 1]
A = [4]
X = 56
A = [12,14,56,3,5,7]
#print A[find_min(A)]
print search_element(A, X)
 

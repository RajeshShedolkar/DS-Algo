#idea is use two binary search. one for searching subarray and one for that eemeny from that subarray

def check(A,B):
    low = 0
    high = len(A)-1
    while low<=high:
        mid = (low+high)/2
        if A[mid]==B:
            return 1
        elif A[mid]>B:
            high = mid-1
        elif A[mid]<B:
            low = mid+1
    return 0  

def searchMatrix(A, B):
    low = 0
    high = len(A)-1
    if high==-1:
        return 0
    while low<=high:
        mid = (low+high)/2
        if A[mid][0]<= B and B <=A [mid][len(A[mid])-1]:
            return check(A[mid], B)
               
        elif A[mid][0]>B:
            high = mid-1
        elif A[mid][len(A[mid])-1]<B:
            low = mid+1
    return 0 


A = [ [2, 3, 4, 6], [16, 19, 33, 36], [37, 38, 38, 41], [47, 47, 50, 51], [55, 57, 58, 62], [63, 65, 66, 66], [68, 70, 75, 77], [78, 84, 84, 86], [86, 87, 88, 92], [94, 95, 96, 97],[100,101,102] ]
#A = [[1, 2, 4, 7], [12, 14, 34, 52]]
B = 102
#B = 33
#A=[[1]]
#B=1
print searchMatrix(A, B)

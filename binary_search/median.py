def median(A, B):
    A = A+B
    A.sort()
    mid = len(A)/2
    if len(A)%2==1:
        return float(A[mid])
    else:
        return float(A[mid]+A[mid-1])/2
             

A = [1,4,5]
B = [2,3,9]
# 1, 2, 3, 4, 5, 9
print median(A, B)    

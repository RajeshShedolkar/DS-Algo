# 3 5 4 2
def max_diff(A):
    count=0
    min = A[0]
    max = 0
    for j in A:
        if max<count:
            max = count
        if min<=j:
            count+=1
        if min>j:
            count=0
            min = j
    return max                               
    
def max_profit(A):
    min=A[0]
    max = A[1]-A[0]
    for a in A[1:]:
        if max<a-min:
            max =a-min
        if min>a:
            min = a
    
    return max 

A = [3,5,4,1,6,2]
print max_profit(A)
A = [3,5,4,1]
A = [1,2,3,4,2,3,4,5,6,7]
print max_diff(A)               

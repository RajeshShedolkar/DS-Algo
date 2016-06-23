# minimum some of two numbers form by digits given by array as input 
# array contains numbers from 0-9
def minimum_sum(A):
    A.sort()
    n = len(A)
    X,Y=0,0
    for i in range(n):
        if i%2 == 0:
           X = X * 10 + A[i]
        else:
            Y = Y * 10 + A[i]
    
    
    return X+Y

A = [6, 8, 4, 5, 2, 3]
print minimum_sum(A)
A = [4, 0, 3, 7, 5]
print minimum_sum(A)

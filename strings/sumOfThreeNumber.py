#closet sum of three numbers to the given number

def sum(A, X):
    A.sort()
    min_diff = 2147483648
    closest_sum = 0
    for i in range(len(A)):
        j = i+1
        k = len(A)-1
        while j<k:
            temp = A[i]+A[j]+A[k]
            diff = abs(X-temp)
            if diff==0:
                return temp 
            if diff < min_diff:
                min_diff = diff
                closest_sum = temp
            if temp<X:
                j+=1
            else:
                k-=1
    return closest_sum

    
                             
A = [1,-1,2,4]
X = 1
print sum(A, X)

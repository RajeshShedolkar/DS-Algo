def min_avg(A, k):
    index = 0
    min_sum=0
    for i in range(k):
        min_sum = min_sum+A[i]
    sum = min_sum
    
    for p in range(k,len(A)):
        sum = sum - A[p-k]+A[p]
        if sum<min_sum:
            min_sum = sum
            index = p-k+1
    return A[index : index + k]

A = [3,7,90,20,10,50,40]

print min_avg(A,3)                 

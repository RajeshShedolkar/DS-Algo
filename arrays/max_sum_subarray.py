# A = [-2, 1, 3, -2, -2, 5]
def max_sum(A):
    max_sum_so_far = A[0]
    n = len(A)
    i = 1
    sum = A[0]
    while i<n:
        #max = max(max_sum_so_far, sum + A[i])
        #sum = sum +A[i]
        #if(sum < A[i]):
        #    sum = A[i]
        sum = max(A[i],sum+A[i]) #both are same things   
        max_sum_so_far = max(max_sum_so_far, sum)
        i+=1     
    return max_sum_so_far

def max_sum1(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here+x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
    
#101010010                 
A = [-1,1,-1,1,-1,1,1,-1,1]

print max_sum(A)
print max_sum1(A)

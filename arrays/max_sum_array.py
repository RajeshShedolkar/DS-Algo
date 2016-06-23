# Maximum sum of subarray of given array
#A =  [-2, -3, 4, -1, 2, -5, 4]
def max_sum(A):
    max_sum=sum= A[0]
    j,index,count = 1,0,1
    for i in A[1:]:
        
        sum = sum+i
        if sum < i:
            sum = i
            index = j
            count=1
        if(max_sum <= sum ):    
            max_sum = max(sum,max_sum)
            count+=1
        j+=1
    print A[index:index+count],index,count
    #print index,count
    return max_sum
#A = [-3, -2, -1, -5]
A = [0, 1, 0]
for i in range(0,len(A)):
    if A[i]==0:
        A[i]=1
    else :
        A[i] = -1
                
print max_sum(A)

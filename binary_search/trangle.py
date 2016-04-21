#this solution have time complexity O(n*n*log(n))

def no_of_trangle(A):
    #sorting array
    A.sort()
    #initialization of high and low
    low = 0
    high = len(A)-1
    #index will be element which we don't need to check beyond that index our solution will be upto that index
    #total trangles
    total, index=0, 0
    #first for loop which will start at 0 and itrate upto n-3
    for i in range(0, len(A)-2):
    #2nd for loop 2nd element it will start at i+1 and itrate upto n-2
        for j in range(i+1, len(A)-1):
            #for each new itration initilization for low and high and also for index
            low = j+1
            high = len(A)-1
            index = j
            #binary search to find rightmost index
            while low<=high and low>j:
                mid = (low+high)/2
                if A[i]+A[j]>A[mid]:
                    index = mid
                    low = mid+1
                else:
                    high = mid-1
            total = total+index-j
    return total

A = [1, 3, 4, 5]
A = [3,1,5,4]
A = [1, 2, 2, 2, 3, 7, 8]
print no_of_trangle(A)

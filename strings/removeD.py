# remove adjacent duplicates from string
# ex.   RADDABCE  // 1st time
#       RAABCE    // 2nd time 
#       RBCE      // 3rd time no Adjacent duplicates found
# final output:  RBCE
A = 'RADDABCE'


def remove(A):
    A = list(A)
    prev = 0
    curr = 1
    count = 0
    n = len(A)-1
    while curr <= n:
        if A[prev] != A[curr]:
            A[count] = A[prev]
            count += 1
        else:
            curr = curr + 1
        prev = curr
        curr +=1
       
    t = 1

    while A[n]==A[n-1] and n >= 0:
        t+=1
        n=n-1
    if t%2==1:
        A[count]=A[len(A)-1]    
        count = count + 1 
    return A[:count] 

done = 0
print A
while not done:
    #print A
    s = remove(A)
    if len(s)==len(A):
        done = 1
    A = s      

print ''.join(A)                      

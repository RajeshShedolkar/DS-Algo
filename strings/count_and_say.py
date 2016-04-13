''' 
1, 11, 21, 1211, 111221, ...
1 is read off as one 1 or 11.
11 is read off as two 1s or 21.
21 is read off as one 2, then one 1 or 1211.
  
Given an integer n, generate the nth sequence.
for ex n=2 shuld return '11'
'''
def next(A):
    count = 1
    flag=0
    n = len(A)
    val = ''
    for i in range(len(A)-1):
        if A[i]==A[i+1]:
            count+=1
        else:
            flag=1
        
        if flag:
            val = val+str(count)+A[i]
            flag=0
            count=1
    
    if A[n-2]==A[n-1]:
        val = val+str(count)+A[n-1]
    else:
        count=1
        val = val+str(count)+A[n-1]
    return val


def countAndSay(A):
    if A==1:
        return '1'
    s = '1'
    for i in range(1,A):
        s = next(s)
    return s

# array of nth sequence
A = [1, 2, 3, 4, 5, 6, 11, 13]
for n in A:
    print countAndSay(n)

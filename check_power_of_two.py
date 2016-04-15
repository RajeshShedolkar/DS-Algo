# Find if Given number is power of 2 or not. 
# More specifically, find if given number can be expressed as 2^k where k >= 1.

def power(A):
    try:
        num = int(A)
    except:
        num=0        
    if num==0:
        return 0
    if A=='1':
        return 0
    elif num%2==1:
        return 0
    A = ''
    while num>0:
        c = str(num%2)
        A = A+c
        num = num/2
    #print len(s[::-1])
    for i in range(len(A)):
        if i==len(A)-1:
            if A[i]=='1':
                return 1
            else:
                return 0
        else:
            if A[i]!='0':
                return 0

#A = '128'
A = '0'
A = '0w'
A = '1'
A = "48"
A = '256'
print power(A)

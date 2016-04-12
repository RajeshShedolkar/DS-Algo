def isNumber(A):
    A = A.strip()
    n = len(A)
    if n == 0:
        return 0
    if A[0] == '+' or A[0] == '-':
        A = A[1:]
        n = n - 1
        if n == 0:
            return 0
    i = 0
    dotEncountered = False
    eEncountered = False
    while i < n:
        if A[i] >= '0' and A[i] <= '9':
            i += 1
            continue
        if A[i] == '.':
            if dotEncountered:
                return 0
            dotEncountered = True
            i += 1
            if i >= n:
                return 0
            elif A[i] == 'e':
                return 0
        elif A[i] == 'e':
            if eEncountered:
                return 0
            eEncountered = True
            dotEncountered = True
            i += 1
            if i < n and (A[i] == '-' or A[i] == '+'):
                i += 1
        else:
            return 0
    return 1


#Testcase1  :  A = " 0.1 "
#Testcase2  :  A = "0"
#Testcase3  :  A = "abc"
#Testcase4  :  A = "+0.1"
A = "2e10" 
print isNumber(A)    

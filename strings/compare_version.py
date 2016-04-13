def compareVersion(A, B):
    diff = abs(len(A.split('.'))-len(B.split('.')))
    if len(A)>len(B):
        B = B+'.0'*diff
    elif len(A)<len(B):
        A = A+'.0'*diff
    try :
        if int(A)==int(B):
            return 0
    except:
        pass
    A = A.split('.')
    B = B.split('.')
    for i in range(len(A)):
        if int(A[i])<int(B[i]):
            return -1
        elif int(A[i])>int(B[i]) :
            return 1
    
    return 0 

print '''If version1 > version2 return 1,
If version1 < version2 return -1,
otherwise return 0.  '''
A = ['1.2', '2', '1.14.1']
B = ['1', '2.0', '1.14.4']
for i in range(len(A)):
    print A[i],':',B[i],'==>', compareVersion(A[i], B[i])

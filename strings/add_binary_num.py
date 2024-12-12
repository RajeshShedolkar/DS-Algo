def add_bit(a, b, c):
    s = int(a)+int(b)+int(c)
    if s==0:
        return '0','0'
    elif s==1:
        return '0','1'
    elif s==2:
        return '1','0'
    elif s==3:
        return '1','1'                  

def add(A, B):
    diff = len(A)-len(B)
    if diff<0:
        A = ''.join(['0']*abs(diff)) + A
    else:
        B = ''.join(['0']*abs(diff))+B
    carry=0
    print A,B
    sum = ''
    for i in range(len(A))[::-1]:
        carry,s=add_bit(A[i], B[i], carry)
        sum = sum+s
    if carry=='1':    
        sum = sum+carry    
    return sum[::-1]
A = '111'
B = '101010101'
print(add(A,B))

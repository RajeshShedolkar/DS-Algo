'''
Questions: Q1. Does string contain whitespace characters before the number?
A. Yes 
Q2. Can the string have garbage characters after the number?
A. Yes. Ignore it. 
Q3. If no numeric character is found before encountering garbage characters, what should I do?
A. Return 0. 
Q4. What if the integer overflows?
A. Return INT_MAX if the number is positive, INT_MIN otherwise.   
'''
def atoi(A):
    A = A.split(' ')
    B = []
    for i in A:
        if i:
            B.append(i)
            break
    str = ''
    if  B[0][0]=='-' or  B[0][0]=='+' or  '0'<=B[0][0] and B[0][0]<='9':
        sign = B[0][0]
    else:
        sign = False
        
    if sign:    
        for c in B[0][1:]:
            if '0'<=c and c<='9':
                str = str+c
            else:
                break
        str = sign + str    
    result = 0
    
    try :
        if int(str) :
            result = int(str)
    except:
        result = 0
        
    if result > 2147483647:
        result = 2147483647
    elif result < -2147483648:
        result = -2147483648
        
        
    return result

A = ["9 120", "123", "+12", "-1232 4545", "0", "123 a", "w12"]

for str in A:
    print atoi(str)

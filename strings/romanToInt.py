def romanToInt(A):    
    dict={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    num=0
    for i in range(len(A)-1):
        if dict[A[i]]<dict[A[i+1]]:
            num = num - dict[A[i]]
        else:
            num = num+dict[A[i]]
    num = num+dict[A[len(A)-1]]        
    return num

A = "XIV"
A = "XX"
A = "XLVIII"
print romanToInt(A)

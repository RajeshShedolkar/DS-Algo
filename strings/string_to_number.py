def number(str):
    num = 0
    dict = {'0':0,'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    for c in str:
        if '0'<=c and c<='9':
            num = dict[c] + num*10
        else:
            return False
    return num                


def convert(A):
    n = len(A)
    sign = 1
    if A[0]=='+' or A[0]=='-':
        #A = A[1:]
        if A[0]=='-':
            sign = -1
        A = A[1:]     
        n = n-1
        if n==0:
            return False
    
    A = A.split('.')
    num1 = 0
    flag=1   #using flag for handling 0
    flag1 = 1 
    if len(A)==1:
        num1 = number(A[0])
        if num1==0:
            flag=0
        if not num1 and flag:
            return False
    elif len(A)==2 :
        num1 = number(A[0])
        if num1==0:
            flag=0
        if not num1 and flag:
            return False
        num2 = number(A[1])
        if num2==0:
            flag1=0          
        if not number(A[1]) and flag1:
            return False
        #num2 = number(A[1])
        num2 = float(num2)/10**len(A[1])
        num1 = num1+num2
    else:
        return False       
    #print sign        
    return num1*sign           

               
A = "-567.1232" # -567.1232
A = "+512" #512
A = "-56" # -56
A = "123.12.12" #False
A = "+12." #+12.
A = "-0.0123" #-0.0123
A = "0001." #1.0
A = "-12.902092"
print convert(A)
                          

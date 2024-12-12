def check(A):
    if len(A)==2:
        A = '0'+A
    elif len(A)==1:
        A = '00'+A
    elif len(A)>3:
        return False 
              
    try :
        if not ('0'<=A[0] and A[0]<='2'):
            return False      
    except:
        return False
    try:         
        if A[0]=='2':
            if('0'<=A[1] and A[1]<='5') and  ('0'<=A[2] and A[2]<='5'):
                return True
            else:
                return False      
    except:
        return False
    
    try:
        if ('0'<=A[0] and A[0]<='1'): 
            if  ('0'<=A[1] and A[1]<='9') and  ('0'<=A[2] and A[2]<='9'):
                return True
            else:
                return False
    except:
       return False    
                        
def valid_ip(A):
    A = A.split(":")
    if not len(A)==4:
        return False
    valid = True
    for c in A:
        valid = valid*check(c)
    if valid:
        return True
    else:      
        return False      
              
A = "0:0:0:0"
A = "255:255:255:255"
print(A, valid_ip(A))

# Reverse bits of an 32 bit unsigned integer
'''
Input X=3
     00000000000000000000000000000011 
=>   11000000000000000000000000000000
'''
# Output 3221225472

def reverse(A):
    B=0
    k=31
    while k>0:
        #print A
        i = A&1
        B = B|i
        B = B<<1
        A = A>>1
        k-=1
    #print A    
    return B+A

A = 3
print reverse(A) 

# another method without using extra space
# by just solving two equations
# we have 1st equation sum of numbers from 1 to n - original sum
# for example S - S_original = m - r
# another equation of sum of square
# S2 - S_original2 = m*m - r*r
# sovle these two equations Eq1 = m-r & Eq2 = m+r
# m = (Eq1+Eq2)/2 & r = Eq2 - m

def repeatNumber(A):
    S = 0
    S2 = 0
    n = 0
    S_original=0
    S2_original = 0
    for i in A:
        S_original = S_original + i
        S2_original = S2_original + i*i
    
    n=len(A)
    S = n*(n+1)/2
    S2 = S*(2*n+1)/3
    eq1 = S-S_original # missing-repeat
    eq2 = (S2-S2_original)/eq1 # missing + repeat
    m = (eq1+eq2)/2
    r = eq2 - m
    return [r,m]
    
def repeat(A):
    list = [False]*(len(A)+1)
    n = len(A)
    sum = 0
    list[0]=True
    for i in range(len(A)):
        if list[A[i]]==False:
            list[A[i]]=True
        else:
            repeat=A[i]
        sum = sum+A[i] 
    miss = (n*(n+1))/2 -sum+repeat
    return [repeat,miss]

A = [4,1,2,5,2]
print repeat(A) 
print repeatNumber(A)        

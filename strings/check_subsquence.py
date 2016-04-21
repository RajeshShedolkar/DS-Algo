def check_subsequence(A, B):
    j=len(B)-1
    for i in A[::-1]:
        if i==B[j]:
            j-=1
    
    if j==-1:
        return True
    else:
        return False



A = 'AvfvXhggYhnb'
B = 'AXY'   
print check_subsequence(A, B)                        

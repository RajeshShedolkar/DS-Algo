def check_palindrome(A):
    i=0
    j=len(A)-1
    while i < j:
        if A[i]!=A[j]:
            return False
        i+=1
        j-=1
    return True

print(check_palindrome('aba'))
        

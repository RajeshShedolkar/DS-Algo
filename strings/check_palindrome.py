def check(A):
    A = A.lower()
    # 'a'.isalnum() returns True and '@'.isalnum() returns False
    A = ''.join(e for e in A if e.isalnum())
    if A==A[::-1]:
        return True
    else:
        return False


A = "A man, a plan, a canal: Panama"
#A = "race a car"
print (check(A))                   

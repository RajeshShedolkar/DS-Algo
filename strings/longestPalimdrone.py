def check(A, start, end):
    while start<end:
        if A[start]!=A[end]:
            return False
        start+=1
        end-=1
    return True 

def longestPalindrome(A):
    length = len(A)-1
    while length>=0:
        start=0
        end = length
        while end<=len(A)-1:
            if check(A, start, end):
                return A[start:end+1]
            start+=1
            end+=1
        length-=1
    return A

A = "aaaabaaa"
print A, longestPalindrome(A)

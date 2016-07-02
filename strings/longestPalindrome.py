def check(A, start, end):
    while start<end:
        if A[start]!=A[end]:
            return False
        start+=1
        end-=1
    return True 

# Time Complexity order of o(n*n*n)
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


def check_max(max_len, curr_index, current_val, start_index):
    if max_len < current_val:
        max_len = current_val
        curr_index = start_index
    return max_len, curr_index        
        
# Time complexity O(n*n)
def subString(A):
    count, max_len = 0, 0
    n = len(A)
    start_index = 0 
    for i in range(len(A)):
        # check for even length palindrome
        start = i-1
        end = i
        count = 0
        while start>=0 and end<n:
            if A[start]!=A[end]:
                break
            count += 1
            start = start - 1
            end = end + 1
        #max_len = max(2*count, max_len)
        max_len,start_index = check_max(max_len, start_index, 2*count, start+1)
        # check for odd length palindrome
        start = i - 1
        end = i + 1
        count = 0
        while start>=0 and end<n:
            if A[start]!=A[end]:
                break
            count += 1
            start = start - 1
            end = end + 1
        #max_len = max(2*count, max_len)
        max_len, start_index = check_max(max_len, start_index, 2*count+1, start+1)  
    #print start_index
    return A[start_index : start_index + max_len]

A = "abb"
#print A, longestPalindrome(A)
print subString(A)

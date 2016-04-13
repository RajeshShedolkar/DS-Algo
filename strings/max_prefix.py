def longestCommonPrefix(A):
    A_min = min([len(e) for e in A])
    count=0
    for i in range(A_min):
        c =  A[0][i]
        for a in A:
            if c!=a[i]:
                return a[0:count]
        count+=1      
    return A[0][0:count] 

A =  ["abcdefgh", "abefghijk", "abcefgh" ]
A =  ["cdeerare", "cde"]
A =  ["abcd", "abc", "ab", "a"]
print longestCommonPrefix(A)

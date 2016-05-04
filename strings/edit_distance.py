# edit distance means the no. of steps by doing operation add, delete, update make the given two strings equal
# here in this program we need to identify those cases who have 1 edit distance

def edit_distance(A, B):
    diff = abs(len(A)-len(B))
    if diff<2:
        i=0
        j=0
        count=0
        if len(A)==len(B):
            while i < len(A):
                if count>1:
                    return False
                if A[i]!=B[i]:
                    count+=1
                i+=1
        else:
            while i<len(A) and j<len(B):
                if count>1:
                    return False
                if A[i]==B[j]:
                    i+=1
                    j+=1
                else:
                    count+=1
                    i+=1
            #to handle boundary case since A has length n and B has n-1 length
            # to handle such type of cases A = 'aaac' & B = 'aaa' 
            if count==0:
                    count+=1
        if count==1:
            return True
        else:
            return False                    
    else:
        return False

A = 'aba'
B = 'aa'
A = 'abc'
B = 'ad'
A = 'ccc'
B = 'cc'
A = 'v'
B = ''
A = ''
print edit_distance(A, B)         

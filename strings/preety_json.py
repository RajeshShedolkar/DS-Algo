def json(A):
    A = A.replace(" ","")
    count=0
    c = ''
    B = []
    i=0
    while i< len(A):
        if A[i]=='{' or A[i]=='[':
            if c:
                B.append(count*'\t'+c)
            B.append(count*'\t'+A[i])
            count = count+1
            c = ''
        elif A[i]=='}' or A[i]==']':
            if c:
                B.append(count*'\t'+c)
            count = count-1
            if i<len(A)-1:
                if A[i+1]==',':
                    B.append(count*'\t'+A[i]+A[i+1])
                    i = i+1 
                else:
                    B.append(count*'\t'+A[i])
            elif i==len(A)-1:
                B.append(count*'\t'+A[i])
            c = ''
        elif A[i]==',':
            B.append('\t'*count+c+A[i])
            c = ''
        else:
            c+=A[i]
        i+=1
    return B
A = " [{1:2,3:4},{'one':1,'two':'rwo'},'raj':'twswt']"
A = '["foo", {"bar":["baz",null,1.0,2]}]'
A = '{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}'
#A = '[[{{[]}}]]'
for i in json(A):
    print i

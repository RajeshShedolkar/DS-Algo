A = [1,2,3,4]
b = 6
b = b % len(A)
def rotate(A,b):
    ret = []
    for i in range(len(A)):
        ret.append(A[(i+b)%len(A)])
    return ret

print rotate(A,b)        

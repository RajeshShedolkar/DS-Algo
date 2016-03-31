def mod(a):
    if a<0:
        a = -a
    return a     
def min_path(A, B):
    total_steps = 0
    n = len(A)
    x=[]
    y=[]
    i=1;
    while i<n:
        x.append(mod(A[i]-A[i-1]))
        y.append(mod(B[i]-B[i-1]))
        total_steps = total_steps + max(x[i-1],y[i-1])
        i+=1
    return total_steps


A = [0, 1, 1]
B = [0, 1, 2]
print min_path(A, B)          

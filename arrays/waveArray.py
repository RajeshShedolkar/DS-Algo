def wave(A):
    A = sorted(A)
    for i in range(0, len(A), 2):
        if i+1< len(A):
            A[i],A[i+1]=A[i+1],A[i]
    return A

A = [3, 1, 4, 2, 5]
print(wave(A))         

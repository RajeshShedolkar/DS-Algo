A = [[1, 2, 3], [4, 5, 6], [7, 8, 9] ]
def spiral(A):
    T,B,L,R=0,len(A)-1,0,len(A)-1
    direction = 0
    arr=[]
    while T <= B and L <= R :
        if direction==0:
            i = L
            while i <= R:
                arr.append(A[T][i])
                i = i + 1
            direction = 1
            T = T + 1
        elif direction == 1 :
            i = T
            while i <= B :
                arr.append(A[i][R])
                i = i + 1
            R = R - 1
            direction = 2
        elif direction == 2 :
            i = R
            while i >= L :
                arr.append(A[B][i])            
                i = i - 1
            B = B - 1
            direction = 3
        elif direction == 3 :
            i = B
            while i >= T :
                arr.append(A[i][L])
                i = i - 1
            L = L + 1
            direction = 0
     
    return arr                                                     

print spiral(A)

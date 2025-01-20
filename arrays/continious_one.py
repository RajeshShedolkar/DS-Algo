#Find Index of 0 to be replaced with 1 to get longest continuous sequence of 1s in a binary array
# 1 1 0 0 1 0 1 1 1 0 1 1 1
# idea is simple.basicaly track the length between two two zeros excluding 1 zero in between the length

def max_count(A):
    
    prev_prev_zero = -1
    prev_zero = -1
    max_count = 0
    i = 0
    index = -1
    n = len(A)
    while i < n:
        if A[i] == 0:
            if i - prev_prev_zero > max_count:
                max_count = i - prev_prev_zero
                index = prev_zero
            prev_prev_zero = prev_zero
            prev_zero = i
        i+=1
    if n - prev_prev_zero > max_count:
        max_count = n - prev_prev_zero
        index = prev_zero
    return index


A = [1, 1, 1, 0]
#A = [1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1]
print(A, "  index : ", max_count(A))

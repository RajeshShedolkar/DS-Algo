def compare(a, b):
    XY = a+b
    YX = a+b
    if a > b:
        return 1
    else :
        return -1

A = ['9', '90', '32', '912', '12' ]
print A.sort(compare)

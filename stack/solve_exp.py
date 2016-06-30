# exp is in pre order

def solve(A):
    ret = []
    first, second = 0, 0
    
    for a in A:
        #second = ret.pop()
        #first = ret.pop() 
        if a in '*/+-':
            second = ret.pop()
            first = ret.pop()
            if a == '+':
                ret.append(first + second)
            elif a == '-':
                ret.append(first - second)
            elif a == '/':
                ret.append(first / second)
            else:
                ret.append(first*second)
        else:
            ret.append(int(a))

    if len(ret) == 1:
        return ret[0]
    else:
        return 0

A = ["2", "1", "+", "3", "*"]
A = ["4", "13", "5", "/", "+"]
print solve(A)

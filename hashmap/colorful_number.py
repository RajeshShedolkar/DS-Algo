'''
A number can be broken into different sub-sequence parts. 
Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
And this number is a COLORFUL number, since product of every digit of a sub-sequence are different

N = 23
2 3 23
2 -> 2
3 -> 3
23 -> 6
this number is a COLORFUL number since product of every digit of a sub-sequence are different. 

Output : 1

'''


def consecutive_groups(iterable):
    s = tuple(iterable)
    for size in range(1, len(s)+1):
        for index in range(len(s)+1-size):
            yield iterable[index:index+size]

def prod(a):
    prod = 1
    for i in a:
        prod = prod*int(i)
    return prod 


def colorful(A):
    s = str(A)
    d = {}
    a = list(consecutive_groups(s))
    for i in a:
        p = prod(i)
        if p in d:
            return 0
        else:
            d[p]=1
    return 1 



print colorful(23)
print colorful(242)
print colorful(3245)

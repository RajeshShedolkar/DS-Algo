'''
# Read input from stdin and provide input before running code

name = raw_input('What is your name?\n')
print 'Hi, %s.' % name
'''
# print 'Hello World!'

s = raw_input()
def F(string):
    s = {}
    for i in string:
        if i not in s:
            s[i]=0
        else:
            s[i] = s[i] + 1
    return len(s)

def consecutive_groups(iterable):
    s = tuple(iterable)
    for size in range(1, len(s)+1):
        for index in range(len(s)+1-size):
            yield iterable[index:index+size]

A = list( consecutive_groups(s) )
A_sum = 0
A_dis_sum = 0
s_dis = {}
for a in A:
    if a not in s_dis:
        s_dis[a] = 0
        A_dis_sum = A_dis_sum + F(a)
    A_sum = A_sum + F(a)

print abs(A_sum-A_dis_sum)


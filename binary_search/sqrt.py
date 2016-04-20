#sqrt in integer

def sqrt(n):
    x=n
    y=1
    while x>y:
        x = (x+y)/2
        y = n/x
    
    return x
n=11
n=0
n=49
n=48
print sqrt(n)
           

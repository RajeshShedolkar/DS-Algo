#check y is power of x

def check_power(x, y):
    if x==1:
        return (y==1)
 
    pow = 1  
    while pow<y:
        pow = pow*x
    if pow==y:
        return True
    return False

x, y=1, 12
print check_power(x, y)    

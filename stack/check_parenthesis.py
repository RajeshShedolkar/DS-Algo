
def match(a, b):
    if a=='(' and b==')' or a=='{' and b=='}' or a=='[' and b==']' :
        return True
    else:
        return False     

def check(exp):
    stack = []

    for c in exp:
        if c in ['{','[', '(' ]:
            stack.append(c)
        elif c in [ '}', ')', ']' ]:
            if len(stack) and not match(stack.pop(), c):
                return False
    if stack:
        return False
    else:
        return True



exp = '[({a+b}+{b-a})]'

print check(exp)
                

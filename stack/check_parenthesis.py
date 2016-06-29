
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
            # handling case like '}]'
            if len(stack)==0:
                return False

            if not match(stack.pop(), c):
                return False
    if stack:
        return False
    else:
        return True



exp = '[({a+b}+{b-a})]'

exp = '}]'
print check(exp)
                

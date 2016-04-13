def subString(sub, string):
    n1 = len(sub)
    n2 = len(string)
    if n1==0 or n2 ==0:
        return -1
    string = string.split(sub)
    #print string
    if len(string[0])==n2:
        return -1
    else:
        return len(string[0])

sub = "esha"
string = "rajesh"   

print subString(sub, string)                

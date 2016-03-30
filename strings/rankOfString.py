#this function for those strings who doesn't have duplicate elements
# str = 'string'
def fact(n):
    if n<=1 :
        return 1
    else :
        return n*fact(n-1)     


def rank(str):
    rank = 0
    for i in range(len(str)):
        j = i + 1
        count=0
        while j<len(str):
            if str[i] > str[j] :
                count+=1
            j+=1      
        
        rank = rank + count*fact( len(str) - 1 - i )
    return rank+1

str = 'bac'
print rank(str)   

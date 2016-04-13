# length of last word
def lengthOfLastWord(A):
    A = A.split(' ')
    B = []
    p = 0
    for str in A:
        if str: 
            B.append(str)
    #print len(B)
    if len(B)>0:
        p = len(B[len(B)-1])    
            
    return  p

A = ["my name is rajesh","  my  is  rajesh    ", "rajesh", "   t    "]

for word in A:
    print lengthOfLastWord(word) 


# reverse strings of words
def reverseWords(A):
    # A[::-1] reverse sting
    B = []
    A = A.split(' ')
    for i in A:
        if i:
            B.append(i)
    B = B[::-1] #reverse array elements directly
    return ' '.join(B) 

A =[ "my name is rajseh", "  my   name  is       rajesh"]
for sen in A:
    print reverseWords(sen)

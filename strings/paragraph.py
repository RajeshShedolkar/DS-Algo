# make sentences in paragraph
# ASSUMING n > maximum length of word containing sentences

def para(A, n):
    print len(A), A
    start = 0
    end = n
    while start < len(A):
        while end < len(A) and  A[end]!= ' ':
            end -= 1
        # also includeing extra space  
        print A[start:end + 1]
        #if we want to modify we can add '\n' add after the 'end' index 
        start = end + 1
        end = end + 1 + n

#----------------------------------------------------
# INPUT
A = 'abc ab defghi mnop jkl er e r rfg mno dhdh'
para(A, 20)              

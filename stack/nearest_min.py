# nearest minimum element

# time complexity  O(n*n)
def prevSmaller(A):
    min_val= A[0]
    ret = [-1]*len(A)
    for i in range(len(A)):
        j = i-1
        while j>=0:
            if A[j]<A[i]:
                ret[i] = A[j]
                break
            j-=1
    return ret

# order(n)
def small(A):
    st = []
    ans = [-1]*len(A)
    for i in range(len(A)):
        while len(st)>0 and st[len(st)-1] >= A[i]:
            st.pop()
        if len(st) == 0 :
            ans[i] = -1;
        else: 
            ans[i] = st[len(st)-1]
        st.append(A[i])
    return ans 

A = [34, 35, 27, 42, 5, 28, 39, 20, 28]
print(prevSmaller(A))
print(small(A))

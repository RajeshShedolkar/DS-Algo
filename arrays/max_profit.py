def maxDifference(A):
    min_element = A[0]
    max_diff = A[1]-A[0]
    for next_element in A[1:]:
        if max_diff < next_element - min_element:
            max_diff = next_element - min_element
        if min_element > next_element:
            min_element = next_element
    
    return max_diff
    
A = [25, 7, 28, 1, 19];
print maxDifference(A)
                      
                    
            

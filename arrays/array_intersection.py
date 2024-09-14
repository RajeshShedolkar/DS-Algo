from collections import Counter

def array_intersection(arr1, arr2):
    count1 = Counter(arr1)
    count2 = Counter(arr2)
    intersection = []
    
    for num in count1:
        if num in count2:
            intersection.extend([num] * min(count1[num], count2[num]))
    
    return intersection

# Example usage:
arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 2, 4, 6]
print(array_intersection(arr1, arr2))  # Output: [2, 2, 4]

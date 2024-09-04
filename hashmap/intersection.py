from collections import Counter

def intersect(nums1, nums2):
    # Count the elements in both arrays
    counts1 = Counter(nums1)
    counts2 = Counter(nums2)
    intersection = []
    print(counts1, counts2)
    for num in counts1:
        if num in counts2:
            # Get the minimum count of each number from both arrays
            intersection.extend([num] * min(counts1[num], counts2[num]))
    
    return intersection

# Example usage
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4, 9, 5]
print(intersect(nums1, nums2))  # Output: [4, 9]

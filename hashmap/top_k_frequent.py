from collections import Counter
import heapq

def top_k_frequent(nums, k):
    # Count the frequency of each element using a hashmap
    count = Counter(nums)
    # Use a heap to get the k most frequent elements
    return heapq.nlargest(k, count.keys(), key=count.get)

# Example usage
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(top_k_frequent(nums, k))  # Output: [1, 2]

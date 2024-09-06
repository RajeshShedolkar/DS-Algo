def subarray_sum(nums, k):
    # Create a hashmap to store the cumulative sum frequencies
    sum_map = {0: 1}
    count = 0
    cumulative_sum = 0

    for num in nums:
        cumulative_sum += num
        # Check if there is a subarray that ends at the current index and sums to k
        if cumulative_sum - k in sum_map:
            count += sum_map[cumulative_sum - k]
        # Update the hashmap with the current cumulative sum
        sum_map[cumulative_sum] = sum_map.get(cumulative_sum, 0) + 1

    return count

# Example usage
nums = [1, 1, 1]
k = 2
print(subarray_sum(nums, k))  # Output: 2

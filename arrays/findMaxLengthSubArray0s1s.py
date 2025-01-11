def findMaxLength(nums):
    # Replace 0s with -1s
    nums = [-1 if num == 0 else 1 for num in nums]
    
    prefix_sum = 0
    max_length = 0
    prefix_sum_map = {0: -1}  # To handle subarray starting from index 0

    for i, num in enumerate(nums):
        prefix_sum += num

        # Check if this prefix_sum has been seen before
        if prefix_sum in prefix_sum_map:
            # Calculate the length of the subarray
            max_length = max(max_length, i - prefix_sum_map[prefix_sum])
        else:
            # Store the first occurrence of this prefix_sum
            prefix_sum_map[prefix_sum] = i

    return max_length

# Example Usage
nums = [0, 1, 0, 1, 0, 1, 1]
print("Length of longest subarray with equal number of 0s and 1s:", findMaxLength(nums))

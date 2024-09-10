def find_max_length(nums):
    count_map = {0: -1}  # To handle the case where subarray starts from index 0
    max_length = 0
    count = 0

    for i, num in enumerate(nums):
        count += 1 if num == 1 else -1
        
        if count in count_map:
            max_length = max(max_length, i - count_map[count])
        else:
            count_map[count] = i

    return max_length

# Example usage
nums = [0, 1, 0, 1, 0, 1]
print(find_max_length(nums))  # Output: 6

def maxSubArray(nums):
    max_sum = nums[0]  # Initialize with the first element
    current_sum = nums[0]

    for num in nums[1:]:  # Start iterating from the second element
        current_sum = max(num, current_sum + num)  # Decide to add num to the current subarray or start new
        max_sum = max(max_sum, current_sum)  # Update max_sum if current_sum is larger

    return max_sum

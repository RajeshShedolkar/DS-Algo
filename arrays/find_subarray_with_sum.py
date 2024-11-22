def find_subarray_with_sum(arr, target):
    # Initialize pointers and current sum
    left = 0
    current_sum = 0
    
    # Iterate through the array with the right pointer
    for right in range(len(arr)):
        # Add the current element to the sum
        current_sum += arr[right]
        
        # Shrink the window if the sum exceeds the target
        while current_sum > target and left <= right:
            current_sum -= arr[left]
            left += 1
        
        # Check if the current sum equals the target
        if current_sum == target:
            # Return 1-based indices
            return (left + 1, right + 1)
    
    # Return None if no such subarray is found
    return None

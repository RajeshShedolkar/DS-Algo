def kadane_algorithm(arr):
    # Initialize variables
    max_current = arr[0]  # Maximum sum ending at the current position
    max_global = arr[0]   # Maximum sum found so far

    for i in range(1, len(arr)):
        # Update the maximum sum ending at the current position
        max_current = max(arr[i], max_current + arr[i])

        # Update the global maximum if the current is larger
        if max_current > max_global:
            max_global = max_current

    return max_global


# Example usage
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum subarray sum:", kadane_algorithm(arr))


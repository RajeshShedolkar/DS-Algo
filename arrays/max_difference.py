def max_difference(arr):
    min_value = arr[0]
    max_diff = 0
    
    for num in arr[1:]:
        if num < min_value:
            min_value = num
        else:
            max_diff = max(max_diff, num - min_value)
    
    return max_diff

# Example usage:
arr = [7, 1, 5, 3, 6, 4]
print(max_difference(arr))  # Output: 5 (6 - 1)

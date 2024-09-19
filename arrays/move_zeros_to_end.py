def move_zeros_to_end(arr):
    count = 0  # Count of non-zero elements
    
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count], arr[i] = arr[i], arr[count]
            count += 1
    
    return arr

# Example usage:
arr = [0, 1, 0, 3, 12]
print(move_zeros_to_end(arr))  # Output: [1, 3, 12, 0, 0]

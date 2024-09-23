def min_jumps(arr):
    n = len(arr)
    
    if n == 1:
        return 0
    if arr[0] == 0:
        return -1
    
    max_reach = arr[0]
    step = arr[0]
    jump = 1
    
    for i in range(1, n):
        if i == n - 1:
            return jump
        
        max_reach = max(max_reach, i + arr[i])
        step -= 1
        
        if step == 0:
            jump += 1
            if i >= max_reach:
                return -1
            step = max_reach - i
    
    return -1

# Example usage:
arr = [2, 3, 1, 1, 4]
print(min_jumps(arr))  # Output: 2 (jump from 2 -> 3 -> 4)

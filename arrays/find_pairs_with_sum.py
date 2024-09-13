def find_pairs_with_sum(arr, target):
    pairs = []
    seen = set()
    
    for num in arr:
        diff = target - num
        if diff in seen:
            pairs.append((diff, num))
        seen.add(num)
    
    return pairs

# Example usage:
arr = [1, 2, 3, 4, 5, 6]
target = 7
print(find_pairs_with_sum(arr, target))  # Output: [(3, 4), (2, 5), (1, 6)]

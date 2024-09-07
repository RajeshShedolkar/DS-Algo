def find_duplicates(nums):
    # Create a hashmap to store the frequency of each element
    num_count = {}
    duplicates = []

    for num in nums:
        if num in num_count:
            duplicates.append(num)
        else:
            num_count[num] = 1

    return duplicates

# Example usage
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(find_duplicates(nums))  # Output: [2, 3]

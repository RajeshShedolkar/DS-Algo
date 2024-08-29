def first_unique_char(s):
    # Create a hashmap to store the frequency of each character
    char_count = {}
    
    # Count frequency of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find the index of the first non-repeating character
    for index, char in enumerate(s):
        if char_count[char] == 1:
            return index
            
    return -1

# Example usage
s = "leetcode"
print(first_unique_char(s))  # Output: 0 (first unique character 'l')

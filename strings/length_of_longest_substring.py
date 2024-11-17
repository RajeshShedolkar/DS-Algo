def length_of_longest_substring(s: str) -> int:
    # Dictionary to store the last index of each character
    char_index = {}
    max_length = 0
    start = 0  # Left pointer of the sliding window

    for end in range(len(s)):  # Right pointer of the sliding window
        # If the character is already in the substring, move the start pointer
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1
        
        # Update the last index of the character
        char_index[s[end]] = end
        
        # Calculate the maximum length
        max_length = max(max_length, end - start + 1)

    return max_length

# Test Cases
print(length_of_longest_substring("abcabcbb"))  # Output: 3
print(length_of_longest_substring("bbbbb"))     # Output: 1
print(length_of_longest_substring("pwwkew"))    # Output: 3

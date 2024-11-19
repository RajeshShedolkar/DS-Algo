from collections import Counter

def first_unique_char(s: str) -> int:
    char_count = Counter(s)
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
    return -1

# Example usage
print(first_unique_char("leetcode"))  # Output: 0
print(first_unique_char("aabb"))      # Output: -1

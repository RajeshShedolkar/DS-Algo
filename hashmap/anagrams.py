from collections import Counter

def is_anagram(s, t):
    # Count the frequency of characters in both strings
    return Counter(s) == Counter(t)

# Example usage
s = "anagram"
t = "nagaram"
print(is_anagram(s, t))  # Output: True

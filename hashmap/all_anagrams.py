from collections import Counter

def find_anagrams(s, p):
    p_count = Counter(p)
    s_count = Counter()
    result = []

    for i in range(len(s)):
        # Add one more letter on the right side of the window
        s_count[s[i]] += 1
        
        # Remove one letter from the left side of the window
        if i >= len(p):
            if s_count[s[i - len(p)]] == 1:
                del s_count[s[i - len(p)]]
            else:
                s_count[s[i - len(p)]] -= 1
        
        # Compare the window with the target string count
        if p_count == s_count:
            result.append(i - len(p) + 1)
    
    return result

# Example usage
s = "cbaebabacd"
p = "abc"
print(find_anagrams(s, p))  # Output: [0, 6]

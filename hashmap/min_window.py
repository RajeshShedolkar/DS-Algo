from collections import Counter

def min_window(s, t):
    if not t or not s:
        return ""
    
    t_count = Counter(t)
    current_count = {}
    have, need = 0, len(t_count)
    left, right = 0, 0
    res, res_len = [-1, -1], float("inf")
    
    while right < len(s):
        char = s[right]
        current_count[char] = current_count.get(char, 0) + 1
        
        if char in t_count and current_count[char] == t_count[char]:
            have += 1
        
        while have == need:
            # Update result if this window is smaller
            if (right - left + 1) < res_len:
                res = [left, right]
                res_len = right - left + 1
            
            # Pop from the left of the window
            current_count[s[left]] -= 1
            if s[left] in t_count and current_count[s[left]] < t_count[s[left]]:
                have -= 1
            left += 1
        
        right += 1
    
    l, r = res
    return s[l:r+1] if res_len != float("inf") else ""

# Example usage
s = "ADOBECODEBANC"
t = "ABC"
print(min_window(s, t))  # Output: "BANC"

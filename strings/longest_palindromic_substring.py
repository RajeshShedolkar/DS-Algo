def longest_palindromic_substring(s: str) -> str:
    def expand_from_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        # Odd-length palindromes
        temp = expand_from_center(i, i)
        if len(temp) > len(longest):
            longest = temp
        # Even-length palindromes
        temp = expand_from_center(i, i + 1)
        if len(temp) > len(longest):
            longest = temp

    return longest

# Example Usage
s = "babad"
print("Longest palindromic substring:", longest_palindromic_substring(s))

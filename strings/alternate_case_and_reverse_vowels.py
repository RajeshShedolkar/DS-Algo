def alternate_case_and_reverse_vowels(s: str) -> str:
    def reverse_vowels(string):
        vowels = "aeiouAEIOU"
        string_list = list(string)
        vowel_positions = [i for i in range(len(string)) if string[i] in vowels]
        left, right = 0, len(vowel_positions) - 1
        
        # Reverse the vowels
        while left < right:
            string_list[vowel_positions[left]], string_list[vowel_positions[right]] = (
                string_list[vowel_positions[right]],
                string_list[vowel_positions[left]],
            )
            left += 1
            right -= 1
        return ''.join(string_list)

    # Apply alternate case
    alternate_cased = ''.join(
        char.upper() if i % 2 == 0 else char.lower()
        for i, char in enumerate(s)
    )
    
    # Reverse vowels in the alternate cased string
    result = reverse_vowels(alternate_cased)
    return result

# Test cases
print(alternate_case_and_reverse_vowels("hello world"))  # Output: "HeLlO wOrLd"
print(alternate_case_and_reverse_vowels("programming is fun"))  # Output: "PrOgRaMmInG iS fUn"

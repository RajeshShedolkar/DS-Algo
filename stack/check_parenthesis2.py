def is_valid_parentheses(s):
    # Stack to keep track of opening brackets
    stack = []
    
    # Dictionary to match opening and closing brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    # Traverse each character in the string
    for char in s:
        # If the character is a closing bracket
        if char in bracket_map:
            # Pop the topmost element from the stack if stack is not empty, otherwise assign a dummy value
            top_element = stack.pop() if stack else '#'
            
            # If the topmost element does not match the corresponding opening bracket in the map, return False
            if bracket_map[char] != top_element:
                return False
        else:
            # If it's an opening bracket, push it onto the stack
            stack.append(char)
    
    # Return True if the stack is empty (all brackets matched and closed correctly), otherwise False
    return not stack

# Test cases
print(is_valid_parentheses("()"))       # True
print(is_valid_parentheses("()[]{}"))   # True
print(is_valid_parentheses("(]"))       # False
print(is_valid_parentheses("([)]"))     # False
print(is_valid_parentheses("{[]}"))     # True

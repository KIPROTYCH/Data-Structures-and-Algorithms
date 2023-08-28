def is_balanced(expression):
    stack = []  # Initialize an empty stack to keep track of opening brackets
    
    opening_brackets = "([{"
    closing_brackets = ")]}"
    bracket_pairs = {')': '(', ']': '[', '}': '{'}  # Define opening and closing brackets and their pairs
    
    for char in expression:
        if char in opening_brackets:
            stack.append(char)  # Push opening bracket onto the stack
        elif char in closing_brackets:
            if not stack or stack[-1] != bracket_pairs[char]:
                return False  # Unbalanced if stack is empty or corresponding opening bracket not at top
            stack.pop()  # Pop corresponding opening bracket from stack
    
    return len(stack) == 0  # Expression is balanced if stack is empty

# Test cases
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False

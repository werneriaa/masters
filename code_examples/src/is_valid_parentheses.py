# https://leetcode.com/problems/valid-parentheses/description/
# Grade: Easy
# Solution: https://leetcode.com/problems/valid-parentheses/solutions/4629015/20-1-approach-1-o-n-python-c-step-by-step-explanation/


def is_valid_parentheses(s: str) -> bool:
    # Stack to keep track of opening parentheses
    stack = []
    # Dictionary mapping closing and opening parentheses
    d = {")": "(", "}": "{", "]": "["}

    # Iterate through each character in the string
    for x in s:
        # If x is a closing parenthesis
        if x in d:
            # Pop the corresponding opening parenthesis from the stack
            if stack and stack[-1] == d[x]:
                stack.pop()
            else:
                return False  # Mismatched parentheses
        else:
            stack.append(x)  # If x is an opening parenthesis, push onto the stack

    # If the stack is empty, all parentheses are matched
    return not stack

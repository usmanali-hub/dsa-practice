"""Valid Parentheses.

Given a string of the bracket characters ``()[]{}`` (other characters are ignored), return True if every
opening bracket is closed by the same type in the correct order.

Approach: a stack of opening brackets. Push each opener; on a closer the top of the stack must be its matching
opener, otherwise the string is invalid. The stack must be empty at the end. Time O(n), space O(n).
"""

PAIRS = {")": "(", "]": "[", "}": "{"}


def is_valid(s: str) -> bool:
    stack: list[str] = []
    for ch in s:
        if ch in PAIRS.values():
            stack.append(ch)
        elif ch in PAIRS and (not stack or stack.pop() != PAIRS[ch]):
            return False
    return not stack

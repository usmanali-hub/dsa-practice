"""Valid Parentheses.

Given a string of ()[]{} characters, decide whether every bracket is closed by the right type in
the right order.

Approach: a stack. Push each opener; on a closer, the top of the stack must be its matching opener.
At the end the stack must be empty. Time O(n), space O(n).
"""

PAIRS = {")": "(", "]": "[", "}": "{"}


def is_valid(s: str) -> bool:
    stack: list[str] = []
    for ch in s:
        if ch in PAIRS:
            if not stack or stack.pop() != PAIRS[ch]:
                return False
        else:
            stack.append(ch)
    return not stack

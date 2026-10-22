"""Valid Palindrome.

Return True if the string reads the same forwards and backwards after lowercasing and
ignoring every non-alphanumeric character.

Approach: two pointers from both ends, skipping non-alphanumeric characters in place.
Time O(n), space O(1). Building a cleaned copy and comparing it to its reverse is simpler but O(n) space.
"""


def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

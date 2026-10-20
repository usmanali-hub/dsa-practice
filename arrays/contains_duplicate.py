"""Contains Duplicate.

Return True if any value appears at least twice.

Approach: walk the list with a set; the first repeat returns early.
Time O(n), space O(n). Sorting first gives O(n log n) time, O(1) extra space.
"""


def contains_duplicate(nums: list[int]) -> bool:
    seen: set[int] = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False

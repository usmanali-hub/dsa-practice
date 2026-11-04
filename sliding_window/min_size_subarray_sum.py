"""Minimum Size Subarray Sum.

Return the length of the shortest contiguous subarray whose sum is at least ``target``, or 0 if none exists.
All numbers must be positive.

Approach: a variable-size window. Grow the right edge until the sum reaches the target, then shrink the left
edge for as long as the sum still reaches it, recording the shortest length seen. Positivity is what makes this
valid: adding an element can only raise the sum and removing one can only lower it, so each edge only moves
forward. Time O(n), space O(1). Raises ValueError if any number is not positive.
"""


def min_subarray_len(target: int, nums: list[int]) -> int:
    if any(n <= 0 for n in nums):
        raise ValueError("numbers must be positive")
    best = len(nums) + 1
    total = left = 0
    for right, value in enumerate(nums):
        total += value
        while total >= target and left <= right:
            best = min(best, right - left + 1)
            total -= nums[left]
            left += 1
    return best if best <= len(nums) else 0

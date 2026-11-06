"""Max Consecutive Ones III.

Given a binary array and an integer ``k``, return the length of the longest subarray that contains at most
``k`` zeros (i.e. all ones after flipping at most ``k`` zeros).

Approach: a variable-size window that may hold at most ``k`` zeros. Extend the right edge every step, counting
zeros; when the count exceeds ``k`` move the left edge forward until it is back to ``k``. The window length
never needs to shrink below its best size, so each edge only moves forward. Time O(n), space O(1).
"""


def longest_ones(nums: list[int], k: int) -> int:
    if k < 0:
        raise ValueError("k must be non-negative")
    zeros = left = best = 0
    for right, value in enumerate(nums):
        if value == 0:
            zeros += 1
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        best = max(best, right - left + 1)
    return best

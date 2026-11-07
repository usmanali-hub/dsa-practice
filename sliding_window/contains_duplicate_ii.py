"""Contains Duplicate II.

Return True if some value appears at two indices ``i`` and ``j`` with ``abs(i - j) <= k``.

Approach: a fixed-size window of the last ``k`` elements kept in a set. Before adding ``nums[i]`` check whether it
is already in the window; then add it, and once the window holds more than ``k`` elements drop the oldest. Time O(n),
space O(min(n, k)). A negative ``k`` raises ValueError; ``k == 0`` can never match.
"""


def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    if k < 0:
        raise ValueError("k must be non-negative")
    window: set[int] = set()
    for i, value in enumerate(nums):
        if value in window:
            return True
        window.add(value)
        if len(window) > k:
            window.remove(nums[i - k])
    return False

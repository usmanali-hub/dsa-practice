"""Contains Duplicate II.

Return True if two equal values sit at indices i != j with |i - j| <= k.

Approach: remember the last index at which each value was seen. If the previous occurrence of the
current value is within k positions, we are done; otherwise overwrite it, since a later index can
only be closer to future occurrences. Time O(n), space O(n).
"""


def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    last_seen: dict[int, int] = {}
    for i, value in enumerate(nums):
        if value in last_seen and i - last_seen[value] <= k:
            return True
        last_seen[value] = i
    return False

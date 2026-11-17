"""Search Insert Position (easy).

Given a sorted list of distinct integers and a target, return the index of the target, or the index where it would be
inserted to keep the list sorted.

Approach: binary search for the leftmost index whose value is >= target, using a half-open range [lo, hi) so the loop
always shrinks and the answer is simply ``lo`` when it ends. Time O(log n), space O(1).
"""


def search_insert(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo

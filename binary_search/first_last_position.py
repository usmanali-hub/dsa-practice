"""Find First and Last Position of Element in Sorted Array (medium).

Given a sorted list (duplicates allowed) and a target, return ``[first_index, last_index]`` of the target, or
``[-1, -1]`` if it is absent, in O(log n).

Approach: two binary searches over a half-open range. ``lower_bound`` finds the first index with value >= target and
``upper_bound`` the first index with value > target; the target occupies ``[lower, upper)``. A single search that
finds one occurrence and scans outwards would be O(n) when every element equals the target. Time O(log n), space O(1).
"""


def _bound(nums: list[int], target: int, strict: bool) -> int:
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target or (strict and nums[mid] == target):
            lo = mid + 1
        else:
            hi = mid
    return lo


def search_range(nums: list[int], target: int) -> list[int]:
    first = _bound(nums, target, strict=False)
    if first == len(nums) or nums[first] != target:
        return [-1, -1]
    return [first, _bound(nums, target, strict=True) - 1]

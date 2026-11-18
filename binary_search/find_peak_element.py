"""Find Peak Element (medium).

A peak element is an element that is strictly greater than its neighbors.
Given an integer array nums, find a peak element, and return its index. If the array contains
multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -inf. In other words, an element is always considered
to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.
"""


def find_peak_element(nums: list[int]) -> int:
    if not nums:
        raise ValueError("nums must not be empty")

    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < nums[mid + 1]:
            # Peak must be to the right
            lo = mid + 1
        else:
            # Peak must be at mid or to the left
            hi = mid

    return lo

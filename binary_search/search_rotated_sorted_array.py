"""Search in Rotated Sorted Array (medium).

A sorted list of distinct integers was rotated at an unknown pivot (``[4, 5, 6, 7, 0, 1, 2]``). Return the index of
the target or -1.

Approach: binary search where, at every step, at least one half of ``[lo, hi]`` is sorted. Compare ``nums[lo]`` with
``nums[mid]`` to find which half is sorted, check whether the target lies inside that sorted half, and keep that half or
discard it. Time O(log n), space O(1). Duplicates would break the "which half is sorted" test (``nums[lo] == nums[mid]``
no longer tells), so this solution requires distinct values.
"""


def search(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:  # left half [lo, mid] is sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:  # right half [mid, hi] is sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1

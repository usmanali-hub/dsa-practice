"""Single Element in a Sorted Array (easy).

Every element in a sorted array appears exactly twice except one, which appears once. Find it in O(log n) time.

Approach: pairs are (nums[0],nums[1]), (nums[2],nums[3]), ... before the single element, so a pair always starts at
an even index there. Binary search on even indices: if nums[mid] == nums[mid+1], the pairing is still intact up to
mid, so the single element is to the right; otherwise it is at or before mid. Time O(log n), space O(1).
"""


def single_non_duplicate(nums: list[int]) -> int:
    if not nums:
        raise ValueError("nums must not be empty")
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if mid % 2 == 1:
            mid -= 1  # always compare an even index with its would-be pair at mid + 1
        if nums[mid] == nums[mid + 1]:
            lo = mid + 2
        else:
            hi = mid
    return nums[lo]

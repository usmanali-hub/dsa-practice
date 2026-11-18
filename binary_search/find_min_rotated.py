"""Find Minimum in Rotated Sorted Array (medium).

Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array
[a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.
"""


def find_min(nums: list[int]) -> int:
    if not nums:
        raise ValueError("nums must not be empty")

    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            # Minimum must be in the right unsorted portion
            lo = mid + 1
        else:
            # nums[mid] <= nums[hi], minimum is at mid or to the left
            hi = mid

    return nums[lo]

"""Sort Colors (Dutch national flag).

Sort a list containing only 0, 1 and 2 in place, in one pass and without a library sort.

Approach: three regions are kept by three pointers. Everything before ``low`` is 0, everything after
``high`` is 2, and ``mid`` scans the unknown middle. A 0 is swapped down, a 2 is swapped up (and not
yet inspected, because what arrived is unknown), a 1 stays. Time O(n), space O(1).
Raises ValueError for any value other than 0, 1 or 2.
"""


def sort_colors(nums: list[int]) -> None:
    if any(n not in (0, 1, 2) for n in nums):
        raise ValueError("values must be 0, 1 or 2")
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 2:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
        else:
            mid += 1

"""Sort Colors (Dutch national flag).

Sort a list containing only 0, 1 and 2 in place, without using a library sort.

Approach: three pointers. ``low`` is the end of the 0 region, ``high`` the start of the 2 region,
and ``i`` scans. Swap 0s to the front and 2s to the back in a single pass.
Time O(n), space O(1).
"""


def sort_colors(nums: list[int]) -> None:
    low, i, high = 0, 0, len(nums) - 1
    while i <= high:
        if nums[i] == 0:
            nums[low], nums[i] = nums[i], nums[low]
            low += 1
            i += 1
        elif nums[i] == 2:
            nums[i], nums[high] = nums[high], nums[i]
            high -= 1  # do not advance i: the swapped-in value is unchecked
        else:
            i += 1

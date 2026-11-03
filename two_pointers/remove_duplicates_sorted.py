"""Remove Duplicates from Sorted Array.

Modify the sorted list in place so each value appears once, and return the new length. The first
``k`` slots hold the unique values in order; what lies beyond them is unspecified.

Approach: a slow pointer marks the end of the unique prefix, a fast pointer scans ahead, and a value
is copied only when it differs from the last kept one. Time O(n), space O(1).
"""


def remove_duplicates(nums: list[int]) -> int:
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write

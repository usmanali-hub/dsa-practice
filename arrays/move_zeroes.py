"""Move Zeroes.

Move all zeros to the end of the list in place, keeping the relative order of
the non-zero elements.

Approach: two pointers. ``write`` marks where the next non-zero belongs; swap
each non-zero into it. Time O(n), space O(1), one pass.
"""


def move_zeroes(nums: list[int]) -> None:
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1

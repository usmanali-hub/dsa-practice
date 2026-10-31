"""Squares of a Sorted Array.

Given integers sorted ascending, return the squares sorted ascending.

Approach: the largest square is at one of the two ends, because negatives become large when squared.
Fill the result from the back, taking whichever end has the larger absolute value and moving that
pointer inward. Time O(n), space O(n) for the output, versus O(n log n) for squaring and re-sorting.
"""


def sorted_squares(nums: list[int]) -> list[int]:
    result = [0] * len(nums)
    left, right = 0, len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[i] = nums[left] ** 2
            left += 1
        else:
            result[i] = nums[right] ** 2
            right -= 1
    return result

"""Trapping Rain Water.

Given bar heights, return how many units of water stay trapped after rain.

Water above a bar is ``min(tallest to its left, tallest to its right) - height``. Two pointers move
inward from both ends; the side with the lower wall is the one whose water level is already decided
(the other wall is at least as tall), so it is settled and advanced. Time O(n), space O(1).
Raises ValueError for negative heights.
"""


def trap(height: list[int]) -> int:
    if any(h < 0 for h in height):
        raise ValueError("heights must be non-negative")
    left, right = 0, len(height) - 1
    left_max = right_max = water = 0
    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            water += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            water += right_max - height[right]
            right -= 1
    return water

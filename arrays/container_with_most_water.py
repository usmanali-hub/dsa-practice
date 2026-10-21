"""Container With Most Water.

Given heights of vertical lines, pick two lines that, with the x-axis, hold the most water.

Approach: two pointers from both ends. The area is limited by the shorter line, so moving the
taller pointer can never help; always move the shorter one inward.
Time O(n), space O(1). Brute force over all pairs is O(n^2).
"""


def max_area(heights: list[int]) -> int:
    left, right = 0, len(heights) - 1
    best = 0
    while left < right:
        best = max(best, min(heights[left], heights[right]) * (right - left))
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return best

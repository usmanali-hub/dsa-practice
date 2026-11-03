"""Container With Most Water.

Bars of the given heights stand at positions 0..n-1. Pick two of them as walls and return the largest
amount of water the container between them can hold: ``min(height) * distance``.

Approach: start with the widest container and move the shorter wall inward. Moving the taller wall can
never help (the width shrinks and the height is still capped by the shorter wall), so the shorter one is
the only move that can improve the result. Time O(n), space O(1). Fewer than two bars hold nothing.
Raises ValueError for negative heights.
"""


def max_area(height: list[int]) -> int:
    if any(h < 0 for h in height):
        raise ValueError("heights must be non-negative")
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        best = max(best, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best

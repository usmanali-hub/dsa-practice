"""Largest Rectangle in Histogram.

Given bar heights (each of width 1), return the area of the largest rectangle that fits inside the histogram.

Approach: a monotonic stack of indices with increasing heights. When a bar is shorter than the one on top of the
stack, the top bar can no longer extend right, so pop it and compute the widest rectangle that uses it as the
shortest bar: it spans from just after the new stack top to just before the current index. A sentinel height of 0 at
the end flushes the stack. Each index is pushed and popped once. Time O(n), space O(n).
"""


def largest_rectangle(heights: list[int]) -> int:
    best = 0
    stack: list[int] = []  # indices of bars with increasing heights
    for i, h in enumerate([*heights, 0]):
        while stack and heights[stack[-1]] >= h:
            height = heights[stack.pop()]
            left = stack[-1] + 1 if stack else 0
            best = max(best, height * (i - left))
        stack.append(i)
    return best

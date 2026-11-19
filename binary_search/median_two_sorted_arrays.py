"""Median of Two Sorted Arrays (medium, LeetCode "hard" but a standard binary-search exercise).

Given two sorted arrays of total length n, return the median in O(log(min(m, n))) time (a merge is O(m + n)).

Approach: binary search the number of elements taken from the *shorter* array, `i`, so that together with
`j = half - i` elements from the other array, the left side holds exactly half the combined length. The partition
is correct when every left element is <= every right element on both sides; shrink the search range toward the side
with the wrong order. With the shorter array searched, `j` always stays in range. Time O(log(min(m, n))), space O(1).
"""


def find_median_sorted_arrays(a: list[int], b: list[int]) -> float:
    if len(a) > len(b):
        a, b = b, a
    m, n = len(a), len(b)
    if m == 0 and n == 0:
        raise ValueError("both arrays are empty")
    total = m + n
    half = (total + 1) // 2
    lo, hi = 0, m
    while lo <= hi:
        i = (lo + hi) // 2
        j = half - i
        a_left = a[i - 1] if i > 0 else float("-inf")
        a_right = a[i] if i < m else float("inf")
        b_left = b[j - 1] if j > 0 else float("-inf")
        b_right = b[j] if j < n else float("inf")
        if a_left <= b_right and b_left <= a_right:
            if total % 2 == 1:
                return float(max(a_left, b_left))
            return (max(a_left, b_left) + min(a_right, b_right)) / 2
        if a_left > b_right:
            hi = i - 1
        else:
            lo = i + 1
    raise AssertionError("inputs were not sorted")

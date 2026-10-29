"""Intersection of Two Arrays II.

Return the multiset intersection: each value appears as many times as it appears in both arrays.

Approach: count the shorter array, then walk the longer one and spend a count each time a value
matches. Time O(n + m), space O(min(n, m)).
"""

from collections import Counter


def intersect(a: list[int], b: list[int]) -> list[int]:
    if len(a) > len(b):
        a, b = b, a
    remaining = Counter(a)
    result: list[int] = []
    for value in b:
        if remaining[value] > 0:
            remaining[value] -= 1
            result.append(value)
    return result

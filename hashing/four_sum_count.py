"""4Sum II.

Count tuples (i, j, k, l) with a[i] + b[j] + c[k] + d[l] == 0.

Approach: meet in the middle. Count every pairwise sum of a and b in a hash map, then for each pair
from c and d add the count of its negation. Time O(n^2), space O(n^2), versus O(n^4) brute force.
"""

from collections import Counter


def four_sum_count(a: list[int], b: list[int], c: list[int], d: list[int]) -> int:
    ab = Counter(x + y for x in a for y in b)
    return sum(ab[-(x + y)] for x in c for y in d)

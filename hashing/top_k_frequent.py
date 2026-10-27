"""Top K Frequent Elements.

Return the ``k`` most frequent values in ``nums`` (any order). Ties at the cut-off are broken by
first appearance so the result is deterministic.

Approach: count with a hash map, then bucket values by frequency (a value can occur at most
``len(nums)`` times) and read the buckets from the highest frequency down. Time O(n), space O(n).
A heap gives O(n log k) and a full sort O(n log n).
"""

from collections import Counter


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    if k <= 0:
        return []
    counts = Counter(nums)  # insertion-ordered, so ties keep first-appearance order
    buckets: list[list[int]] = [[] for _ in range(len(nums) + 1)]
    for value, freq in counts.items():
        buckets[freq].append(value)
    result: list[int] = []
    for freq in range(len(nums), 0, -1):
        for value in buckets[freq]:
            result.append(value)
            if len(result) == k:
                return result
    return result

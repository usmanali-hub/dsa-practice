"""Subarray Sum Equals K.

Count the contiguous subarrays whose elements sum to ``k``. Values may be negative, so a sliding
window does not work.

Approach: prefix sums with a hash map. If the running sum is ``s`` and ``s - k`` was seen ``c``
times before, then ``c`` subarrays ending here sum to ``k``. Start with {0: 1} so subarrays that
begin at index 0 are counted. Time O(n), space O(n).
"""

from collections import defaultdict


def subarray_sum(nums: list[int], k: int) -> int:
    seen: dict[int, int] = defaultdict(int)
    seen[0] = 1
    running = count = 0
    for n in nums:
        running += n
        count += seen[running - k]
        seen[running] += 1
    return count

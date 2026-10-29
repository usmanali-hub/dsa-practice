"""Contiguous Array.

Given a binary array, return the length of the longest contiguous subarray with equally many 0s and 1s.

Approach: treat 0 as -1 and keep a running balance. Two positions with the same balance enclose a
stretch that sums to zero, so store the first index of each balance and measure the distance back to
it. The empty prefix (balance 0 at index -1) must be seeded. Time O(n), space O(n).
"""


def find_max_length(nums: list[int]) -> int:
    first_seen = {0: -1}
    balance = best = 0
    for i, bit in enumerate(nums):
        balance += 1 if bit == 1 else -1
        if balance in first_seen:
            best = max(best, i - first_seen[balance])
        else:
            first_seen[balance] = i
    return best

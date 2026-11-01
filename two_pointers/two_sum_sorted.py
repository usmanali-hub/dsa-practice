"""Two Sum II: input array is sorted.

Return the 1-based indices ``[i, j]`` (i < j) of the two numbers that add up to ``target``, or an
empty list when there is no such pair.

Approach: one pointer at each end. A sum that is too small can only grow by moving the left pointer
up, a sum that is too large can only shrink by moving the right pointer down, so each step discards
one element for good. Time O(n), space O(1), unlike the hash-map version of Two Sum (O(n) space).
"""


def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        if total < target:
            left += 1
        else:
            right -= 1
    return []

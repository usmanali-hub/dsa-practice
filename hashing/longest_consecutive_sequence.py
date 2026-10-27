"""Longest Consecutive Sequence.

Return the length of the longest run of consecutive integers that appear in ``nums`` (in any order).

Approach: put everything in a set and only start counting from numbers that begin a run, meaning
``n - 1`` is not in the set. Each number is then visited at most twice, so it is O(n) even though
there is a loop inside the loop. Sorting would be O(n log n).
"""


def longest_consecutive(nums: list[int]) -> int:
    values = set(nums)
    best = 0
    for n in values:
        if n - 1 in values:
            continue  # not the start of a run
        length = 1
        while n + length in values:
            length += 1
        best = max(best, length)
    return best

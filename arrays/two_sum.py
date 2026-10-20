"""Two Sum.

Given a list of integers and a target, return the indices of the two numbers
that add up to the target (exactly one solution is assumed).

Approach: one pass with a hash map of value -> index. For each number, check
whether its complement was already seen.
Time O(n), space O(n). Brute force is O(n^2) time, O(1) space.
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i
    raise ValueError("no two numbers add up to target")

"""Maximum Average Subarray I.

Return the largest average of any contiguous run of exactly ``k`` numbers.

Approach: a fixed-size window. Compute the first window's sum, then slide one step at a time by adding the
entering element and removing the leaving one, so each step costs O(1). Time O(n), space O(1).
Raises ValueError unless 1 <= k <= len(nums).
"""


def find_max_average(nums: list[int], k: int) -> float:
    if not 1 <= k <= len(nums):
        raise ValueError("k must be between 1 and len(nums)")
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        best = max(best, window)
    return best / k

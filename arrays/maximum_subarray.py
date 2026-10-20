"""Maximum Subarray (Kadane's algorithm).

Return the largest sum of any contiguous, non-empty subarray.

Approach: at each element, either extend the running subarray or start fresh
from the current element, whichever is larger; track the best seen.
Time O(n), space O(1). Brute force over all subarrays is O(n^2).
"""


def max_subarray(nums: list[int]) -> int:
    if not nums:
        raise ValueError("nums must be non-empty")
    current = best = nums[0]
    for n in nums[1:]:
        current = max(n, current + n)
        best = max(best, current)
    return best

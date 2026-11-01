"""3Sum Closest.

Return the sum of three numbers that is closest to ``target`` (the sum itself, not the numbers).

Approach: sort, fix the first number, sweep two pointers over the rest, and remember the best sum seen.
An exact match ends the search early. Time O(n^2), space O(1) beyond the sorted copy.
Raises ValueError for fewer than three numbers, because no sum exists.
"""


def three_sum_closest(nums: list[int], target: int) -> int:
    if len(nums) < 3:
        raise ValueError("need at least three numbers")
    nums = sorted(nums)
    best = nums[0] + nums[1] + nums[2]
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if abs(total - target) < abs(best - target):
                best = total
            if total == target:
                return total
            if total < target:
                left += 1
            else:
                right -= 1
    return best

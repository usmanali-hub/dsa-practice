"""3Sum.

Return all unique triplets in ``nums`` that sum to zero.

Approach: sort, fix the first number, then sweep two pointers inward over the rest. Too small a sum
moves the left pointer up, too large moves the right pointer down. Duplicates are skipped at all
three positions so each triplet appears once. Time O(n^2), space O(1) beyond the output.
"""


def three_sum(nums: list[int]) -> list[list[int]]:
    nums = sorted(nums)
    result: list[list[int]] = []
    for i, first in enumerate(nums):
        if first > 0:
            break  # everything after is positive too, so no triplet can reach zero
        if i > 0 and first == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = first + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([first, nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
    return result

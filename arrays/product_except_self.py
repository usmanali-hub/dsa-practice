"""Product of Array Except Self.

For each index, return the product of all other elements, without division.

Approach: prefix and suffix products. First pass stores the product of everything
to the left of i; second pass multiplies in the product of everything to the right.
Time O(n), space O(1) extra (the output list does not count).
"""


def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    out = [1] * n
    left = 1
    for i in range(n):
        out[i] = left
        left *= nums[i]
    right = 1
    for i in range(n - 1, -1, -1):
        out[i] *= right
        right *= nums[i]
    return out

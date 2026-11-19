"""Split Array Largest Sum (medium).

Split `nums` (non-negative integers, order preserved) into `k` contiguous, non-empty subarrays so that the largest
subarray sum is as small as possible. Return that minimum possible largest sum.

Approach: binary search the answer itself. For a candidate cap `c`, a greedy scan can check in O(n) whether `nums`
can be split into at most `k` pieces each summing to at most `c` (pack greedily; start a new piece when adding the
next element would exceed `c`). "Can split within c pieces" is monotonic in `c`, so binary search over
`[max(nums), sum(nums)]` for the smallest c that a feasible split achieves. Time O(n log(sum(nums))), space O(1).
"""


def pieces_needed(nums: list[int], cap: int) -> int:
    pieces, current = 1, 0
    for n in nums:
        if current + n > cap:
            pieces += 1
            current = n
        else:
            current += n
    return pieces


def split_array(nums: list[int], k: int) -> int:
    if not nums:
        raise ValueError("nums must not be empty")
    if not (1 <= k <= len(nums)):
        raise ValueError("k must be between 1 and len(nums)")
    lo, hi = max(nums), sum(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if pieces_needed(nums, mid) <= k:
            hi = mid
        else:
            lo = mid + 1
    return lo

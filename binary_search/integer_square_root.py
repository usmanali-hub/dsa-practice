"""Sqrt(x) (easy).

Return the integer part of the square root of a non-negative integer without using ``**0.5`` or ``math.sqrt``
(floating point loses exactness for large values).

Approach: binary search for the largest ``r`` with ``r * r <= x`` over ``[0, x]`` (for x >= 2 the answer is at most
``x // 2``, which halves the range). Time O(log x), space O(1). Python integers are exact, so there is no overflow.
"""


def integer_sqrt(x: int) -> int:
    if x < 0:
        raise ValueError("x must be non-negative")
    if x < 2:
        return x
    lo, hi = 1, x // 2
    while lo < hi:
        mid = (lo + hi + 1) // 2  # round up so the loop always shrinks when lo = mid
        if mid * mid <= x:
            lo = mid
        else:
            hi = mid - 1
    return lo

"""Square Root with k Decimal Places (easy/medium).

Given a non-negative number x and a precision k, return floor(sqrt(x) * 10**k) / 10**k as a float — the square root
truncated (not rounded) to k decimal places, without using math.sqrt.

Approach: binary search over scaled integers. Let scale = 10**k; search for the largest integer r with
r*r <= x * scale**2, over [0, (x+1) * scale] (a safe upper bound since (x+1)*scale >= sqrt(x)*scale for x >= 0).
Working entirely in integers avoids floating-point error creeping into the comparison. Time O(log(x * 10**k)),
space O(1).
"""


def sqrt_with_precision(x: float, k: int) -> float:
    if x < 0:
        raise ValueError("x must be non-negative")
    if k < 0:
        raise ValueError("k must be non-negative")
    scale = 10**k
    target = round(x * scale * scale)  # x * scale**2, as an exact integer
    lo, hi = 0, (int(x) + 1) * scale
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid * mid <= target:
            lo = mid
        else:
            hi = mid - 1
    return lo / scale

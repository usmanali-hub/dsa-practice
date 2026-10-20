"""Best Time to Buy and Sell Stock.

Given daily prices, return the maximum profit from one buy followed by one sell
(0 if no profit is possible).

Approach: single pass tracking the lowest price so far and the best profit if
selling today. Time O(n), space O(1). Brute force over all pairs is O(n^2).
"""


def max_profit(prices: list[int]) -> int:
    lowest = float("inf")
    best = 0
    for p in prices:
        lowest = min(lowest, p)
        best = max(best, p - lowest)
    return int(best)

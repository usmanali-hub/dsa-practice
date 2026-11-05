"""Best Time to Buy and Sell Stock.

Given daily prices, return the maximum profit from one buy followed by one later sell, or 0 if every
trade would lose money.

Approach: one pass tracking the lowest price seen so far. At each day the best sale ending today is
``price - lowest_so_far``; keep the largest. The "window" is the span from the cheapest earlier day to today,
and its left edge jumps to today whenever a new low appears. Time O(n), space O(1).
"""


def max_profit(prices: list[int]) -> int:
    best = 0
    lowest = None
    for price in prices:
        if lowest is None or price < lowest:
            lowest = price
        else:
            best = max(best, price - lowest)
    return best

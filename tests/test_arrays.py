import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from arrays.contains_duplicate import contains_duplicate
from arrays.two_sum import two_sum


@pytest.mark.parametrize(
    "nums,target,expected",
    [([2, 7, 11, 15], 9, [0, 1]), ([3, 2, 4], 6, [1, 2]), ([3, 3], 6, [0, 1]), ([-1, -2, -3, -4], -6, [1, 3])],
)
def test_two_sum(nums, target, expected):
    assert two_sum(nums, target) == expected


def test_two_sum_no_answer():
    with pytest.raises(ValueError):
        two_sum([1, 2], 10)


@pytest.mark.parametrize(
    "nums,expected", [([1, 2, 3, 1], True), ([1, 2, 3, 4], False), ([], False), ([5], False), ([0, 0], True)]
)
def test_contains_duplicate(nums, expected):
    assert contains_duplicate(nums) is expected


from arrays.best_time_to_buy_sell_stock import max_profit


@pytest.mark.parametrize(
    "prices,expected",
    [([7, 1, 5, 3, 6, 4], 5), ([7, 6, 4, 3, 1], 0), ([], 0), ([5], 0), ([1, 2], 1), ([2, 4, 1], 2)],
)
def test_max_profit(prices, expected):
    assert max_profit(prices) == expected

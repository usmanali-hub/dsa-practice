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


from arrays.maximum_subarray import max_subarray


@pytest.mark.parametrize(
    "nums,expected",
    [([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6), ([1], 1), ([5, 4, -1, 7, 8], 23), ([-3, -1, -2], -1), ([0, 0], 0)],
)
def test_max_subarray(nums, expected):
    assert max_subarray(nums) == expected


def test_max_subarray_empty():
    with pytest.raises(ValueError):
        max_subarray([])


from arrays.move_zeroes import move_zeroes


@pytest.mark.parametrize(
    "nums,expected",
    [([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]), ([0], [0]), ([1, 2, 3], [1, 2, 3]), ([0, 0, 1], [1, 0, 0]), ([], [])],
)
def test_move_zeroes(nums, expected):
    move_zeroes(nums)
    assert nums == expected


from arrays.product_except_self import product_except_self


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([2, 3], [3, 2]),
        ([0, 0, 2], [0, 0, 0]),
        ([5], [1]),
    ],
)
def test_product_except_self(nums, expected):
    assert product_except_self(nums) == expected


from arrays.container_with_most_water import max_area


@pytest.mark.parametrize(
    "heights,expected",
    [([1, 8, 6, 2, 5, 4, 8, 3, 7], 49), ([1, 1], 1), ([4, 3, 2, 1, 4], 16), ([1, 2, 1], 2), ([5], 0), ([], 0)],
)
def test_max_area(heights, expected):
    assert max_area(heights) == expected

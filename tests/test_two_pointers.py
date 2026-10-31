import itertools
import random
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from two_pointers.sorted_squares import sorted_squares
from two_pointers.three_sum import three_sum


@pytest.mark.parametrize(
    "nums,expected",
    [([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]), ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]), ([], []), ([5], [25]), ([-3, -3], [9, 9]), ([-5, -4, -3], [9, 16, 25])],
)
def test_sorted_squares(nums, expected):
    assert sorted_squares(nums) == expected


def test_sorted_squares_matches_square_and_sort():
    rng = random.Random(7)
    for _ in range(200):
        nums = sorted(rng.randint(-20, 20) for _ in range(rng.randint(0, 15)))
        assert sorted_squares(nums) == sorted(x * x for x in nums)


def test_sorted_squares_does_not_mutate_input():
    nums = [-2, 0, 3]
    sorted_squares(nums)
    assert nums == [-2, 0, 3]


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([], []),
        ([1, 2], []),
        ([-2, 0, 0, 2, 2], [[-2, 0, 2]]),
    ],
)
def test_three_sum_examples(nums, expected):
    assert three_sum(nums) == expected


def test_three_sum_matches_brute_force_and_has_no_duplicates():
    rng = random.Random(8)
    for _ in range(300):
        nums = [rng.randint(-5, 5) for _ in range(rng.randint(0, 12))]
        brute = sorted({tuple(sorted(t)) for t in itertools.combinations(nums, 3) if sum(t) == 0})
        got = three_sum(nums)
        assert sorted(tuple(t) for t in got) == brute
        assert len(got) == len(brute)  # each triplet exactly once


def test_three_sum_does_not_mutate_input():
    nums = [3, -1, -2, 0]
    three_sum(nums)
    assert nums == [3, -1, -2, 0]

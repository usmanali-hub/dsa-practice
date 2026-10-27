import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from hashing.longest_consecutive_sequence import longest_consecutive
from hashing.subarray_sum_equals_k import subarray_sum


@pytest.mark.parametrize(
    "nums,k,expected",
    [
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
        ([], 0, 0),
        ([0, 0, 0], 0, 6),  # every non-empty subarray sums to 0
        ([1, -1, 0], 0, 3),
        ([-1, -1, 1], 0, 1),
        ([5], 5, 1),
        ([5], 4, 0),
    ],
)
def test_subarray_sum(nums, k, expected):
    assert subarray_sum(nums, k) == expected


def brute_force(nums, k):
    return sum(1 for i in range(len(nums)) for j in range(i, len(nums)) if sum(nums[i : j + 1]) == k)


def test_subarray_sum_matches_brute_force_on_random_input():
    import random

    rng = random.Random(0)
    for _ in range(200):
        nums = [rng.randint(-3, 3) for _ in range(rng.randint(0, 12))]
        k = rng.randint(-4, 4)
        assert subarray_sum(nums, k) == brute_force(nums, k), (nums, k)


@pytest.mark.parametrize(
    "nums,expected",
    [([100, 4, 200, 1, 3, 2], 4), ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9), ([], 0), ([7], 1), ([1, 1, 1], 1), ([-2, -1, 0], 3), ([1, 3, 5], 1)],
)
def test_longest_consecutive(nums, expected):
    assert longest_consecutive(nums) == expected

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from hashing.isomorphic_strings import is_isomorphic
from hashing.longest_consecutive_sequence import longest_consecutive
from hashing.subarray_sum_equals_k import subarray_sum
from hashing.top_k_frequent import top_k_frequent


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


@pytest.mark.parametrize(
    "nums,k,expected",
    [([1, 1, 1, 2, 2, 3], 2, [1, 2]), ([1], 1, [1]), ([4, 4, 5, 5, 6], 2, [4, 5]), ([1, 2, 3], 3, [1, 2, 3]), ([1, 2], 0, []), ([], 3, [])],
)
def test_top_k_frequent(nums, k, expected):
    assert top_k_frequent(nums, k) == expected


def test_top_k_frequent_matches_counter_most_common_on_random_input():
    import random
    from collections import Counter

    rng = random.Random(1)
    for _ in range(100):
        nums = [rng.randint(0, 6) for _ in range(rng.randint(1, 30))]
        k = rng.randint(1, 4)
        got = top_k_frequent(nums, k)
        freqs = Counter(nums)
        assert len(set(got)) == len(got) == min(k, len(freqs))
        # every returned value is at least as frequent as every value left out
        assert min(freqs[v] for v in got) >= max((freqs[v] for v in freqs if v not in got), default=0)


@pytest.mark.parametrize(
    "s,t,expected",
    [("egg", "add", True), ("foo", "bar", False), ("paper", "title", True), ("ab", "aa", False), ("badc", "baba", False), ("", "", True), ("a", "ab", False)],
)
def test_is_isomorphic(s, t, expected):
    assert is_isomorphic(s, t) is expected

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from hashing.contains_duplicate_within_k import contains_nearby_duplicate
from hashing.contiguous_array import find_max_length
from hashing.four_sum_count import four_sum_count
from hashing.intersect_two_arrays import intersect
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


@pytest.mark.parametrize(
    "nums,k,expected",
    [([1, 2, 3, 1], 3, True), ([1, 0, 1, 1], 1, True), ([1, 2, 3, 1, 2, 3], 2, False), ([], 5, False), ([7], 0, False), ([5, 5], 0, False), ([5, 5], 1, True)],
)
def test_contains_nearby_duplicate(nums, k, expected):
    assert contains_nearby_duplicate(nums, k) is expected


def test_contains_nearby_duplicate_matches_brute_force():
    import random

    rng = random.Random(3)
    for _ in range(200):
        nums = [rng.randint(0, 8) for _ in range(rng.randint(0, 15))]
        k = rng.randint(0, 6)
        brute = any(nums[i] == nums[j] and j - i <= k for i in range(len(nums)) for j in range(i + 1, len(nums)))
        assert contains_nearby_duplicate(nums, k) is brute


def test_four_sum_count_known_cases():
    assert four_sum_count([1, 2], [-2, -1], [-1, 2], [0, 2]) == 2
    assert four_sum_count([0], [0], [0], [0]) == 1
    assert four_sum_count([1], [1], [1], [1]) == 0


def test_four_sum_count_matches_brute_force():
    import itertools
    import random

    rng = random.Random(4)
    for _ in range(50):
        lists = [[rng.randint(-3, 3) for _ in range(rng.randint(1, 5))] for _ in range(4)]
        brute = sum(1 for t in itertools.product(*lists) if sum(t) == 0)
        assert four_sum_count(*lists) == brute


@pytest.mark.parametrize(
    "a,b,expected",
    [([1, 2, 2, 1], [2, 2], [2, 2]), ([4, 9, 5], [9, 4, 9, 8, 4], [9, 4]), ([], [1], []), ([1, 1], [1], [1]), ([1, 2], [3, 4], [])],
)
def test_intersect_examples(a, b, expected):
    assert sorted(intersect(a, b)) == sorted(expected)


def test_intersect_matches_counter_intersection_on_random_input():
    import random
    from collections import Counter

    rng = random.Random(5)
    for _ in range(200):
        a = [rng.randint(0, 5) for _ in range(rng.randint(0, 12))]
        b = [rng.randint(0, 5) for _ in range(rng.randint(0, 12))]
        assert Counter(intersect(a, b)) == Counter(a) & Counter(b)
        assert Counter(intersect(a, b)) == Counter(intersect(b, a))


@pytest.mark.parametrize(
    "nums,expected",
    [([0, 1], 2), ([0, 1, 0], 2), ([0, 0, 1, 0, 0, 0, 1, 1], 6), ([], 0), ([1, 1, 1], 0), ([1, 0, 1, 0, 1, 0], 6)],
)
def test_find_max_length(nums, expected):
    assert find_max_length(nums) == expected


def test_find_max_length_matches_brute_force():
    import random

    rng = random.Random(6)
    for _ in range(300):
        nums = [rng.randint(0, 1) for _ in range(rng.randint(0, 16))]
        brute = max(
            (j - i for i in range(len(nums)) for j in range(i + 1, len(nums) + 1) if sum(nums[i:j]) * 2 == j - i),
            default=0,
        )
        assert find_max_length(nums) == brute

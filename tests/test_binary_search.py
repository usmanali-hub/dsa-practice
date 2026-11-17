import bisect
import math
import random
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from binary_search.first_last_position import search_range
from binary_search.integer_square_root import integer_sqrt
from binary_search.search_insert_position import search_insert
from binary_search.search_rotated_sorted_array import search


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [([], 5, 0), ([1], 0, 0), ([1], 1, 0), ([1], 2, 1), ([1, 3, 5, 6], 5, 2), ([1, 3, 5, 6], 2, 1), ([1, 3, 5, 6], 7, 4), ([1, 3, 5, 6], 0, 0)],
)
def test_search_insert_examples(nums, target, expected):
    assert search_insert(nums, target) == expected


def test_search_insert_matches_bisect_left_on_random_inputs():
    rng = random.Random(1)
    for _ in range(500):
        nums = sorted(rng.sample(range(-50, 50), rng.randint(0, 30)))
        target = rng.randint(-55, 55)
        assert search_insert(nums, target) == bisect.bisect_left(nums, target)


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [([4, 5, 6, 7, 0, 1, 2], 0, 4), ([4, 5, 6, 7, 0, 1, 2], 3, -1), ([1], 0, -1), ([1], 1, 0), ([], 1, -1), ([3, 1], 1, 1), ([5, 1, 3], 5, 0)],
)
def test_search_rotated_examples(nums, target, expected):
    assert search(nums, target) == expected


def test_search_rotated_finds_every_element_and_rejects_absent_ones_for_every_rotation():
    rng = random.Random(2)
    for n in range(1, 25):
        base = sorted(rng.sample(range(-100, 100), n))
        for k in range(n):
            nums = base[k:] + base[:k]
            for i, value in enumerate(nums):
                assert search(nums, value) == i
            assert search(nums, 1000) == -1 and search(nums, -1000) == -1
            absent = [x for x in range(-101, 101) if x not in nums][:5]
            assert all(search(nums, a) == -1 for a in absent)


@pytest.mark.parametrize(("x", "expected"), [(0, 0), (1, 1), (2, 1), (3, 1), (4, 2), (8, 2), (9, 3), (15, 3), (16, 4), (2147395599, 46339)])
def test_integer_sqrt_examples(x, expected):
    assert integer_sqrt(x) == expected


def test_integer_sqrt_matches_math_isqrt_including_perfect_squares_and_huge_values():
    for x in list(range(2000)) + [10**18, 10**18 - 1, (10**9 + 7) ** 2, (10**9 + 7) ** 2 - 1, 10**40 + 12345]:
        assert integer_sqrt(x) == math.isqrt(x)


def test_integer_sqrt_rejects_negative_numbers():
    with pytest.raises(ValueError):
        integer_sqrt(-1)


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [([5, 7, 7, 8, 8, 10], 8, [3, 4]), ([5, 7, 7, 8, 8, 10], 6, [-1, -1]), ([], 0, [-1, -1]), ([1], 1, [0, 0]), ([2, 2, 2, 2], 2, [0, 3]), ([1, 2, 3], 4, [-1, -1]), ([1, 2, 3], 0, [-1, -1])],
)
def test_search_range_examples(nums, target, expected):
    assert search_range(nums, target) == expected


def test_search_range_matches_bisect_on_random_inputs_with_many_duplicates():
    rng = random.Random(4)
    for _ in range(500):
        nums = sorted(rng.choice(range(8)) for _ in range(rng.randint(0, 25)))
        target = rng.randint(-1, 9)
        left, right = bisect.bisect_left(nums, target), bisect.bisect_right(nums, target)
        assert search_range(nums, target) == ([left, right - 1] if left < right else [-1, -1])

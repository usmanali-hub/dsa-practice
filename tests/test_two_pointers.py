import itertools
import random
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from two_pointers.remove_duplicates_sorted import remove_duplicates
from two_pointers.sorted_squares import sorted_squares
from two_pointers.three_sum import three_sum
from two_pointers.three_sum_closest import three_sum_closest
from two_pointers.trapping_rain_water import trap
from two_pointers.two_sum_sorted import two_sum_sorted


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


@pytest.mark.parametrize(
    "numbers,target,expected",
    [([2, 7, 11, 15], 9, [1, 2]), ([2, 3, 4], 6, [1, 3]), ([-1, 0], -1, [1, 2]), ([1, 2, 3], 100, []), ([], 3, []), ([5], 5, []), ([3, 3], 6, [1, 2])],
)
def test_two_sum_sorted(numbers, target, expected):
    assert two_sum_sorted(numbers, target) == expected


def test_two_sum_sorted_matches_brute_force():
    rng = random.Random(9)
    for _ in range(300):
        numbers = sorted(rng.randint(-8, 8) for _ in range(rng.randint(0, 10)))
        target = rng.randint(-12, 12)
        got = two_sum_sorted(numbers, target)
        exists = any(numbers[i] + numbers[j] == target for i in range(len(numbers)) for j in range(i + 1, len(numbers)))
        assert bool(got) == exists
        if got:
            i, j = got
            assert 1 <= i < j <= len(numbers) and numbers[i - 1] + numbers[j - 1] == target


@pytest.mark.parametrize(
    "nums,target,expected",
    [([-1, 2, 1, -4], 1, 2), ([0, 0, 0], 1, 0), ([1, 1, 1, 0], -100, 2), ([1, 1, 1, 0], 100, 3), ([-5, -4, -3], 0, -12)],
)
def test_three_sum_closest_examples(nums, target, expected):
    assert three_sum_closest(nums, target) == expected


def test_three_sum_closest_matches_brute_force():
    rng = random.Random(10)
    for _ in range(300):
        nums = [rng.randint(-10, 10) for _ in range(rng.randint(3, 10))]
        target = rng.randint(-30, 30)
        sums = [sum(t) for t in itertools.combinations(nums, 3)]
        got = three_sum_closest(nums, target)
        assert got in sums
        assert abs(got - target) == min(abs(s - target) for s in sums)


def test_three_sum_closest_needs_three_numbers():
    with pytest.raises(ValueError):
        three_sum_closest([1, 2], 3)


@pytest.mark.parametrize("nums,k", [([], 0), ([1], 1), ([1, 1, 2], 2), ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5), ([2, 2, 2], 1)])
def test_remove_duplicates_examples(nums, k):
    original = list(nums)
    assert remove_duplicates(nums) == k
    assert nums[:k] == sorted(set(original))


def test_remove_duplicates_matches_set_on_random_input():
    rng = random.Random(11)
    for _ in range(300):
        nums = sorted(rng.randint(-5, 5) for _ in range(rng.randint(0, 20)))
        expected = sorted(set(nums))
        k = remove_duplicates(nums)
        assert k == len(expected)
        assert nums[:k] == expected


@pytest.mark.parametrize(
    "height,expected",
    [([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6), ([4, 2, 0, 3, 2, 5], 9), ([], 0), ([3], 0), ([1, 2, 3], 0), ([3, 0, 3], 3)],
)
def test_trap_examples(height, expected):
    assert trap(height) == expected


def _trap_brute_force(height):
    return sum(max(0, min(max(height[: i + 1]), max(height[i:])) - h) for i, h in enumerate(height))


def test_trap_matches_brute_force():
    rng = random.Random(12)
    for _ in range(400):
        height = [rng.randint(0, 8) for _ in range(rng.randint(0, 15))]
        assert trap(height) == _trap_brute_force(height)


def test_trap_rejects_negative_heights():
    with pytest.raises(ValueError):
        trap([1, -1, 2])

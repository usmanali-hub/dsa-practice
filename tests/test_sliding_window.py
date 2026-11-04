import random
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from sliding_window.max_average_subarray import find_max_average
from sliding_window.min_size_subarray_sum import min_subarray_len


@pytest.mark.parametrize(
    "nums,k,expected",
    [([1, 12, -5, -6, 50, 3], 4, 12.75), ([5], 1, 5.0), ([-1, -2, -3], 2, -1.5), ([0, 0, 0], 3, 0.0), ([4, 2, 1, 3, 3], 5, 2.6)],
)
def test_find_max_average_examples(nums, k, expected):
    assert find_max_average(nums, k) == pytest.approx(expected)


def test_find_max_average_matches_brute_force():
    rng = random.Random(21)
    for _ in range(400):
        nums = [rng.randint(-20, 20) for _ in range(rng.randint(1, 15))]
        k = rng.randint(1, len(nums))
        brute = max(sum(nums[i : i + k]) for i in range(len(nums) - k + 1)) / k
        assert find_max_average(nums, k) == pytest.approx(brute)


@pytest.mark.parametrize("nums,k", [([1, 2, 3], 0), ([1, 2, 3], 4), ([], 1)])
def test_find_max_average_rejects_bad_window_sizes(nums, k):
    with pytest.raises(ValueError):
        find_max_average(nums, k)


@pytest.mark.parametrize(
    "target,nums,expected",
    [(7, [2, 3, 1, 2, 4, 3], 2), (4, [1, 4, 4], 1), (11, [1, 1, 1, 1, 1, 1, 1, 1], 0), (15, [1, 2, 3, 4, 5], 5), (3, [], 0), (1, [5], 1)],
)
def test_min_subarray_len_examples(target, nums, expected):
    assert min_subarray_len(target, nums) == expected


def test_min_subarray_len_matches_brute_force():
    rng = random.Random(22)
    for _ in range(500):
        nums = [rng.randint(1, 9) for _ in range(rng.randint(0, 14))]
        target = rng.randint(1, 40)
        lengths = [j - i for i in range(len(nums)) for j in range(i + 1, len(nums) + 1) if sum(nums[i:j]) >= target]
        assert min_subarray_len(target, nums) == (min(lengths) if lengths else 0)


@pytest.mark.parametrize("nums", [[1, 0, 2], [1, -1, 3]])
def test_min_subarray_len_rejects_non_positive_numbers(nums):
    with pytest.raises(ValueError):
        min_subarray_len(5, nums)

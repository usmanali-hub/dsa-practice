import bisect
import random
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

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

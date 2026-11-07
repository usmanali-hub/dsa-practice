import random
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from sliding_window.best_time_to_buy_sell_stock import max_profit
from sliding_window.contains_duplicate_ii import contains_nearby_duplicate
from sliding_window.longest_repeating_replacement import character_replacement
from sliding_window.longest_substring_no_repeat import length_of_longest_substring
from sliding_window.max_average_subarray import find_max_average
from sliding_window.max_consecutive_ones import longest_ones
from sliding_window.min_size_subarray_sum import min_subarray_len
from sliding_window.minimum_window_substring import min_window


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


@pytest.mark.parametrize(
    "prices,expected",
    [([7, 1, 5, 3, 6, 4], 5), ([7, 6, 4, 3, 1], 0), ([], 0), ([5], 0), ([2, 2, 2], 0), ([3, 2, 6, 5, 0, 3], 4), ([1, 2], 1)],
)
def test_max_profit_examples(prices, expected):
    assert max_profit(prices) == expected


def test_max_profit_matches_brute_force():
    rng = random.Random(35)
    for _ in range(500):
        prices = [rng.randint(0, 30) for _ in range(rng.randint(0, 12))]
        brute = max([0] + [prices[j] - prices[i] for i in range(len(prices)) for j in range(i + 1, len(prices))])
        assert max_profit(prices) == brute


@pytest.mark.parametrize(
    "s,expected",
    [("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3), ("", 0), ("a", 1), ("abba", 2), ("tmmzuxt", 5), ("dvdf", 3), ("a b a", 3)],
)
def test_longest_substring_examples(s, expected):
    assert length_of_longest_substring(s) == expected


def test_longest_substring_matches_brute_force():
    rng = random.Random(36)
    for _ in range(500):
        s = "".join(rng.choice("abcd") for _ in range(rng.randint(0, 14)))
        brute = max(
            [0] + [j - i for i in range(len(s)) for j in range(i + 1, len(s) + 1) if len(set(s[i:j])) == j - i]
        )
        assert length_of_longest_substring(s) == brute


@pytest.mark.parametrize(
    "nums,k,expected",
    [([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2, 6), ([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3, 10), ([], 2, 0), ([0, 0, 0], 0, 0), ([0, 0, 0], 5, 3), ([1, 1], 0, 2)],
)
def test_longest_ones_examples(nums, k, expected):
    assert longest_ones(nums, k) == expected


def test_longest_ones_rejects_negative_k():
    with pytest.raises(ValueError):
        longest_ones([1, 0], -1)


def test_longest_ones_matches_brute_force():
    rng = random.Random(37)
    for _ in range(500):
        nums = [rng.randint(0, 1) for _ in range(rng.randint(0, 14))]
        k = rng.randint(0, 4)
        brute = max(
            [0] + [j - i for i in range(len(nums)) for j in range(i + 1, len(nums) + 1) if nums[i:j].count(0) <= k]
        )
        assert longest_ones(nums, k) == brute


@pytest.mark.parametrize(
    "s,t,expected",
    [("ADOBECODEBANC", "ABC", "BANC"), ("a", "a", "a"), ("a", "aa", ""), ("", "a", ""), ("abc", "", ""), ("aab", "ab", "ab"), ("ab", "b", "b"), ("aa", "aa", "aa")],
)
def test_min_window_examples(s, t, expected):
    assert min_window(s, t) == expected


def test_min_window_matches_brute_force():
    rng = random.Random(38)
    for _ in range(500):
        s = "".join(rng.choice("abc") for _ in range(rng.randint(0, 12)))
        t = "".join(rng.choice("abc") for _ in range(rng.randint(1, 4)))
        need = {c: t.count(c) for c in set(t)}
        best = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                w = s[i:j]
                if all(w.count(c) >= n for c, n in need.items()) and (best == "" or len(w) < len(best)):
                    best = w
        assert min_window(s, t) == best


@pytest.mark.parametrize(
    "nums,k,expected",
    [([1, 2, 3, 1], 3, True), ([1, 0, 1, 1], 1, True), ([1, 2, 3, 1, 2, 3], 2, False), ([], 3, False), ([5, 5], 0, False), ([7], 1, False), ([1, 2, 1], 1, False)],
)
def test_contains_nearby_duplicate_examples(nums, k, expected):
    assert contains_nearby_duplicate(nums, k) is expected


def test_contains_nearby_duplicate_rejects_negative_k():
    with pytest.raises(ValueError):
        contains_nearby_duplicate([1], -1)


def test_contains_nearby_duplicate_matches_brute_force():
    rng = random.Random(39)
    for _ in range(600):
        nums = [rng.randint(0, 6) for _ in range(rng.randint(0, 12))]
        k = rng.randint(0, 5)
        brute = any(nums[i] == nums[j] for i in range(len(nums)) for j in range(i + 1, min(len(nums), i + k + 1)))
        assert contains_nearby_duplicate(nums, k) is brute


@pytest.mark.parametrize(
    "s,k,expected",
    [("ABAB", 2, 4), ("AABABBA", 1, 4), ("", 3, 0), ("A", 0, 1), ("ABC", 0, 1), ("ABC", 3, 3), ("AAAA", 0, 4), ("ABBB", 2, 4)],
)
def test_character_replacement_examples(s, k, expected):
    assert character_replacement(s, k) == expected


def test_character_replacement_rejects_negative_k():
    with pytest.raises(ValueError):
        character_replacement("A", -1)


def test_character_replacement_matches_brute_force():
    rng = random.Random(40)
    for _ in range(500):
        s = "".join(rng.choice("ABC") for _ in range(rng.randint(0, 12)))
        k = rng.randint(0, 4)
        brute = max(
            [0]
            + [
                j - i
                for i in range(len(s))
                for j in range(i + 1, len(s) + 1)
                if (j - i) - max(s[i:j].count(c) for c in set(s[i:j])) <= k
            ]
        )
        assert character_replacement(s, k) == brute

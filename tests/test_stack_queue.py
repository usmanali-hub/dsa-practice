import random
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from stack_queue.daily_temperatures import daily_temperatures
from stack_queue.valid_parentheses import is_valid


@pytest.mark.parametrize(
    "s,expected",
    [("()", True), ("()[]{}", True), ("(]", False), ("([)]", False), ("{[]}", True), ("", True), ("(", False), (")", False), ("a(b)c", True), ("((", False), ("}{", False)],
)
def test_is_valid_examples(s, expected):
    assert is_valid(s) is expected


def test_is_valid_matches_a_brute_force_reducer():
    rng = random.Random(41)
    for _ in range(800):
        s = "".join(rng.choice("()[]{}") for _ in range(rng.randint(0, 12)))
        reduced = s
        while any(p in reduced for p in ("()", "[]", "{}")):
            for p in ("()", "[]", "{}"):
                reduced = reduced.replace(p, "")
        assert is_valid(s) is (reduced == "")


@pytest.mark.parametrize(
    "temps,expected",
    [([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]), ([30, 40, 50, 60], [1, 1, 1, 0]), ([30, 60, 90], [1, 1, 0]), ([], []), ([50], [0]), ([60, 50, 40], [0, 0, 0]), ([50, 50, 50], [0, 0, 0])],
)
def test_daily_temperatures_examples(temps, expected):
    assert daily_temperatures(temps) == expected


def test_daily_temperatures_matches_brute_force():
    rng = random.Random(42)
    for _ in range(600):
        temps = [rng.randint(30, 40) for _ in range(rng.randint(0, 14))]
        brute = [next((j - i for j in range(i + 1, len(temps)) if temps[j] > temps[i]), 0) for i in range(len(temps))]
        assert daily_temperatures(temps) == brute

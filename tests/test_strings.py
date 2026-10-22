import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from strings.longest_substring_no_repeat import length_of_longest_substring
from strings.valid_palindrome import is_palindrome


@pytest.mark.parametrize(
    "s,expected",
    [("A man, a plan, a canal: Panama", True), ("race a car", False), ("", True), (" ", True), ("0P", False), ("ab_a", True)],
)
def test_is_palindrome(s, expected):
    assert is_palindrome(s) is expected


@pytest.mark.parametrize(
    "s,expected",
    [("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3), ("", 0), ("abba", 2), ("dvdf", 3), ("a", 1)],
)
def test_longest_substring(s, expected):
    assert length_of_longest_substring(s) == expected

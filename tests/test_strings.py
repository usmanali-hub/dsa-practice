import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from strings.group_anagrams import group_anagrams
from strings.longest_substring_no_repeat import length_of_longest_substring
from strings.valid_anagram import is_anagram
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


@pytest.mark.parametrize(
    "s,t,expected",
    [("anagram", "nagaram", True), ("rat", "car", False), ("", "", True), ("a", "ab", False), ("aab", "abb", False)],
)
def test_is_anagram(s, t, expected):
    assert is_anagram(s, t) is expected


def test_group_anagrams():
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert sorted(sorted(g) for g in result) == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]


def test_group_anagrams_edge_cases():
    assert group_anagrams([]) == []
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]

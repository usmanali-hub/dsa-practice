import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from strings.group_anagrams import group_anagrams
from strings.is_subsequence import is_subsequence
from strings.longest_common_prefix import longest_common_prefix
from strings.longest_substring_no_repeat import length_of_longest_substring
from strings.reverse_words import reverse_words
from strings.valid_anagram import is_anagram
from strings.valid_palindrome import is_palindrome
from strings.valid_parentheses import is_valid


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


@pytest.mark.parametrize(
    "words,expected",
    [(["flower", "flow", "flight"], "fl"), (["dog", "racecar", "car"], ""), ([], ""), (["solo"], "solo"), (["", "a"], ""), (["ab", "ab"], "ab")],
)
def test_longest_common_prefix(words, expected):
    assert longest_common_prefix(words) == expected


@pytest.mark.parametrize(
    "s,expected",
    [("()", True), ("()[]{}", True), ("(]", False), ("([)]", False), ("{[]}", True), ("", True), ("(", False), (")", False)],
)
def test_is_valid(s, expected):
    assert is_valid(s) is expected


@pytest.mark.parametrize(
    "s,expected",
    [("the sky is blue", "blue is sky the"), ("  hello   world  ", "world hello"), ("a", "a"), ("", ""), ("   ", "")],
)
def test_reverse_words(s, expected):
    assert reverse_words(s) == expected


@pytest.mark.parametrize(
    "s,t,expected",
    [("abc", "ahbgdc", True), ("axc", "ahbgdc", False), ("", "abc", True), ("a", "", False), ("", "", True), ("aa", "a", False)],
)
def test_is_subsequence(s, t, expected):
    assert is_subsequence(s, t) is expected

"""Reverse Words in a String.

Return the words of ``s`` in reverse order, separated by single spaces, with no leading or
trailing spaces. Runs of spaces between words collapse.

Approach: ``split()`` with no argument already skips extra whitespace, so reverse the list and
join it. Time O(n), space O(n).
"""


def reverse_words(s: str) -> str:
    return " ".join(reversed(s.split()))

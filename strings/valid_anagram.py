"""Valid Anagram.

Return True if ``t`` is a rearrangement of the letters in ``s``.

Approach: compare character counts. One Counter for ``s``, then subtract as ``t`` is read and fail
fast if a count goes negative. Sorting both strings also works but costs O(n log n).
Time O(n), space O(k) for k distinct characters.
"""

from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    counts = Counter(s)
    for ch in t:
        counts[ch] -= 1
        if counts[ch] < 0:
            return False
    return True

"""Is Subsequence.

Return True if ``s`` can be formed from ``t`` by deleting some characters without reordering the rest.

Approach: two pointers. Walk through ``t`` and advance the pointer in ``s`` whenever the characters
match; ``s`` is a subsequence if its pointer reaches the end. Time O(len(t)), space O(1).
"""


def is_subsequence(s: str, t: str) -> bool:
    i = 0
    for ch in t:
        if i < len(s) and s[i] == ch:
            i += 1
    return i == len(s)

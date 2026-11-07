"""Longest Repeating Character Replacement.

Given an uppercase string ``s`` and an integer ``k``, return the length of the longest substring that can be made
of one repeated letter by replacing at most ``k`` characters.

Approach: a variable-size window with a count per letter. A window is valid when ``length - (count of its most
frequent letter) <= k``. Grow the right edge; when the window becomes invalid move the left edge one step. The
maximum count only ever needs to grow: a stale (too large) maximum can never let the window exceed the best valid
size already found, so it is not recomputed on shrink. Time O(n), space O(1) for a fixed alphabet.
"""


def character_replacement(s: str, k: int) -> int:
    if k < 0:
        raise ValueError("k must be non-negative")
    counts: dict[str, int] = {}
    left = best = most = 0
    for right, ch in enumerate(s):
        counts[ch] = counts.get(ch, 0) + 1
        most = max(most, counts[ch])
        while (right - left + 1) - most > k:
            counts[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best

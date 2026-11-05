"""Longest Substring Without Repeating Characters.

Return the length of the longest substring of ``s`` in which no character appears twice.

Approach: a variable-size window with a map from character to the index where it was last seen. When the
character at ``right`` was last seen inside the current window, move ``left`` just past that earlier index,
so the window never contains a repeat. Each index is visited once. Time O(n), space O(k) for k distinct
characters.
"""


def length_of_longest_substring(s: str) -> int:
    last_seen: dict[str, int] = {}
    left = best = 0
    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        best = max(best, right - left + 1)
    return best

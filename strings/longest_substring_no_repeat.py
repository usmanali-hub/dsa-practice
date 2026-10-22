"""Longest Substring Without Repeating Characters.

Return the length of the longest substring with all distinct characters.

Approach: sliding window with a dict of each character's last seen index. When a character repeats
inside the window, move the window start just past its previous position.
Time O(n), space O(min(n, alphabet size)). Checking every substring is O(n^2) or worse.
"""


def length_of_longest_substring(s: str) -> int:
    last_seen: dict[str, int] = {}
    start = best = 0
    for i, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= start:
            start = last_seen[ch] + 1
        last_seen[ch] = i
        best = max(best, i - start + 1)
    return best

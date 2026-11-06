"""Minimum Window Substring.

Return the shortest substring of ``s`` that contains every character of ``t`` (with multiplicity), or an empty
string if there is none. If several windows tie, the leftmost is returned.

Approach: a variable-size window with a need-count per character and a counter of how many requirements are
still unmet. Grow the right edge until all are met, then shrink the left edge while they stay met, recording the
shortest window. Each edge moves forward at most n times. Time O(|s| + |t|), space O(k) for k distinct characters.
"""

from collections import Counter


def min_window(s: str, t: str) -> str:
    if not t or len(t) > len(s):
        return ""
    need = Counter(t)
    missing = len(t)
    left = 0
    best_start, best_len = 0, len(s) + 1
    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        if missing == 0:
            while need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            if right - left + 1 < best_len:
                best_start, best_len = left, right - left + 1
            need[s[left]] += 1
            missing += 1
            left += 1
    return "" if best_len > len(s) else s[best_start : best_start + best_len]

"""Isomorphic Strings.

Two strings are isomorphic if the characters of ``s`` can be replaced to get ``t`` with a
consistent one-to-one mapping (no two characters map to the same character, order preserved).

Approach: keep a mapping in each direction. A single s-to-t map is not enough, because "ab" and
"aa" would both look consistent. Time O(n), space O(k) for k distinct characters.
"""


def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    forward: dict[str, str] = {}
    backward: dict[str, str] = {}
    for a, b in zip(s, t):
        if forward.setdefault(a, b) != b or backward.setdefault(b, a) != a:
            return False
    return True

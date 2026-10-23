"""Group Anagrams.

Group words that are anagrams of each other.

Approach: words that are anagrams share the same sorted-letters key, so bucket them in a dict keyed
by that signature. Time O(n * k log k) for n words of length k; counting letters into a 26-tuple
instead makes the key O(k) for lowercase ASCII input. Space O(n * k).
"""

from collections import defaultdict


def group_anagrams(words: list[str]) -> list[list[str]]:
    groups: dict[str, list[str]] = defaultdict(list)
    for word in words:
        groups["".join(sorted(word))].append(word)
    return list(groups.values())

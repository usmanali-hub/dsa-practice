"""Longest Common Prefix.

Return the longest prefix shared by every string in the list.

Approach: take the first string as the candidate and shorten it until every other string starts
with it. Comparing column by column also works and stops at the first mismatch.
Time O(S) where S is the total number of characters, space O(1) beyond the result.
"""


def longest_common_prefix(words: list[str]) -> str:
    if not words:
        return ""
    prefix = words[0]
    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

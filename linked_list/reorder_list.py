"""Reorder List (medium).

Reorder L0 -> L1 -> ... -> Ln-1 -> Ln into L0 -> Ln -> L1 -> Ln-1 -> L2 -> ... in place.

Approach: find the middle with slow/fast pointers, cut the list there, reverse the second half, then interleave the two
halves, taking one node from each in turn. Time O(n), space O(1); the nodes are relinked, not copied.
"""

from linked_list.node import ListNode


def reorder_list(head: ListNode | None) -> None:
    if head is None or head.next is None:
        return
    slow, fast = head, head
    while fast.next is not None and fast.next.next is not None:
        assert slow.next is not None
        slow, fast = slow.next, fast.next.next
    second = slow.next
    slow.next = None  # cut: the first half keeps the extra node when the length is odd
    prev: ListNode | None = None
    while second is not None:
        second.next, prev, second = prev, second, second.next
    first: ListNode | None = head
    second = prev
    while second is not None:
        assert first is not None
        first_next, second_next = first.next, second.next
        first.next = second
        second.next = first_next
        first, second = first_next, second_next

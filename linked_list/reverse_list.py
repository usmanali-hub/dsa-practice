"""Reverse Linked List (easy).

Approach: walk the list once, pointing each node back at the one before it. Keep three names: the already-reversed
part (``prev``), the current node, and the saved ``next`` so the rest of the list is not lost when the pointer is
overwritten. Time O(n), space O(1).
"""

from linked_list.node import ListNode


def reverse_list(head: ListNode | None) -> ListNode | None:
    prev: ListNode | None = None
    while head is not None:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev

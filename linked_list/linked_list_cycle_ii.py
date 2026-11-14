"""Linked List Cycle II (medium): find the node where a cycle begins, or None.

Approach: Floyd's tortoise and hare. Move ``slow`` one step and ``fast`` two; if they ever meet there is a cycle,
otherwise ``fast`` reaches the end. At the meeting point, restart one pointer from the head and move both one step at
a time: they meet at the cycle's entrance. Why: let the tail before the cycle be a nodes and the cycle length c. At
the first meeting slow has walked a + k and fast 2(a + k), so a + k is a multiple of c; walking a more steps from the
meeting point therefore lands exactly on the entrance. Time O(n), space O(1).
"""

from linked_list.node import ListNode


def detect_cycle(head: ListNode | None) -> ListNode | None:
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next if slow else None
        fast = fast.next.next
        if slow is fast:
            ptr = head
            while ptr is not slow:
                assert ptr is not None and slow is not None
                ptr, slow = ptr.next, slow.next
            return ptr
    return None

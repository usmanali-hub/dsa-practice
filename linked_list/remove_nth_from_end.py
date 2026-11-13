"""Remove Nth Node From End of List (medium).

Approach: two pointers with a gap. Move ``fast`` n nodes ahead, then advance both until ``fast`` is on the last
node; ``slow`` is then just before the node to delete. A dummy head makes deleting the first node need no special
case. One pass, time O(n), space O(1).
"""

from linked_list.node import ListNode


def remove_nth_from_end(head: ListNode | None, n: int) -> ListNode | None:
    if n < 1:
        raise ValueError("n must be at least 1")
    dummy = ListNode(0, head)
    fast: ListNode | None = dummy
    for _ in range(n):
        fast = fast.next if fast else None
        if fast is None:
            raise ValueError("n is larger than the list length")
    slow = dummy
    while fast is not None and fast.next is not None:
        fast = fast.next
        assert slow.next is not None
        slow = slow.next
    assert slow.next is not None
    slow.next = slow.next.next
    return dummy.next

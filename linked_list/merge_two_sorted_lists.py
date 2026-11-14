"""Merge Two Sorted Lists (easy).

Approach: a dummy head and a tail pointer. Repeatedly attach the smaller front node of the two lists, then attach
whatever remains of the other list. Nodes are relinked, not copied. Taking from the first list on ties keeps the merge
stable. Time O(m + n), space O(1).
"""

from linked_list.node import ListNode


def merge_two_lists(a: ListNode | None, b: ListNode | None) -> ListNode | None:
    dummy = ListNode()
    tail = dummy
    while a is not None and b is not None:
        if b.val < a.val:
            tail.next, b = b, b.next
        else:
            tail.next, a = a, a.next
        tail = tail.next
    tail.next = a if a is not None else b
    return dummy.next

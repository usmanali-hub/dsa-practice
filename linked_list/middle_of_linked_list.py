"""Middle of the Linked List (easy).

Approach: slow and fast pointers. Fast moves two nodes per step and slow one, so when fast reaches the end slow is at
the middle. For an even length this returns the second of the two middle nodes. Time O(n), space O(1).
"""

from linked_list.node import ListNode


def middle_node(head: ListNode | None) -> ListNode | None:
    slow = fast = head
    while fast is not None and fast.next is not None:
        assert slow is not None
        slow, fast = slow.next, fast.next.next
    return slow

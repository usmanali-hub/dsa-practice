"""Palindrome Linked List (easy).

Approach: find the middle with slow/fast pointers, reverse the second half in place, compare it with the first half,
then restore the list so the caller's data is unchanged. Time O(n), space O(1) (copying values into a list would be O(n)
space). For an odd length the middle node is skipped because the second half starts after it.
"""

from linked_list.node import ListNode


def _reverse(head: ListNode | None) -> ListNode | None:
    prev: ListNode | None = None
    while head is not None:
        head.next, prev, head = prev, head, head.next
    return prev


def is_palindrome(head: ListNode | None) -> bool:
    slow = fast = head
    while fast is not None and fast.next is not None:
        assert slow is not None
        slow, fast = slow.next, fast.next.next
    second = _reverse(slow)  # for odd lengths slow is the middle; it ends the reversed half, so it is compared with itself
    left, right = head, second
    result = True
    while right is not None:
        assert left is not None
        if left.val != right.val:
            result = False
            break
        left, right = left.next, right.next
    _reverse(second)  # restore the original order
    return result

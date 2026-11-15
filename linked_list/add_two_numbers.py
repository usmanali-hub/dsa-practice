"""Add Two Numbers (medium).

Each list holds a non-negative integer with the least significant digit first. Add digit by digit with a carry, building
the result list as we go; the loop continues while either list has digits left or a carry remains, so unequal lengths
and a final carry (999 + 1 = 0001 -> 1000) need no special cases. Time O(max(m, n)), space O(1) beyond the output.
"""

from linked_list.node import ListNode


def add_two_numbers(a: ListNode | None, b: ListNode | None) -> ListNode | None:
    dummy = ListNode()
    tail = dummy
    carry = 0
    while a is not None or b is not None or carry:
        total = carry
        if a is not None:
            total += a.val
            a = a.next
        if b is not None:
            total += b.val
            b = b.next
        carry, digit = divmod(total, 10)
        tail.next = ListNode(digit)
        tail = tail.next
    return dummy.next

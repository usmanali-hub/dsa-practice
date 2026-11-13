"""Singly linked list node plus helpers used by the problems and their tests."""

from collections.abc import Iterable, Iterator


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def build(values: Iterable[int]) -> ListNode | None:
    """Build a list from values and return its head (None for no values)."""
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head: ListNode | None) -> list[int]:
    return list(iterate(head))


def iterate(head: ListNode | None) -> Iterator[int]:
    while head is not None:
        yield head.val
        head = head.next

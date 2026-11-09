"""Implement Queue using Stacks.

A first-in-first-out queue built from two last-in-first-out stacks.

Approach: push onto ``inbox``. To pop or peek, if ``outbox`` is empty move everything from ``inbox`` to ``outbox``
(which reverses the order, so the oldest item ends up on top). Each item moves at most once, so every operation is
amortised O(1) even though a single pop can cost O(n). Space O(n).
"""


class QueueUsingStacks:
    def __init__(self) -> None:
        self._inbox: list[int] = []
        self._outbox: list[int] = []

    def push(self, x: int) -> None:
        self._inbox.append(x)

    def _shift(self) -> None:
        if not self._outbox:
            while self._inbox:
                self._outbox.append(self._inbox.pop())

    def pop(self) -> int:
        self._shift()
        if not self._outbox:
            raise IndexError("pop from empty queue")
        return self._outbox.pop()

    def peek(self) -> int:
        self._shift()
        if not self._outbox:
            raise IndexError("peek from empty queue")
        return self._outbox[-1]

    def empty(self) -> bool:
        return not self._inbox and not self._outbox

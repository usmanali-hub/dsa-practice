"""Implement Stack using Queues.

A last-in-first-out stack built from a single first-in-first-out queue.

Approach: after appending a new value to the back of the queue, rotate the queue so every older value moves behind
it (pop from the front and append, ``len - 1`` times). The newest value is then at the front, so ``pop`` and ``top``
take the front. ``push`` costs O(n); ``pop``, ``top`` and ``empty`` are O(1). Space O(n).
"""

from collections import deque


class StackUsingQueues:
    def __init__(self) -> None:
        self._queue: deque[int] = deque()

    def push(self, x: int) -> None:
        self._queue.append(x)
        for _ in range(len(self._queue) - 1):
            self._queue.append(self._queue.popleft())

    def pop(self) -> int:
        if not self._queue:
            raise IndexError("pop from empty stack")
        return self._queue.popleft()

    def top(self) -> int:
        if not self._queue:
            raise IndexError("top of empty stack")
        return self._queue[0]

    def empty(self) -> bool:
        return not self._queue

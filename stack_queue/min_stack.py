"""Min Stack.

A stack that supports push, pop, top and the current minimum, all in O(1).

Approach: keep a second stack that records the minimum *at the time of each push* (the smaller of the new value and
the previous minimum). Popping removes from both stacks, so the minimum always reflects exactly the values still in
the stack. Every operation is O(1); space is O(n).
"""


class MinStack:
    def __init__(self) -> None:
        self._values: list[int] = []
        self._minima: list[int] = []

    def push(self, x: int) -> None:
        self._values.append(x)
        self._minima.append(x if not self._minima else min(x, self._minima[-1]))

    def pop(self) -> int:
        if not self._values:
            raise IndexError("pop from empty stack")
        self._minima.pop()
        return self._values.pop()

    def top(self) -> int:
        if not self._values:
            raise IndexError("top of empty stack")
        return self._values[-1]

    def get_min(self) -> int:
        if not self._minima:
            raise IndexError("minimum of empty stack")
        return self._minima[-1]

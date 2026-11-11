"""Next Greater Element II.

For each element of a circular array, return the first strictly greater value found when moving forward (wrapping
around), or -1 if there is none.

Approach: a monotonic stack of indices still waiting for a greater value, scanned over the array twice (indices 0 to
2n-1, taken modulo n) to simulate the wrap-around. During the first pass indices are pushed; in both passes a larger
value resolves everything smaller on the stack. Only the first pass pushes, so each index is pushed and popped at most
once. Time O(n), space O(n).
"""


def next_greater_circular(nums: list[int]) -> list[int]:
    n = len(nums)
    answer = [-1] * n
    waiting: list[int] = []
    for i in range(2 * n):
        value = nums[i % n]
        while waiting and nums[waiting[-1]] < value:
            answer[waiting.pop()] = value
        if i < n:
            waiting.append(i)
    return answer

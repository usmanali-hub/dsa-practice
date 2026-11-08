"""Daily Temperatures.

For each day, return how many days you must wait for a warmer temperature, or 0 if there is none.

Approach: a monotonic stack of indices whose temperatures are waiting for something warmer, kept in decreasing
order of temperature. When a day is warmer than the temperature at the top of the stack, that earlier day has found
its answer (the distance between the indices); pop and repeat. Each index is pushed and popped once.
Time O(n), space O(n).
"""


def daily_temperatures(temps: list[int]) -> list[int]:
    answer = [0] * len(temps)
    waiting: list[int] = []
    for day, t in enumerate(temps):
        while waiting and temps[waiting[-1]] < t:
            earlier = waiting.pop()
            answer[earlier] = day - earlier
        waiting.append(day)
    return answer

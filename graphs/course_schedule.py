"""Course Schedule (medium).

``prerequisites`` is a list of ``[course, prereq]`` pairs: ``course`` cannot be taken until ``prereq`` is done.
Return whether all ``num_courses`` courses can be finished at all — equivalent to asking whether the prerequisite
graph (course -> courses that depend on it) has a cycle; if it does, no valid order exists.

Approach: Kahn's algorithm (BFS topological sort by in-degree). Build an adjacency list and each course's
in-degree (how many prerequisites it still needs), seed a queue with every course that has none, and repeatedly
remove one, decrementing its dependents' in-degrees and enqueuing any that reach zero. If every course gets
processed this way, there was no cycle; if some are left over, they form (or depend on) one. Time O(V + E), space
O(V + E).
"""

from collections import deque


def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    adjacency: list[list[int]] = [[] for _ in range(num_courses)]
    in_degree = [0] * num_courses
    for course, prereq in prerequisites:
        adjacency[prereq].append(course)
        in_degree[course] += 1

    queue = deque(course for course in range(num_courses) if in_degree[course] == 0)
    processed = 0
    while queue:
        course = queue.popleft()
        processed += 1
        for dependent in adjacency[course]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)

    return processed == num_courses

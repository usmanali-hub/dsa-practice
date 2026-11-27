"""Network Delay Time (medium).

``times`` is a list of ``[source, target, weight]`` directed edges (weight = travel time, always positive). A
signal starts at node ``k``; return the time for it to reach every one of ``n`` nodes (1-indexed), or -1 if some
node is unreachable.

Approach: Dijkstra's algorithm with a min-heap, since all weights are positive. Pop the closest not-yet-finalized
node, relax its outgoing edges, repeat. The answer is the largest finalized distance (the last node to hear the
signal) once every reachable node is settled, or -1 if fewer than n nodes were ever reached. Time
O(E log V), space O(V + E).
"""

import heapq
from collections import defaultdict


def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
    graph: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for source, target, weight in times:
        graph[source].append((target, weight))

    distances: dict[int, int] = {}
    heap: list[tuple[int, int]] = [(0, k)]
    while heap:
        dist, node = heapq.heappop(heap)
        if node in distances:  # already finalized with an equal-or-shorter distance
            continue
        distances[node] = dist
        for neighbor, weight in graph[node]:
            if neighbor not in distances:
                heapq.heappush(heap, (dist + weight, neighbor))

    return max(distances.values()) if len(distances) == n else -1

"""Clone Graph (medium).

Given a reference to a node in a connected undirected graph, return a deep copy of the whole graph (every node and
every edge), with no shared nodes between the original and the copy.

Approach: DFS from the given node, keeping a dict from an original node to its already-made clone. On visiting a
node for the first time, create its clone and record it in the dict *before* recursing into its neighbors — this
is what makes a cycle (which every connected undirected graph with more than one edge has) terminate instead of
looping forever: a neighbor already being cloned is found in the dict and reused, not recreated. Time O(V + E),
space O(V) for the dict and the recursion stack.
"""

from __future__ import annotations


class GraphNode:
    def __init__(self, val: int = 0, neighbors: list[GraphNode] | None = None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: GraphNode | None) -> GraphNode | None:
    if node is None:
        return None
    cloned: dict[GraphNode, GraphNode] = {}

    def dfs(original: GraphNode) -> GraphNode:
        if original in cloned:
            return cloned[original]
        copy = GraphNode(original.val)
        cloned[original] = (
            copy  # recorded before recursing, so a cycle back to this node reuses it
        )
        copy.neighbors = [dfs(neighbor) for neighbor in original.neighbors]
        return copy

    return dfs(node)

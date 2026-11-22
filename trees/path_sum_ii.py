"""Path Sum II (medium).

Return every root-to-leaf path whose node values add up exactly to ``target``. A path only counts if it ends at a
leaf (a node with no children) — reaching the target sum partway down an internal node does not qualify.

Approach: DFS carrying the current path and running sum; at a leaf whose sum matches, record a copy of the path
(not the mutable list itself, since it keeps changing as the search backtracks). Time O(n^2) worst case (a skewed
tree where every node is on a matching path forces an O(n)-length copy at O(n) leaves), space O(h) besides the
output.
"""

from trees.node import TreeNode


def path_sum_ii(root: TreeNode | None, target: int) -> list[list[int]]:
    results: list[list[int]] = []
    path: list[int] = []

    def dfs(node: TreeNode | None, remaining: int) -> None:
        if node is None:
            return
        path.append(node.val)
        remaining -= node.val
        if node.left is None and node.right is None and remaining == 0:
            results.append(list(path))
        else:
            dfs(node.left, remaining)
            dfs(node.right, remaining)
        path.pop()

    dfs(root, target)
    return results

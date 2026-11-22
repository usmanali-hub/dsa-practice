"""Binary Tree Zigzag Level Order Traversal (easy/medium).

Return the tree's values level by level, left-to-right on even levels (0-indexed) and right-to-left on odd levels.

Approach: an ordinary BFS with a queue collects each level left-to-right; reversing every other level's list in
place avoids needing a deque or any left/right-aware insertion during the scan itself. Time O(n), space O(n) for
the queue and output.
"""

from trees.node import TreeNode


def zigzag_level_order(root: TreeNode | None) -> list[list[int]]:
    if root is None:
        return []
    levels: list[list[int]] = []
    queue = [root]
    while queue:
        level = [node.val for node in queue]
        if len(levels) % 2 == 1:
            level.reverse()
        levels.append(level)
        queue = [
            child
            for node in queue
            for child in (node.left, node.right)
            if child is not None
        ]
    return levels

"""Binary Tree Right Side View (medium).

Return the value of the rightmost node at each level, as seen standing to the right of the tree.

Approach: BFS level by level, keeping only the last node visited at each level (the rightmost one), since a plain
level-order traversal already visits every node left to right. Time O(n), space O(w) for the widest level's queue.
"""

from trees.node import TreeNode


def right_side_view(root: TreeNode | None) -> list[int]:
    if root is None:
        return []
    result: list[int] = []
    level = [root]
    while level:
        result.append(level[-1].val)
        next_level: list[TreeNode] = []
        for node in level:
            if node.left is not None:
                next_level.append(node.left)
            if node.right is not None:
                next_level.append(node.right)
        level = next_level
    return result

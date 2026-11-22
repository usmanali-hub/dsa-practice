"""Diameter of Binary Tree (easy).

The diameter is the length (in edges) of the longest path between any two nodes, which may or may not pass through
the root. For each node the longest path through it is left_height + right_height; the answer is the maximum of
that quantity over every node, not just the root.

Approach: one post-order pass that returns each subtree's height while updating a running best for the diameter
seen so far, so the tree is walked once instead of once per node. Time O(n), space O(h) for the recursion stack.
"""

from trees.node import TreeNode


def diameter_of_binary_tree(root: TreeNode | None) -> int:
    best = 0

    def height(node: TreeNode | None) -> int:
        nonlocal best
        if node is None:
            return 0
        left_height = height(node.left)
        right_height = height(node.right)
        best = max(best, left_height + right_height)
        return 1 + max(left_height, right_height)

    height(root)
    return best

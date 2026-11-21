"""Validate Binary Search Tree (easy).

Return True if the tree is a valid BST: every node's value is strictly between the bounds inherited from its
ancestors (not just greater than its immediate left child and less than its immediate right child, which a
local-only check would wrongly accept for some invalid trees).

Approach: recurse carrying a (low, high) exclusive bound for each node; a left child tightens the high bound to the
parent's value, a right child tightens the low bound. Time O(n), space O(h) for the recursion stack (h = tree
height).
"""

from trees.node import TreeNode


def is_valid_bst(root: TreeNode | None) -> bool:
    def valid(node: TreeNode | None, low: float, high: float) -> bool:
        if node is None:
            return True
        if not (low < node.val < high):
            return False
        return valid(node.left, low, node.val) and valid(node.right, node.val, high)

    return valid(root, float("-inf"), float("inf"))

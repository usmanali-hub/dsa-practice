"""Lowest Common Ancestor of a Binary Tree (medium).

Given a binary tree (not necessarily a BST) and two nodes p and q known to exist in it, return their lowest common
ancestor: the deepest node that has both p and q as descendants (a node can be its own descendant).

Approach: a node is the LCA if p and q are found in different subtrees of it, or if the node itself is p or q and
the other is found anywhere below. Recurse post-order: a call returns the node itself if it matches p or q, otherwise
whichever single match bubbles up from its children, or the node itself once both children report a match. Time
O(n) (one pass, every node visited once), space O(h) for the recursion stack.
"""

from trees.node import TreeNode


def lowest_common_ancestor(
    root: TreeNode | None, p: TreeNode, q: TreeNode
) -> TreeNode | None:
    if root is None or root is p or root is q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left is not None and right is not None:
        return root  # p and q were found in different subtrees of this node
    return left if left is not None else right

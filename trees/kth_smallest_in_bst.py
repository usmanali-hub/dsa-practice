"""Kth Smallest Element in a BST (medium).

A BST's inorder traversal visits nodes in sorted order, so the kth smallest value is simply the kth value an
inorder walk produces. The naive approach collects the whole traversal; this stops as soon as it reaches k,
without building the rest of the list.

Approach: an explicit stack doing inorder traversal (go left as far as possible, pop, count, go right), so the
walk can stop early. Time O(h + k) (h to descend to the leftmost node, then k pops), space O(h).
"""

from trees.node import TreeNode


def kth_smallest(root: TreeNode | None, k: int) -> int:
    stack: list[TreeNode] = []
    node = root
    count = 0
    while stack or node is not None:
        while node is not None:
            stack.append(node)
            node = node.left
        node = stack.pop()
        count += 1
        if count == k:
            return node.val
        node = node.right
    raise ValueError(f"tree has fewer than {k} nodes")

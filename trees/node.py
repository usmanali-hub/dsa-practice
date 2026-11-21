"""Binary tree node plus helpers used by the problems and their tests."""

from collections.abc import Iterator


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def build_level_order(values: list[int | None]) -> TreeNode | None:
    """Build a tree from a level-order list (LeetCode style: None marks a missing child; trailing Nones optional)."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values):
            left = values[i]
            i += 1
            if left is not None:
                node.left = TreeNode(left)
                queue.append(node.left)
        if i < len(values):
            right = values[i]
            i += 1
            if right is not None:
                node.right = TreeNode(right)
                queue.append(node.right)
    return root


def inorder(root: TreeNode | None) -> Iterator[int]:
    if root is None:
        return
    yield from inorder(root.left)
    yield root.val
    yield from inorder(root.right)

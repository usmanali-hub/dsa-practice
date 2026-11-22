"""Serialize and Deserialize Binary Tree (medium).

Turn a binary tree into a string and rebuild an identical tree from that string (structure and values, including
where nodes are missing — a tree is not identified by its values alone).

Approach: pre-order traversal, writing "#" for a missing child, comma-separated. Deserializing consumes the same
sequence in the same pre-order: a value starts a node and recursively builds its left then right subtree; a "#"
is a leaf's missing child. Time O(n) for both directions, space O(n) for the string and the recursion stack.
"""

from trees.node import TreeNode

NULL_MARKER = "#"


def serialize(root: TreeNode | None) -> str:
    tokens: list[str] = []

    def visit(node: TreeNode | None) -> None:
        if node is None:
            tokens.append(NULL_MARKER)
            return
        tokens.append(str(node.val))
        visit(node.left)
        visit(node.right)

    visit(root)
    return ",".join(tokens)


def deserialize(data: str) -> TreeNode | None:
    tokens = iter(data.split(","))

    def build() -> TreeNode | None:
        token = next(tokens)
        if token == NULL_MARKER:
            return None
        node = TreeNode(int(token))
        node.left = build()
        node.right = build()
        return node

    return build()

import random
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from trees.diameter_of_binary_tree import diameter_of_binary_tree
from trees.level_order import zigzag_level_order
from trees.lowest_common_ancestor import lowest_common_ancestor
from trees.node import TreeNode, build_level_order, inorder
from trees.path_sum_ii import path_sum_ii
from trees.serialize_deserialize import deserialize, serialize
from trees.validate_bst import is_valid_bst


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([2, 1, 3], True),
        ([5, 1, 4, None, None, 3, 6], False),  # 3 < 5 but is in the right subtree
        ([], True),
        ([1], True),
        (
            [10, 5, 15, None, None, 6, 20],
            False,
        ),  # 6 < 10 but lives under the right child
        ([1, 1], False),  # equal values are not valid (strict BST)
        ([2147483647], True),
    ],
)
def test_is_valid_bst_examples(values, expected):
    assert is_valid_bst(build_level_order(values)) == expected


def test_is_valid_bst_matches_sorted_inorder_on_random_valid_and_shuffled_trees():
    rng = random.Random(9)

    def insert(root, value):
        if root is None:
            return TreeNode(value)
        if value < root.val:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
        return root

    for _ in range(200):
        values = rng.sample(range(-100, 100), rng.randint(0, 15))
        root = None
        for v in values:
            root = insert(root, v)
        assert is_valid_bst(root) is True
        assert list(inorder(root)) == sorted(values)


def test_is_valid_bst_detects_a_single_swapped_subtree_value():
    # A valid BST with one right-subtree value swapped below the valid local range but outside the true ancestor bound
    root = build_level_order([8, 3, 10, 1, 6, 9, 14, None, None, 4, 7])
    assert is_valid_bst(root) is True
    root.left.right.left.val = (
        100  # 4 -> 100: still > 3 locally, but now > root.val, which must fail
    )
    assert is_valid_bst(root) is False


def find(root, value):
    if root is None:
        return None
    if root.val == value:
        return root
    return find(root.left, value) or find(root.right, value)


@pytest.mark.parametrize(
    ("values", "p_val", "q_val", "expected"),
    [
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3),
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5),
        ([1, 2], 1, 2, 1),
        ([1, 2, 3], 2, 3, 1),
    ],
)
def test_lowest_common_ancestor_examples(values, p_val, q_val, expected):
    root = build_level_order(values)
    p, q = find(root, p_val), find(root, q_val)
    assert lowest_common_ancestor(root, p, q).val == expected


def test_lca_of_a_node_and_itself_is_itself():
    root = build_level_order([1, 2, 3])
    node = find(root, 2)
    assert lowest_common_ancestor(root, node, node) is node


def test_lca_matches_brute_force_ancestor_paths_on_random_trees():
    rng = random.Random(10)

    def paths_from_root(node, path, acc):
        if node is None:
            return
        path = (*path, node)
        acc[node] = path
        paths_from_root(node.left, path, acc)
        paths_from_root(node.right, path, acc)

    def brute_force(root, p, q):
        acc: dict = {}
        paths_from_root(root, (), acc)
        set_p = set(acc[p])
        for ancestor in reversed(acc[q]):
            if ancestor in set_p:
                return ancestor
        raise AssertionError("no common ancestor found")

    for _ in range(100):
        size = rng.randint(2, 20)
        values = [rng.randint(0, 1000) for _ in range(size)]
        root = build_level_order(values)
        nodes = list(acc_nodes(root))
        p, q = rng.sample(nodes, 2)
        assert lowest_common_ancestor(root, p, q) is brute_force(root, p, q)


def acc_nodes(root):
    if root is None:
        return
    yield root
    yield from acc_nodes(root.left)
    yield from acc_nodes(root.right)


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([3, 9, 20, None, None, 15, 7], [[3], [20, 9], [15, 7]]),
        ([], []),
        ([1], [[1]]),
        ([1, 2, 3, 4, 5, 6, 7], [[1], [3, 2], [4, 5, 6, 7]]),
    ],
)
def test_zigzag_level_order_examples(values, expected):
    assert zigzag_level_order(build_level_order(values)) == expected


def test_zigzag_level_order_values_match_a_plain_bfs_ignoring_direction():
    rng = random.Random(11)
    for _ in range(100):
        values = [
            rng.randint(0, 50) if rng.random() > 0.3 else None
            for _ in range(rng.randint(0, 20))
        ]
        if not values or values[0] is None:
            continue
        root = build_level_order(values)
        zigzag = zigzag_level_order(root)
        plain_bfs: list[list[int]] = []
        queue = [root]
        while queue:
            plain_bfs.append([n.val for n in queue])
            queue = [c for n in queue for c in (n.left, n.right) if c is not None]
        assert [sorted(level) for level in zigzag] == [
            sorted(level) for level in plain_bfs
        ]
        assert all(
            level == (plain[::-1] if i % 2 else plain)
            for i, (level, plain) in enumerate(zip(zigzag, plain_bfs))
        )


@pytest.mark.parametrize(
    "values",
    [
        [1, 2, 3],
        [],
        [1],
        [1, None, 2, None, None, None, 3],
        [5, 4, 7, 3, None, 2, None, -1, None, 9],
    ],
)
def test_serialize_then_deserialize_round_trips(values):
    root = build_level_order(values)
    data = serialize(root)
    rebuilt = deserialize(data)
    assert serialize(rebuilt) == data


def test_serialize_distinguishes_trees_with_the_same_inorder_values():
    # A root with only a right child vs. only a left child have the same single value but different shape
    right_only = build_level_order([1, None, 2])
    left_only = build_level_order([1, 2])
    assert serialize(right_only) != serialize(left_only)


def test_serialize_deserialize_on_random_trees_preserves_structure_and_values():
    rng = random.Random(12)
    for _ in range(150):
        values = [
            rng.randint(-100, 100) if rng.random() > 0.25 else None
            for _ in range(rng.randint(0, 25))
        ]
        if values and values[0] is None:
            values[0] = rng.randint(-100, 100)
        root = build_level_order(values)
        data = serialize(root)
        rebuilt = deserialize(data)
        assert list(inorder(rebuilt)) == list(inorder(root))
        assert serialize(rebuilt) == data


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        (
            [1, 2, 3, 4, 5],
            3,
        ),  # longest path: 4 -> 2 -> 1 -> 3 or 4 -> 2 -> 5, both length 3
        ([1], 0),
        ([], 0),
        ([1, 2], 1),
        (
            [1, None, 2, None, None, None, 3],
            1,
        ),  # right child's right child: root-2-3 is the only path
    ],
)
def test_diameter_of_binary_tree(values, expected):
    assert diameter_of_binary_tree(build_level_order(values)) == expected


def test_diameter_can_pass_through_a_non_root_node():
    # the longest path, 6-5-2-1-3 (4 edges), passes through the root but is not simply left-height + right-height
    # of the root's immediate children — it runs through the deepest node of node 2's own subtree
    root = TreeNode(
        1, TreeNode(2, TreeNode(4), TreeNode(5, None, TreeNode(6))), TreeNode(3)
    )
    assert diameter_of_binary_tree(root) == 4


def test_path_sum_ii_finds_both_matching_root_to_leaf_paths():
    root = build_level_order([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    result = path_sum_ii(root, 22)
    assert sorted(result) == sorted([[5, 4, 11, 2], [5, 8, 4, 5]])


def test_path_sum_ii_returns_empty_list_when_no_path_matches():
    root = build_level_order([1, 2, 3])
    assert path_sum_ii(root, 100) == []


def test_path_sum_ii_requires_reaching_a_leaf_not_just_the_right_partial_sum():
    # 1 -> 2 sums to 3 but node 2 is not a leaf (it has a child 0), so that partial sum must not be reported;
    # only the full root-to-leaf path 1 -> 2 -> 0 (which also sums to 3) counts
    root = TreeNode(1, TreeNode(2, TreeNode(0)))
    assert path_sum_ii(root, 3) == [[1, 2, 0]]
    assert path_sum_ii(root, 100) == []


def test_path_sum_ii_single_node_tree():
    assert path_sum_ii(build_level_order([5]), 5) == [[5]]
    assert path_sum_ii(build_level_order([5]), 4) == []

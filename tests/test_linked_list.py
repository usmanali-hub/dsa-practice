import random
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from linked_list.add_two_numbers import add_two_numbers
from linked_list.linked_list_cycle_ii import detect_cycle
from linked_list.merge_two_sorted_lists import merge_two_lists
from linked_list.middle_of_linked_list import middle_node
from linked_list.node import ListNode, build, to_list
from linked_list.palindrome_linked_list import is_palindrome
from linked_list.remove_nth_from_end import remove_nth_from_end
from linked_list.reorder_list import reorder_list
from linked_list.reverse_list import reverse_list


def test_reverse_examples():
    assert to_list(reverse_list(build([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert to_list(reverse_list(build([1]))) == [1]
    assert reverse_list(None) is None


def test_reverse_matches_python_reversed_and_is_involutive():
    rng = random.Random(7)
    for _ in range(300):
        values = [rng.randint(-9, 9) for _ in range(rng.randint(0, 15))]
        assert to_list(reverse_list(build(values))) == values[::-1]
        assert to_list(reverse_list(reverse_list(build(values)))) == values


def test_remove_examples():
    assert to_list(remove_nth_from_end(build([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
    assert remove_nth_from_end(build([1]), 1) is None
    assert to_list(remove_nth_from_end(build([1, 2]), 2)) == [2]
    assert to_list(remove_nth_from_end(build([1, 2]), 1)) == [1]


def test_remove_matches_list_deletion():
    rng = random.Random(8)
    for _ in range(400):
        values = [rng.randint(0, 99) for _ in range(rng.randint(1, 12))]
        n = rng.randint(1, len(values))
        expected = values[: len(values) - n] + values[len(values) - n + 1 :]
        assert to_list(remove_nth_from_end(build(values), n)) == expected


def test_remove_rejects_bad_n():
    with pytest.raises(ValueError):
        remove_nth_from_end(build([1, 2]), 3)
    with pytest.raises(ValueError):
        remove_nth_from_end(build([1, 2]), 0)
    with pytest.raises(ValueError):
        remove_nth_from_end(None, 1)


def test_merge_examples():
    assert to_list(merge_two_lists(build([1, 2, 4]), build([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert merge_two_lists(None, None) is None
    assert to_list(merge_two_lists(None, build([0]))) == [0]
    assert to_list(merge_two_lists(build([5]), None)) == [5]


def test_merge_matches_sorted_concatenation_and_relinks_nodes():
    rng = random.Random(9)
    for _ in range(400):
        a = sorted(rng.randint(-5, 5) for _ in range(rng.randint(0, 8)))
        b = sorted(rng.randint(-5, 5) for _ in range(rng.randint(0, 8)))
        ha, hb = build(a), build(b)
        nodes = set()
        for h in (ha, hb):
            while h is not None:
                nodes.add(id(h))
                h = h.next
        out = merge_two_lists(ha, hb)
        assert to_list(out) == sorted(a + b)
        seen = set()
        while out is not None:
            seen.add(id(out))
            out = out.next
        assert seen == nodes  # same node objects, none created or lost


def test_merge_is_stable_on_ties():
    a, b = build([1, 1]), build([1])
    first_a, only_b = a, b
    out = merge_two_lists(a, b)
    assert out is first_a and out.next is not None and out.next.next is only_b


def make_cycle(values: list[int], entry: int | None) -> tuple[ListNode | None, ListNode | None]:
    head = build(values)
    if entry is None or head is None:
        return head, None
    nodes = []
    cur: ListNode | None = head
    while cur is not None:
        nodes.append(cur)
        cur = cur.next
    nodes[-1].next = nodes[entry]
    return head, nodes[entry]


def test_cycle_detection_finds_the_entrance_or_none():
    assert detect_cycle(None) is None
    assert detect_cycle(build([1])) is None
    head, entry = make_cycle([1], 0)
    assert detect_cycle(head) is entry
    head, entry = make_cycle([3, 2, 0, -4], 1)
    assert detect_cycle(head) is entry
    head, entry = make_cycle([1, 2], 0)
    assert detect_cycle(head) is entry


def test_cycle_detection_matches_a_visited_set_on_random_lists():
    rng = random.Random(10)
    for _ in range(500):
        n = rng.randint(0, 12)
        entry = rng.choice([None, *range(n)]) if n else None
        head, expected = make_cycle(list(range(n)), entry)
        assert detect_cycle(head) is expected


def test_palindrome_examples_and_the_list_is_left_unchanged():
    for values, expected in (([1, 2, 2, 1], True), ([1, 2], False), ([1], True), ([], True), ([1, 2, 1], True), ([1, 2, 3, 2, 2], False)):
        head = build(values)
        assert is_palindrome(head) is expected
        assert to_list(head) == values  # restored


def test_palindrome_matches_comparing_with_the_reversed_list():
    rng = random.Random(12)
    for _ in range(600):
        values = [rng.randint(0, 2) for _ in range(rng.randint(0, 10))]
        assert is_palindrome(build(values)) is (values == values[::-1])


def digits(n: int) -> list[int]:
    return [int(c) for c in str(n)[::-1]]


def test_add_two_numbers_examples():
    assert to_list(add_two_numbers(build([2, 4, 3]), build([5, 6, 4]))) == [7, 0, 8]
    assert to_list(add_two_numbers(build([0]), build([0]))) == [0]
    assert to_list(add_two_numbers(build([9, 9, 9]), build([1]))) == [0, 0, 0, 1]
    assert add_two_numbers(None, None) is None


def test_add_two_numbers_matches_integer_addition():
    rng = random.Random(13)
    for _ in range(500):
        x, y = rng.randint(0, 10**rng.randint(0, 12)), rng.randint(0, 10**rng.randint(0, 12))
        assert to_list(add_two_numbers(build(digits(x)), build(digits(y)))) == digits(x + y)


@pytest.mark.parametrize(
    ("values", "expected"),
    [([], []), ([1], [1]), ([1, 2], [2]), ([1, 2, 3], [2, 3]), ([1, 2, 3, 4], [3, 4]), ([1, 2, 3, 4, 5], [3, 4, 5]), ([1, 2, 3, 4, 5, 6], [4, 5, 6])],
)
def test_middle_node_returns_second_middle_for_even_lengths(values, expected):
    assert to_list(middle_node(build(values))) == expected


def test_middle_node_is_the_node_at_index_n_div_2():
    for n in range(1, 40):
        head = build(range(n))
        assert middle_node(head).val == n // 2


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([], []),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([1, 2, 3], [1, 3, 2]),
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
    ],
)
def test_reorder_list_examples(values, expected):
    head = build(values)
    reorder_list(head)
    assert to_list(head) == expected


def test_reorder_list_matches_a_simple_reference_and_keeps_the_same_nodes():
    for n in range(60):
        values = list(range(n))
        head = build(values)
        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next
        reorder_list(head)
        expected = []
        lo, hi = 0, n - 1
        while lo <= hi:
            expected.append(values[lo])
            if lo != hi:
                expected.append(values[hi])
            lo, hi = lo + 1, hi - 1
        assert to_list(head) == expected
        seen = []
        node = head
        while node:
            seen.append(node)
            node = node.next
        assert sorted(map(id, seen)) == sorted(map(id, nodes))

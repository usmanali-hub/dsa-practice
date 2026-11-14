import random
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from linked_list.linked_list_cycle_ii import detect_cycle
from linked_list.merge_two_sorted_lists import merge_two_lists
from linked_list.node import ListNode, build, to_list
from linked_list.remove_nth_from_end import remove_nth_from_end
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

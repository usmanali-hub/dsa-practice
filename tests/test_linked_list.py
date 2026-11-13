import random
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from linked_list.node import build, to_list
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

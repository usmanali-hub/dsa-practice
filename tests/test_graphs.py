import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from graphs.course_schedule import can_finish
from graphs.number_of_islands import num_islands


def test_num_islands_counts_disjoint_groups():
    grid = [
        list("11000"),
        list("11000"),
        list("00100"),
        list("00011"),
    ]
    assert num_islands(grid) == 3


def test_num_islands_only_counts_4_directional_connections_not_diagonal():
    # two land cells touching only at a corner are two separate islands
    grid = [
        list("10"),
        list("01"),
    ]
    assert num_islands(grid) == 2


def test_num_islands_all_water_is_zero_islands():
    grid = [list("000"), list("000")]
    assert num_islands(grid) == 0


def test_num_islands_all_land_is_one_island():
    grid = [list("11"), list("11")]
    assert num_islands(grid) == 1


def test_num_islands_empty_grid():
    assert num_islands([]) == 0
    assert num_islands([[]]) == 0


def test_num_islands_handles_a_grid_too_large_for_plain_recursion():
    # one single island filling a 200x200 grid; a naive recursive flood fill would blow the recursion limit here
    size = 200
    grid = [["1"] * size for _ in range(size)]
    assert num_islands(grid) == 1


def test_can_finish_returns_true_for_a_valid_prerequisite_chain():
    assert can_finish(2, [[1, 0]]) is True


def test_can_finish_returns_false_for_a_direct_cycle():
    assert can_finish(2, [[1, 0], [0, 1]]) is False


def test_can_finish_returns_false_for_a_longer_cycle():
    assert can_finish(3, [[1, 0], [2, 1], [0, 2]]) is False


def test_can_finish_with_no_prerequisites_is_always_true():
    assert can_finish(5, []) is True


def test_can_finish_handles_courses_outside_any_cycle():
    # courses 2 and 3 form a cycle; course 4 (which depends on nothing problematic) must not make the whole thing
    # look solvable, nor should the unrelated course 4 falsely register as part of the cycle
    assert can_finish(5, [[1, 0], [2, 3], [3, 2]]) is False

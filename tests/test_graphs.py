import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from graphs.clone_graph import GraphNode, clone_graph
from graphs.course_schedule import can_finish
from graphs.network_delay_time import network_delay_time
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


def _edges(node):
    seen = set()
    stack = [node]
    edges = set()
    while stack:
        current = stack.pop()
        if id(current) in seen:
            continue
        seen.add(id(current))
        for neighbor in current.neighbors:
            edges.add(frozenset((current.val, neighbor.val)))
            stack.append(neighbor)
    return edges


def _build_graph(adjacency: dict[int, list[int]]) -> dict[int, GraphNode]:
    nodes = {val: GraphNode(val) for val in adjacency}
    for val, neighbors in adjacency.items():
        nodes[val].neighbors = [nodes[n] for n in neighbors]
    return nodes


def test_clone_graph_produces_separate_nodes_with_the_same_edges():
    nodes = _build_graph({1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]})
    clone = clone_graph(nodes[1])
    assert clone is not nodes[1]
    assert _edges(clone) == _edges(nodes[1])


def test_clone_graph_handles_a_cycle_without_infinite_recursion():
    # a triangle: 1-2-3-1; cloning must terminate and preserve all three edges
    nodes = _build_graph({1: [2, 3], 2: [1, 3], 3: [1, 2]})
    clone = clone_graph(nodes[1])
    assert _edges(clone) == {frozenset((1, 2)), frozenset((1, 3)), frozenset((2, 3))}


def test_clone_graph_single_node_with_no_neighbors():
    single = GraphNode(1)
    clone = clone_graph(single)
    assert clone is not single
    assert clone.val == 1
    assert clone.neighbors == []


def test_clone_graph_of_none_is_none():
    assert clone_graph(None) is None


def test_network_delay_time_returns_the_slowest_finalized_distance():
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    assert network_delay_time(times, n=4, k=2) == 2


def test_network_delay_time_returns_minus_one_when_a_node_is_unreachable():
    times = [[1, 2, 1]]
    assert (
        network_delay_time(times, n=3, k=1) == -1
    )  # node 3 has no incoming edge at all


def test_network_delay_time_picks_the_shorter_of_two_paths_to_the_same_node():
    # 1 -> 2 direct costs 10; 1 -> 3 -> 2 costs 1 + 1 = 2, which must win
    times = [[1, 2, 10], [1, 3, 1], [3, 2, 1]]
    assert network_delay_time(times, n=3, k=1) == 2


def test_network_delay_time_single_node_with_itself_as_source():
    assert network_delay_time([], n=1, k=1) == 0

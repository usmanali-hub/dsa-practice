import random
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from stack_queue.daily_temperatures import daily_temperatures
from stack_queue.eval_rpn import eval_rpn
from stack_queue.largest_rectangle_histogram import largest_rectangle
from stack_queue.min_stack import MinStack
from stack_queue.queue_using_stacks import QueueUsingStacks
from stack_queue.valid_parentheses import is_valid


@pytest.mark.parametrize(
    "s,expected",
    [("()", True), ("()[]{}", True), ("(]", False), ("([)]", False), ("{[]}", True), ("", True), ("(", False), (")", False), ("a(b)c", True), ("((", False), ("}{", False)],
)
def test_is_valid_examples(s, expected):
    assert is_valid(s) is expected


def test_is_valid_matches_a_brute_force_reducer():
    rng = random.Random(41)
    for _ in range(800):
        s = "".join(rng.choice("()[]{}") for _ in range(rng.randint(0, 12)))
        reduced = s
        while any(p in reduced for p in ("()", "[]", "{}")):
            for p in ("()", "[]", "{}"):
                reduced = reduced.replace(p, "")
        assert is_valid(s) is (reduced == "")


@pytest.mark.parametrize(
    "temps,expected",
    [([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]), ([30, 40, 50, 60], [1, 1, 1, 0]), ([30, 60, 90], [1, 1, 0]), ([], []), ([50], [0]), ([60, 50, 40], [0, 0, 0]), ([50, 50, 50], [0, 0, 0])],
)
def test_daily_temperatures_examples(temps, expected):
    assert daily_temperatures(temps) == expected


def test_daily_temperatures_matches_brute_force():
    rng = random.Random(42)
    for _ in range(600):
        temps = [rng.randint(30, 40) for _ in range(rng.randint(0, 14))]
        brute = [next((j - i for j in range(i + 1, len(temps)) if temps[j] > temps[i]), 0) for i in range(len(temps))]
        assert daily_temperatures(temps) == brute


def test_queue_using_stacks_matches_a_deque_on_random_operations():
    from collections import deque

    rng = random.Random(43)
    for _ in range(200):
        q, ref = QueueUsingStacks(), deque()
        for _ in range(60):
            op = rng.choice(["push", "push", "pop", "peek"])
            if op == "push":
                x = rng.randint(0, 99)
                q.push(x)
                ref.append(x)
            elif ref:
                assert (q.pop() if op == "pop" else q.peek()) == (ref.popleft() if op == "pop" else ref[0])
            assert q.empty() is (not ref)


def test_queue_using_stacks_empty_errors():
    q = QueueUsingStacks()
    with pytest.raises(IndexError):
        q.pop()
    with pytest.raises(IndexError):
        q.peek()


@pytest.mark.parametrize(
    "tokens,expected",
    [(["2", "1", "+", "3", "*"], 9), (["4", "13", "5", "/", "+"], 6), (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
     (["7", "-2", "/"], -3), (["-7", "2", "/"], -3), (["5"], 5), (["3", "4", "-"], -1)],
)
def test_eval_rpn_examples(tokens, expected):
    assert eval_rpn(tokens) == expected


def test_eval_rpn_matches_python_eval_on_random_expressions():
    rng = random.Random(44)

    def build(depth):
        if depth == 0 or rng.random() < 0.25:
            n = rng.randint(1, 9)
            return [str(n)], str(n)
        lt, le = build(depth - 1)
        rt, re_ = build(depth - 1)
        op = rng.choice("+-*")
        return lt + rt + [op], f"({le}{op}{re_})"

    for _ in range(300):
        toks, expr = build(4)
        assert eval_rpn(toks) == eval(expr)


def test_min_stack_tracks_the_minimum_of_what_remains():
    rng = random.Random(45)
    for _ in range(200):
        st, ref = MinStack(), []
        for _ in range(60):
            if ref and rng.random() < 0.4:
                assert st.pop() == ref.pop()
            else:
                x = rng.randint(-20, 20)
                st.push(x)
                ref.append(x)
            if ref:
                assert st.top() == ref[-1] and st.get_min() == min(ref)


def test_min_stack_empty_errors():
    st = MinStack()
    for call in (st.pop, st.top, st.get_min):
        with pytest.raises(IndexError):
            call()


@pytest.mark.parametrize("heights,expected", [([2, 1, 5, 6, 2, 3], 10), ([2, 4], 4), ([], 0), ([5], 5), ([3, 3, 3], 9), ([6, 5, 4, 3], 12), ([0, 0], 0)])
def test_largest_rectangle_examples(heights, expected):
    assert largest_rectangle(heights) == expected


def test_largest_rectangle_matches_brute_force():
    rng = random.Random(46)
    for _ in range(500):
        h = [rng.randint(0, 9) for _ in range(rng.randint(0, 12))]
        brute = max((min(h[i : j + 1]) * (j - i + 1) for i in range(len(h)) for j in range(i, len(h))), default=0)
        assert largest_rectangle(h) == brute

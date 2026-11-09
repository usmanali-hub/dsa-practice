"""Evaluate Reverse Polish Notation.

Evaluate an expression in postfix form with + - * / where division truncates toward zero.

Approach: scan the tokens with a stack of operands. A number is pushed; an operator pops the right operand, then the
left one (order matters for - and /), and pushes the result. The stack ends with the single answer.
Python's // floors toward minus infinity, so division is done on absolute values and the sign restored, which
truncates toward zero without float rounding. Time O(n), space O(n).
"""


def _divide(a: int, b: int) -> int:
    q = abs(a) // abs(b)
    return q if (a >= 0) == (b >= 0) else -q


def eval_rpn(tokens: list[str]) -> int:
    stack: list[int] = []
    for tok in tokens:
        if tok in ("+", "-", "*", "/"):
            right, left = stack.pop(), stack.pop()
            if tok == "+":
                stack.append(left + right)
            elif tok == "-":
                stack.append(left - right)
            elif tok == "*":
                stack.append(left * right)
            else:
                stack.append(_divide(left, right))
        else:
            stack.append(int(tok))
    if len(stack) != 1:
        raise ValueError("malformed expression")
    return stack[0]

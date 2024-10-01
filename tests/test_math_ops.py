from math_lib.math_ops import MathOps


def test_add_op():
    math_ops = MathOps()
    assert math_ops.add(2, 3), 5

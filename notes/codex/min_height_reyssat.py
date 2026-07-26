"""Exact bounded search for the minimum nondegenerate derivative height.

The triple is (2, 3^10*109, 23^5).  Integer arithmetic only.
"""

from fractions import Fraction

A = 21_454_470
B = 59_049
C = 1_399_205
ABC_OVER_R = 5_508_110_403


def wronskian(x2: int, x3: int, x109: int) -> int:
    a = 2
    b = 6_436_341
    value = a * b * (
        Fraction(10 * x3, 3) + Fraction(x109, 109) - Fraction(x2, 2)
    )
    assert value.denominator == 1
    return value.numerator


def find_below(limit: int):
    best = None
    for x3 in range(-limit, limit + 1):
        for x23 in range(-limit, limit + 1):
            target = C * x23 - A * x3
            quotient = target // B
            for x109 in (quotient, quotient + 1):
                x2 = target - B * x109
                if max(abs(x2), abs(x3), abs(x109), abs(x23)) > limit:
                    continue
                w = wronskian(x2, x3, x109)
                if w:
                    candidate = (x2, x3, x109, x23, w)
                    if best is None or max(map(abs, candidate[:4])) < max(
                        map(abs, best[:4])
                    ):
                        best = candidate
    return best


assert find_below(600) is None
solution = find_below(601)
assert solution == (601, -38, -79, -586, -ABC_OVER_R)
print(solution)

"""Verify pointwise bounds for C/rad(3B_2n) using exact division polynomials."""
from functools import cache
from math import isqrt

try:
    from flint import fmpz as Integer
except ImportError:
    Integer = int


@cache
def division_value(n):
    if n < 5:
        return Integer((0, 1, 1, -37, -70)[n])
    m = n // 2
    if n % 2:
        left = division_value(m + 2) * division_value(m) ** 3
        right = division_value(m - 1) * division_value(m + 1) ** 3
        return left - 144 * right if m % 2 else 144 * left - right
    return division_value(m) * (
        division_value(m + 2) * division_value(m - 1) ** 2
        - division_value(m - 2) * division_value(m + 1) ** 2
    )


def verify(n, lower_factor, expected_bits, expected_milli):
    w = abs(division_value(n))
    a_squared = w*w + 12*division_value(n - 1)*division_value(n + 1)
    numerator = 4*lower_factor**2*w**6*10**6
    denominator = 3*a_squared*(4*w**4 - a_squared**2)
    floor_milli = isqrt(int(numerator // denominator))
    assert (4*w**4).bit_length() == expected_bits
    assert floor_milli == expected_milli
    assert floor_milli**2 * denominator <= numerator < (floor_milli + 1)**2 * denominator
    print(n, lower_factor, expected_bits, floor_milli)


if __name__ == "__main__":
    cases = [
        (9, 9, 207, 145497),
        (27, 27, 1869, 145869),
        (53, 211, 7202, 138930),
        (159, 633, 64822, 1209819),
        (891, 891, 2035537, 6001264),
        (1551, 1551, 6168039, 75401973),
    ]
    for case in cases:
        verify(*case)

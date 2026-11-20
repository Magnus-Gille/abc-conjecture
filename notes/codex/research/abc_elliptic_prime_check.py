"""Check first occurrences of squared good primes in four elliptic denominators.

Requires the Python packages cypari and sympy. The optional argument is an
inclusive upper bound for primes (default 100000).
"""

import argparse
from fractions import Fraction

from cypari import pari
from sympy import primerange


N = 29274
COEFFICIENT = 4 * N**2
POINTS = (
    (1771077, 2356659459),
    (142188, 52467372),
    (171462, 69956496),
    (313650, 174891240),
)


def isogenous_points():
    curve = pari.ellinit([0, 0, 0, -N**2, 0])
    for point in POINTS:
        x, y = pari.ellmul(curve, list(point), 4)
        yield Fraction(str(x - N**2 / x)), Fraction(str(y * (1 + N**2 / x**2)))


def affine_multiple_before_order(point, scalar, modulus):
    """Positive scalar strictly below the order of point modulo the prime."""
    x, y = point
    u, v = point
    for bit in bin(scalar)[3:]:
        slope = (3 * u**2 + COEFFICIENT) * pow(2 * v, -1, modulus) % modulus
        new_x = (slope**2 - 2 * u) % modulus
        u, v = new_x, (slope * (u - new_x) - v) % modulus
        if bit == "1":
            slope = (y - v) * pow(x - u, -1, modulus) % modulus
            new_x = (slope**2 - x - u) % modulus
            u, v = new_x, (slope * (u - new_x) - v) % modulus
    return u, v


def reduce_point(point, modulus):
    return tuple(q.numerator * pow(q.denominator, -1, modulus) % modulus for q in point)


def first_depth(curve_mod_p, point, prime):
    x, _ = point
    if x.denominator % prime == 0:
        denominator = x.denominator
        depth = 0
        while denominator % (prime * prime) == 0:
            denominator //= prime * prime
            depth += 1
        assert denominator % prime != 0
        return 1, depth

    order = int(pari.ellorder(curve_mod_p, list(reduce_point(point, prime))))
    assert order >= 2
    depth = 1
    modulus = prime**2
    while True:
        u, v = reduce_point(point, modulus)
        previous = affine_multiple_before_order((u, v), order - 1, modulus)
        assert previous[0] % prime == u % prime and (previous[1] + v) % prime == 0
        if previous != (u, -v % modulus):
            return order, depth
        depth += 1
        modulus *= prime


def run(bound):
    points = list(isogenous_points())
    good_primes = 0
    hits = [[] for _ in points]
    for prime in primerange(3, bound + 1):
        if N % prime == 0:
            continue
        curve = pari.ellinit([0, 0, 0, COEFFICIENT, 0], prime)
        good_primes += 1
        for index, point in enumerate(points):
            order, depth = first_depth(curve, point, prime)
            if depth >= 2:
                hits[index].append((prime, order, depth))
    return good_primes, hits


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bound", type=int, default=100000, nargs="?")
    count, rows = run(parser.parse_args().bound)
    print(f"{count} good primes checked. Rows give (prime, first index, exponent).")
    for index, row in enumerate(rows, 1):
        print(index, row)

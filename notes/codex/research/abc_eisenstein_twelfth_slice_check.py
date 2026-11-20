"""Exact checks for the elliptic slice. Run with Python 3, using its standard library."""

from fractions import Fraction
from math import isqrt, lcm


def add(left, right):
    if left is None:
        return right
    if right is None:
        return left
    x, y = left
    s, t = right
    if x == s and y == -t:
        return None
    if left == right:
        slope = (3 * x * x + 72 * x + 36) / (2 * y)
    else:
        slope = (t - y) / (s - x)
    new_x = slope * slope - 36 - x - s
    return new_x, slope * (x - new_x) - y


def prime_to_six(value):
    assert value > 0
    for prime in (2, 3):
        while value % prime == 0:
            value //= prime
    return value


def powers_and_totients(limit):
    phi = list(range(limit + 1))
    primes = []
    for p in range(2, limit + 1):
        if phi[p] == p:
            primes.append(p)
            for multiple in range(p, limit + 1, p):
                phi[multiple] -= phi[multiple] // p
    return primes, phi


def check_multiples():
    base = Fraction(-2), Fraction(8)
    points = [None]
    for _ in range(122):
        points.append(add(points[-1], base))
    for n in range(3, 62, 2):
        abscissa, ordinate = points[n]
        square = -abscissa / 2
        x, y = isqrt(square.numerator), isqrt(square.denominator)
        assert Fraction(x * x, y * y) == square
        z = ordinate * y**3 / (4 * x)
        assert z.denominator == 1
        assert x**4 - 18 * x**2 * y**2 + 9 * y**4 == -2 * z**2
        assert x % 2 and y % 2 and x % 3
        denominators = [points[m][0].denominator for m in (n - 1, n + 1)]
        assert all(isqrt(b)**2 == b for b in denominators)
        product = isqrt(denominators[0]) * isqrt(denominators[1])
        assert prime_to_six(abs(x*x - y*y)) == prime_to_six(product)
        doubled = points[2*n][0]
        assert doubled == Fraction(x**4 - 9*y**4, 2*x*y*z)**2
        assert prime_to_six(isqrt(doubled.denominator)) == prime_to_six(abs(x*y*z))
        if n == 3:
            assert (x, y, z) == (11, 3, 46)
            assert 1413128809**2 + 3 * 1236395160**2 == 37**12
        if n == 53:
            assert y % 211**2 == 0 and y % 211**3 != 0
            square = x*x + 3*y*y
            f0 = -2*z*z
            difference = 12*x**3*y - 36*x*y**3
            q = (x*y * (x*x-y*y) * (x*x-9*y*y) * (x*x-3*y*y)
                 * (x*x-6*x*y-3*y*y) * (x*x+6*x*y-3*y*y))
            residual = abs(z * (f0+difference) * (f0-difference) * q * square)
            height = (square // 4) ** 12
            assert 10**6501 < height < 10**6502
            for p, e in ((2, 25), (3, 3), (211, 2)):
                assert residual % p**e == 0 and residual % p**(e+1) != 0
            assert height * (2**24 * 9 * 211) // residual == 138132
    return 30


def check_prime_forcing(limit):
    primes, phi = powers_and_totients(2 * limit)
    k = lcm(*(phi[m] for m in range(1, 2 * limit + 1) if m % 3))
    tested = 0
    for p in primes:
        if not 7 <= p <= limit:
            continue
        residues = {a * a % p for a in range(1, p)}
        order = 1
        for x in range(p):
            rhs = x * (x*x + 36*x + 36) % p
            order += 1 if rhs == 0 else 2 * (rhs in residues)
        if order % 3 == 0:
            continue
        assert order % p and order <= 2 * limit
        assert pow(3, k, p * order) == 1
        tested += 1
    return tested


if __name__ == "__main__":
    print(f"Checked adjacent denominators at {check_multiples()} odd indices.")
    print(f"Checked the base-3 forcing congruence at {check_prime_forcing(2000)} primes.")

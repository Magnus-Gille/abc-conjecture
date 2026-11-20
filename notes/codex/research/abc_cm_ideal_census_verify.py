"""Verify exact primitive CM packets for E: y^2 = x^3-8x^2+8x, A=(1,1).

Run with an installed cypari or cypari2. Rational point arithmetic, ideal norms,
and removal of earlier prime support use only the Python standard library.
"""
import argparse
import csv
from fractions import Fraction
from functools import cache
from math import gcd, isqrt, lcm, prod
from pathlib import Path

try:
    from cypari import pari
except ImportError:
    from cypari2 import Pari
    pari = Pari()


def rational_multiples(bound):
    """Return the affine rational points [k]A for 1 <= k <= bound."""
    one = Fraction(1)
    points = [None, (one, one)]
    for k in range(2, bound + 1):
        x, y = points[-1]
        if k == 2:
            slope = (3 * x * x - 16 * x + 8) / (2 * y)
        else:
            slope = (y - one) / (x - one)
        new_x = slope * slope + 8 - x - one
        new_y = slope * (one - new_x) - one
        assert new_y * new_y == new_x**3 - 8 * new_x**2 + 8 * new_x
        points.append((new_x, new_y))
    return points


def complex_abscissa(a, b, points):
    """Return the two rational coefficients of x([(a+b*tau)]A)."""
    if not b:
        return points[a][0], Fraction(0)

    xb, yb = points[b]
    twist_x = -(xb - 8 + 8 / xb) / 2
    twist_y_coefficient = yb * (1 - 8 / xb**2) / 4
    assert -2 * twist_y_coefficient**2 == twist_x**3 - 8 * twist_x**2 + 8 * twist_x
    if not a:
        return twist_x, Fraction(0)

    xa, ya = points[a]
    slope_rational = -ya / (twist_x - xa)
    slope_radical = twist_y_coefficient / (twist_x - xa)
    return (
        slope_rational**2 - 2 * slope_radical**2 + 8 - xa - twist_x,
        2 * slope_rational * slope_radical,
    )


def odd_denominator_norm(x, y):
    """Odd part of the norm of the square-root denominator ideal of x+y*tau."""
    d = lcm(x.denominator, y.denominator)
    m, n = int(x * d), int(y * d)
    ideal_gcd_norm = gcd(d*d, d*m, d*n, m*m + 2*n*n)
    denominator_norm = d*d // ideal_gcd_norm
    while denominator_norm % 2 == 0:
        denominator_norm //= 2
    root = isqrt(denominator_norm)
    assert root**2 == denominator_norm
    return root


def packet_rows(limit):
    bound = isqrt(limit)
    points = rational_multiples(bound)
    ideals = sorted((a*a + 2*b*b, a, b)
                   for a in range(bound + 1) for b in range(isqrt(limit//2) + 1)
                   if 0 < a*a + 2*b*b <= limit and gcd(a, b) == 1)
    prior_support = 1
    for norm, a, b in ideals:
        denominator = odd_denominator_norm(*complex_abscissa(a, b, points))
        packet = denominator
        while (common := gcd(prior_support, packet)) != 1:
            packet //= common
        yield norm, a, b, denominator, packet
        prior_support *= packet


def check_exceptional_witness():
    p, r, tau = 205883, 34387, 49823
    assert int(pari(p).isprime()) and (tau*tau + 2) % p == 0
    assert 167**2 + 2*57**2 == r and r % p != 0
    curve = pari.ellinit([0, -8, 0, 8, 0], p)
    point = [1, 1]
    tau_point = [-pow(2, -1, p) % p, -7*tau*pow(4, -1, p) % p]
    assert int(pari.ellorder(curve, point)) == r
    relation = pari.elladd(curve, pari.ellmul(curve, point, 167),
                           pari.ellmul(curve, tau_point, -57))
    assert list(relation) == [0]

    modulus = p**3
    @cache
    def division_polynomial(k):
        if k < 5:
            return (0, 1, 2, -45, 868)[k] % modulus
        h = k // 2
        w = division_polynomial
        if k % 2:
            return (w(h+2)*w(h)**3 - w(h-1)*w(h+1)**3) % modulus
        return (w(h) * pow(2, -1, modulus) *
                (w(h+2)*w(h-1)**2 - w(h-2)*w(h+1)**2)) % modulus

    assert division_polynomial(r) == 34977*p**2
    print('Upper witness: (167-57*tau) of norm 34387, p=205883, exact depth 2.')


def verify(path, limit):
    with path.open(newline='') as stream:
        rows = list(csv.DictReader(stream))
    expected = list(packet_rows(limit))
    assert len(expected) == len(rows), 'Incomplete table across the requested disk'
    primes = {}
    prime_tests = set()
    exceptional = []
    open_rows = []
    for (norm, a, b, denominator, packet), row in zip(expected, rows):
        assert (norm, a, b) == tuple(int(row[k]) for k in ('norm', 'a', 'b'))
        assert denominator == int(row['odd_denominator_norm'])
        if row['first_prime_powers'] == '?':
            open_rows.append((norm, a, b))
            continue
        factors = []
        for item in row['first_prime_powers'].split():
            p, e = map(int, item.split('^'))
            assert e >= 1 and p not in prime_tests
            assert p % 8 in (1, 3), 'Every odd prime in a primitive packet splits'
            assert int(pari(p).isprime()) == 1, ('primality', p)
            prime_tests.add(p)
            primes[p] = (norm, e)
            factors.append((p, e))
            if e > 1:
                exceptional.append((norm, a, b, p, e))
        assert prod(p**e for p, e in factors) == packet, (norm, a, b)
    cutoff = open_rows[0][0] - 1 if open_rows else limit
    complete_count = sum(row[0] <= cutoff for row in expected)
    proven_primes = [p for p, (norm, _) in primes.items() if norm <= cutoff]
    assert cutoff >= 280
    assert all(primes[p][1] == 1 for p in proven_primes)
    print(f'Complete through norm {cutoff}: {complete_count} conjugacy classes, '
          f'{len(proven_primes)} distinct proved odd primes.')
    print(f'Full disk through {limit}: {len(rows)} conjugacy classes, '
          f'{len(rows)-len(open_rows)} factored, {len(primes)} distinct proved odd primes.')
    print(f'Open (norm, a, b): {open_rows}.')
    print(f'Largest prime in complete disk: {max(proven_primes)} '
          f'({len(str(max(proven_primes)))} digits).')
    print(f'Exceptional primitive first depths: {exceptional}.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate', nargs='?', type=Path,
                        default=Path(__file__).with_name('abc_cm_ideal_census.csv'))
    parser.add_argument('--limit', type=int, default=400)
    args = parser.parse_args()
    verify(args.certificate, args.limit)
    check_exceptional_witness()

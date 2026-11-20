"""Check the exact mixed-orbit denominator and local character certificates."""

from fractions import Fraction
from functools import cache
from math import gcd, isqrt, prod

from abc_octic_mixed_prime_indices import multiple, roots


def division_polynomials(field_prime=None):
    def reduce(value):
        if field_prime is None:
            return value
        return value.numerator * pow(value.denominator, -1, field_prime) % field_prime

    x = reduce(Fraction(-200, 81))
    y = reduce(Fraction(-1360, 729))
    b2, b4, b8 = 64, 64, -1024
    w2 = reduce(2 * y)
    w3 = reduce(3 * x**4 + b2 * x**3 + 3 * b4 * x**2 + b8)
    w4 = reduce(w2 * (2 * x**6 + b2 * x**5 + 5 * b4 * x**4
                      + 10 * b8 * x**2 + b2 * b8 * x + b4 * b8))
    inverse_w2 = 1 / w2 if field_prime is None else pow(w2, -1, field_prime)

    @cache
    def value(n):
        if n < 5:
            return (0, 1, w2, w3, w4)[n]
        k = n // 2
        if n % 2:
            return reduce(value(k + 2) * value(k)**3 - value(k - 1) * value(k + 1)**3)
        return reduce(value(k) * inverse_w2 * (value(k + 2) * value(k - 1)**2
                                                - value(k - 2) * value(k + 1)**2))

    return value


def run():
    psi = division_polynomials()
    first = [int(9**(n*n - 1) * psi(n)) for n in range(1, 5)]
    assert first == [1, -2720, -30363362304, -30978334255722004480]
    for n in range(1, 26, 2):
        s, t, y, v = roots(n)
        assert y*y == s*s + 2*t*t and v*v == (s-t)**2 + t*t
        term = (-1)**((n-1)//2) * psi(n) * 9**(n*n - 1) / 2**(5*(n*n-1)//4)
        assert y == 9*term and isqrt(y*y) == y
        if n % 3:
            assert (y//9 - (-1)**((n-1)//2)*n) % 3 == 0

    for p, r in ((353, 8), (127, 32)):
        assert all(p % j for j in range(2, isqrt(p) + 1))
        w = division_polynomials(p)
        assert all(w(n) for n in range(1, r)) and w(r) == 0
        for n in range(1, 4*r, 2):
            legendre = pow((-1)**((n-1)//2)*w(n), (p-1)//2, p)
            assert legendre in (1, p - 1)
            if p == 353:
                assert (legendre == p - 1) == (n % 8 in (3, 5))
            elif n % 8 == 7:
                assert (legendre == p - 1) == (n % 32 in (7, 15, 23))
        if p == 353:
            assert [w(n) for n in range(1, 10)] == [1, 158, 45, 340, 320, 154, 209, 0, 261]
            x = -200 * pow(81, -1, p)
            assert (x*w(4)**2 - w(5)*w(3)) % p == 0

    p = 89
    assert multiple(27, p) is None and multiple(9, p) is not None
    for m, expected in ((1, (24, 85, 1)), (5, (21, 53, 88)), (7, (57, 79, 88)),
                        (11, (57, 79, 88)), (13, (21, 53, 88)), (17, (24, 85, 1))):
        x, y = multiple((3*m + 1)//2, p)
        if x == 1:
            assert y == p - 1  # The seed and its involute have the same slope.
            slope = 7 * pow(4, -1, p) % p
        else:
            slope = (y+x) * pow(2*(x-1), -1, p) % p
        ratio = (slope + 40) * pow(slope - 40, -1, p) % p
        assert (slope, ratio, pow(ratio, 22, p)) == expected
    certificates = {
        5: [(5521, 30)],
        7: [(3023, 126), (13, 14)],
        11: [(4751, 44), (59, 11)],
        13: [(1871, 156), (701, 234)],
        17: [(577, 34), (43, 17), (233, 17)],
        19: [(9067, 57), (5393, 76)],
        23: [(4967, 828), (1103, 92), (1471, 184), (9199, 46)],
        41: [(929, 82), (4457, 369), (983, 164), (2131, 41)],
        43: [(1031, 172), (739, 43), (251, 43), (521, 86)],
        59: [(2089, 59), (6473, 1062), (1061, 118), (347, 59)],
    }
    for k, pairs in certificates.items():
        possible = set(range(1, k))
        for p, r in pairs:
            assert all(p % j for j in range(2, isqrt(p) + 1))
            assert (288*k) % (4*r) == 0
            w = division_polynomials(p)
            assert w(r) == 0
            assert all(w(j) for j in range(1, r) if r % j == 0)
            for m in range(287, 288*k, 288):
                if gcd(m, k) == 1:
                    sign = pow(-w(m % (4*r)), (p-1)//2, p)
                    if sign == p-1:
                        possible.discard(m % k)
        assert possible == {k-1}, (k, possible)
    assert 288*prod(certificates) == 1113861650821920
    assert 48*prod(k-1 for k in certificates) == 85346589081600
    for q, p, r in ((3, 13633, 24), (5, 31, 8), (7, 127, 32),
                    (11, 353, 8), (13, 189697, 8), (17, 2687, 56),
                    (19, 191, 16)):
        assert all(p % j for j in range(2, isqrt(p) + 1))
        assert (p-1) % q == 0 and r % 8 == 0
        w = division_polynomials(p)
        assert w(r) == 0 and all(w(j) for j in range(1, r) if r % j == 0)
        c = 9**4 * pow(32, -1, p) % p
        for n in range(5, q*r, 8):
            if gcd(n, q*r) != 1 and n not in (5, 13):
                continue
            value = pow(c, (n*n - 1)//4, p) * w(n) % p
            assert value and pow(value, (p-1)//q, p) != 1, (q, p, n)
        assert all(n in (5, 13) for n in range(5, q*r+1, 8)
                   if (q*r) % n == 0 and all(n % j for j in range(2, isqrt(n)+1)))
    print('Verified the denominator normalization and all local character tables.')


if __name__ == '__main__':
    run()

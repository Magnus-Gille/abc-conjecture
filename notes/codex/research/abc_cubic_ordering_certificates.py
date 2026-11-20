"""Check the cubic boundary, a simultaneous CRT witness, and three exact orders."""

from fractions import Fraction
from itertools import combinations
from math import isqrt, prod


def prime_factors(n):
    factors = set()
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.add(divisor)
            n //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if n > 1:
        factors.add(n)
    return factors


def det(a, b):
    return a[0] * b[1] - a[1] * b[0]


def cubic_roots():
    # Solve g(1/z) = 2/3 or -1/3 for each ordering by inverting the matrix.
    orders = ((1, 0, 0, 1), (-1, 1, 0, 1), (0, 1, 1, 0),
              (0, 1, -1, 1), (1, 0, 1, -1), (-1, 1, -1, 0))
    pairs = []
    for a, b, c, d in orders:
        pair = []
        for target in (Fraction(2, 3), Fraction(-1, 3)):
            z = (a - target*c) / (target*d - b)
            assert (a + b*z) / (c + d*z) == target
            pair.append(z)
        pairs.append(tuple(pair))
    expected = (('3/2', '-3'), ('3', '3/4'), ('2/3', '-1/3'),
                ('-2', '1/4'), ('-1/2', '4'), ('1/3', '4/3'))
    assert tuple(tuple(map(str, pair)) for pair in pairs) == expected
    roots = {r for pair in pairs for r in pair}
    assert len(roots) == 12
    points = [(r.numerator, r.denominator) for r in roots | {Fraction(0), Fraction(1)}]
    points.append((1, 0))  # infinity
    bad = set().union(*(prime_factors(abs(det(a, b))) for a, b in combinations(points, 2)))
    assert bad == {2, 3, 5, 7, 11, 13}
    print('Cubic roots:', ', '.join(map(str, sorted(roots))))
    print('Determinant primes:', *sorted(bad))
    return roots


def lattice_check(k, basis):
    # The order of 2 is 4*5^(k-1) since 2^4-1 has 5-adic valuation one.
    modulus = 5**k
    index = 4 * 5**(k-1)
    a, b = basis
    for u, v in basis:
        assert pow(2, u, modulus) * pow(3, v, modulus) % modulus == 1
    assert abs(det(a, b)) == index
    # A Gauss-reduced basis certifies that its first vector is shortest.
    norm_a = sum(x*x for x in a)
    assert norm_a <= sum(x*x for x in b)
    assert 2 * abs(a[0]*b[0] + a[1]*b[1]) <= norm_a
    return a


def valuation(n, p):
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def exponent_witness(roots):
    # The roots are in the z coordinate. Opposite signs share a block.
    magnitudes = sorted({abs(r) for r in roots})
    blocks = (17, 19, 23, 29, 31, 37, 41, 43, 47, 53)
    assert len(magnitudes) == len(set(blocks)) == 10
    assert all(q > 13 and prime_factors(q) == {q} for q in blocks)
    product = prod(blocks)
    exponents = []
    for r in magnitudes:
        a, b = (valuation(r.numerator, p) - valuation(r.denominator, p) for p in (2, 3))
        assert Fraction(2)**a * Fraction(3)**b == r
        exponents.append((a, b))

    k = 9
    index = 4 * 5**(k-1)
    a = lattice_check(k, ((-611, 973), (1025, 925)))
    b = lattice_check(k+1, ((-2247, 1021), (1439, 2823)))
    assert det(a, b) != 0
    # A CRT representative in index*Z^2 is automatically in L_k.
    weights = [(product//q) * pow(product//q, -1, q) for q in blocks]
    start = []
    for residues in zip(*exponents):
        residue = sum(x*w for x, w in zip(residues, weights)) % product
        start.append(index * (residue * pow(index, -1, product) % product))

    # Round in the basis P*a, P*b about the center of the positive box.
    scale = product * isqrt(index)
    assert scale**2 == product**2 * index
    delta = tuple(4*scale - x for x in start)
    denominator = product * det(a, b)
    i = round(Fraction(det(delta, b), denominator))
    j = round(Fraction(det(a, delta), denominator))
    u, v = (x + product*(i*y + j*z) for x, y, z in zip(start, a, b))
    assert all(2*scale <= x <= 6*scale for x in (u, v))
    assert pow(2, u, 5**k) * pow(3, v, 5**k) % 5**k == 1
    for q, (x, y) in zip(blocks, exponents):
        assert u > x and v > y and (u-x) % q == (v-y) % q == 0
    # Hence z/|r| is a q-th power with integer base >1. Zsigmondy applies
    # at order q for positive r and at order 2q for negative r.
    print(f'Switch {k} to {k+1}: {a}, {b}; P={product}; (u,v)=({u},{v})')
    print('Blocks (|r|,q):', ' '.join(f'({r},{q})' for r, q in zip(magnitudes, blocks)))


def order_example():
    for p, order in ((61, 10), (547, 14), (374857981681, 70)):
        assert prime_factors(p) == {p}
        assert pow(3, order, p) == 1
        assert all(pow(3, order//q, p) != 1 for q in prime_factors(order))
        assert pow(3, 176, p) == p-3
    print('Primes dividing 3^176+3: 61, 547, 374857981681; orders of 3: 10, 14, 70')


if __name__ == '__main__':
    exponent_witness(cubic_roots())
    order_example()

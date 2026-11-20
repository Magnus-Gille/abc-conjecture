"""A ninth-cyclotomic packet at every prime q=1 mod 9 in (100,200]."""

from fractions import Fraction
from functools import cache
from itertools import product
from math import gcd, isqrt, log, prod


def det(u, v):
    return u[0]*v[1] - u[1]*v[0]


def dot(u, v):
    return u[0]*v[0] + u[1]*v[1]


def combination(i, u, j, v):
    return (i*u[0] + j*v[0], i*u[1] + j*v[1])


@cache
def root(q, e):
    if e == 1:
        return next(x for x in range(2, q) if pow(x, 9, q) == 1 and pow(x, 3, q) != 1)
    x, m = root(q, e-1), q**(e-1)
    error = (pow(x, 9, m*q) - 1) // m
    return x + m * (-error * pow(9*x**8, -1, q) % q)


def gauss(residue, modulus):
    u, v = (1, residue), (0, modulus)
    while True:
        if dot(v, v) < dot(u, u):
            u, v = v, u
        if 2*abs(dot(u, v)) <= dot(u, u):
            break
        v = combination(1, v, -round(Fraction(dot(u, v), dot(u, u))), u)
    assert abs(det(u, v)) == modulus
    assert all((b-residue*a) % modulus == 0 for a, b in (u, v))
    return u, v  # Gauss reduction makes u Euclidean-shortest.


def shortest_max_norm(u, v):
    # A max-norm minimizer has Euclidean length <= sqrt(2)*|u|. Projection
    # perpendicular to u gives |j|<2; projection along u then gives |i|<2.
    options = (u, v, combination(1, u, 1, v), combination(1, u, -1, v))
    return min(options, key=lambda w: max(map(abs, w)))


def transition(primes, level):
    depths = dict.fromkeys(primes, level)
    residue, modulus = 0, 1
    for q in primes:
        m = q**level
        residue += modulus * ((root(q, level) - residue) * pow(modulus, -1, m) % m)
        modulus *= m
    basis = gauss(residue, modulus)
    for step in range(4*level*len(primes) + 1):
        q = primes[step % len(primes)]
        e, m = depths[q], q**depths[q]
        gap = root(q, e+1) - residue
        assert gap % m == 0
        new_residue = residue + modulus * ((gap//m) * pow(modulus//m, -1, q) % q)
        new_basis = gauss(new_residue, modulus*q)
        mixed_depths = len(set(depths.values())) > 1
        euclidean_change = det(basis[0], new_basis[0]) != 0
        max_norm_change = det(shortest_max_norm(*basis), shortest_max_norm(*new_basis)) != 0
        if mixed_depths and euclidean_change and max_norm_change:
            assert all(dot(u, u) < dot(v, v) for u, v in (basis, new_basis))
            return modulus, depths, basis, new_basis[0], q
        residue, modulus, basis = new_residue, modulus*q, new_basis
        depths[q] += 1
    raise AssertionError('no transition in this sample')


def select_pair(basis, depths):
    u, v = basis
    lines = []
    for q, e in depths.items():
        x, m = root(q, e+1), q**e
        gaps = tuple(b-x*a for a, b in basis)
        assert all(gap % m == 0 for gap in gaps)
        first = (u[0], v[0])
        second = tuple(gap//m for gap in gaps)
        assert det(first, second) % q != 0
        lines.append((q, first, second))

    size = max(map(abs, u + v))
    center = (1200*size, 600*size)
    i0 = round(Fraction(det(center, v), det(u, v)))
    j0 = round(Fraction(det(u, center), det(u, v)))
    choices = []
    for di, dj in product(range(-50, 50), repeat=2):
        coeff = (i0+di, j0+dj)
        a, b = combination(coeff[0], u, coeff[1], v)
        assert 0 < a < 3*b < 2*a  # every point lies in the requested sector
        if any(dot(coeff, line) % q == 0 for q, first, second in lines for line in (first, second)):
            continue
        g = gcd(a, b)
        assert all(g % q for q in depths)
        choices.append((a//g, b//g, g, coeff))
    return min(choices), len(choices)  # choose the smallest reduced A in the box


def main():
    primes = [q for q in range(101, 201) if q % 9 == 1 and all(q % d for d in range(2, isqrt(q)+1))]
    level = 7
    modulus, depths, basis, next_shortest, increment = transition(primes, level)
    (a, b, g, coeff), good = select_pair(basis, depths)
    assert gcd(a, b) == 1 and 0 < a < 3*b < 2*a
    phi = a**6 + a**3*b**3 + b**6
    actual = {}
    for q in primes:
        value, e = phi, 0
        while value % q == 0:
            value //= q
            e += 1
        actual[q] = e
        assert (b - root(q, depths[q])*a) % q**depths[q] == 0
        ratio = b * pow(a, -1, q) % q
        assert pow(ratio, 9, q) == 1 and pow(ratio, 3, q) != 1
    packet = prod(primes)
    assert actual == depths and modulus == prod(q**e for q, e in actual.items())
    assert phi % modulus == 0 and gcd(phi//modulus, packet) == 1
    gain = modulus // packet
    print(f'L={level}, P={packet}, D={modulus}, next determinant={modulus*increment} (q={increment})')
    print(f'Reduced basis at D: {basis}\nShortest after the increment: {next_shortest}')
    print(f'{good}/10000 coefficient pairs survive; selected {coeff}, gcd before reduction {g}')
    print(f'A={a}\nB={b}\ndirect depths={actual}\nD/P={gain}')
    print(f'bit lengths of A, D, D/P: {a.bit_length()}, {modulus.bit_length()}, {gain.bit_length()}; '
          f'log(D/P)/log(A)={log(gain)/log(a):.9f}')


if __name__ == '__main__':
    main()

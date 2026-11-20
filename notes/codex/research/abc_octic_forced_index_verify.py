"""Check cubefull-index certificates for the (1,2) orbit using only Python 3."""

from collections import Counter
from math import isqrt
from pathlib import Path
import sys

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)


def is_prime(n):
    return n >= 2 and all(n % j for j in range(2, isqrt(n) + 1))


def curve_add(p1, p2, modulus):
    """Affine addition on Y²=X³−4225X, when the slope denominator is a unit."""
    if p1 is None:
        return p2
    x, y = p1
    u, v = p2
    if p1 == p2:
        slope = (3*x*x - 4225) * pow(2*y, -1, modulus) % modulus
    else:
        slope = (v-y) * pow(u-x, -1, modulus) % modulus
    z = (slope*slope-x-u) % modulus
    return z, (slope*(x-z)-y) % modulus


def multiple(k, modulus, seed):
    s,t,z = seed
    q = (-4*s*s*t*t*pow(z*z, -1, modulus) % modulus,
         2*s*t*(s**4-4*t**4)*pow(z**3, -1, modulus) % modulus)
    point = None
    for bit in bin(k)[2:]:
        if point is not None:
            point = curve_add(point, point, modulus)
        if bit == '1':
            point = curve_add(point, q, modulus)
    return point


def orbit_slope(r, modulus, seed=(1,2,1)):
    """x(P_r) in Z/modulus, via P_r=P+[(r−1)/2]T over the quadratic algebra."""
    def sub(a, b):
        return (a[0]-b[0]) % modulus, (a[1]-b[1]) % modulus

    def mul(a, b):
        return ((a[0]*b[0]+65*a[1]*b[1]) % modulus,
                (a[0]*b[1]+a[1]*b[0]) % modulus)

    def div(a, b):
        reciprocal_norm = pow(b[0]*b[0]-65*b[1]*b[1], -1, modulus)
        return mul(a, (reciprocal_norm*b[0], -reciprocal_norm*b[1]))

    s,t,z = seed
    assert s**4 + 4*t**4 == 65*z*z
    u, v = multiple((r-1)//2, modulus, seed)
    scale = pow(2*t*t, -1, modulus)
    x0 = (s*s*scale % modulus, z*scale % modulus)
    y0 = mul(x0, (s*pow(t, -1, modulus) % modulus, 0))
    x1 = (u * pow(65, -1, modulus) % modulus, 0)
    y1 = (0, v * pow(65**2, -1, modulus) % modulus)
    chord = div(sub(y1, y0), sub(x1, x0))
    x = sub(sub(mul(chord, chord), x0), x1)
    y = sub(mul(chord, sub(x0, x)), y0)
    root, sqrt65_coeff = div(y, x)
    assert sqrt65_coeff == 0
    return root


def main():
    filespec = Path(__file__).with_name('abc_octic_forced_index_certificates.txt')
    products = {'+': 65, '-': 65}
    counts = {'+': Counter(), '-': Counter()}
    single = {'+': 13, '-': 5}
    for line in filespec.read_text().splitlines():
        if not line or line.startswith('#'):
            continue
        sign, stage, prime, witness = line.split()
        stage, p, r = int(stage), int(prime), int(witness)
        assert p > 13 and p % 4 == 1 and is_prime(p)
        assert r > 1 and r % 2 == 1 and products[sign] % r == 0
        assert products[sign] % p != 0
        slope = orbit_slope(r, p**3)
        value = (slope + (1 if sign == '+' else -1))**2 + 1
        assert value % (p*p) == 0 and value % (p**3) != 0
        products[sign] *= p
        if single[sign] % r == 0:
            single[sign] *= p
        counts[sign][stage] += 1
    for sign, product in products.items():
        print(f'U{sign} stages {sorted(counts[sign].items())}, '
              f'{sum(counts[sign].values())} extra primes, '
              f'{len(str(product))} digits in the forced divisor. '
              f'From its seed prime alone: {len(str(single[sign]))} digits.')


if __name__ == '__main__':
    main()

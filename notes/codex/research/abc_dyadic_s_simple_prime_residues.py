"""Verify the finite certificate of simple primes of s_(2^k) from its CSV."""

import csv
from collections import defaultdict
from fractions import Fraction
from math import gcd, lcm, prod
from pathlib import Path


def prime_factors(n):
    factors = set()
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            factors.add(divisor)
            while n % divisor == 0:
                n //= divisor
        divisor += 1 if divisor == 2 else 2
    if n > 1:
        factors.add(n)
    return factors


def affine_multiple(scalar, modulus):
    """Multiply R on E' while denominators are units (scalars below its order)."""
    x, y = -8 % modulus, 16 % modulus
    u, v = x, y
    assert scalar >= 1
    for bit in bin(scalar)[3:]:
        slope = (3*u*u + 32*u + 32) * pow(2*v, -1, modulus) % modulus
        a = (slope*slope - 16 - 2*u) % modulus
        u, v = a, (slope*(u-a)-v) % modulus
        if bit == "1":
            slope = (v-y) * pow(u-x, -1, modulus) % modulus
            a = (slope*slope - 16 - u - x) % modulus
            u, v = a, (slope*(u-a)-v) % modulus
    return u, v


def check_period(modulus, exponent, factors):
    """Check the exact order of 2 in (Z/modulus)^* modulo the signs {1,-1}."""
    assert pow(2, exponent, modulus) in (1, modulus-1)
    assert all(pow(2, exponent//ell, modulus) not in (1, modulus-1)
               for ell in factors if exponent % ell == 0)


def check_row(p, r, h, H):
    assert p > 5 and prime_factors(p) == {p}
    assert r >= 3 and r % 2 and gcd(p,r) == 1
    assert prime_factors(h) == {h} and H > h and H % h == 0
    # All calculations here must return affine points using only unit divisions.
    for ell in prime_factors(r):
        affine_multiple(r//ell, p)
    x, y = affine_multiple(r-1, p*p)
    assert (x % p, y % p) == (-8 % p, -16 % p)
    assert (x, y) != (-8 % (p*p), -16 % (p*p))
    check_period(r, h, {h})
    assert (2*h*(p-1)) % H == 0
    check_period(r*p, H, prime_factors(p-1) | {2,h})


def read_rows():
    with Path(__file__).with_suffix(".csv").open() as source:
        rows = [tuple(map(int, row)) for row in list(csv.reader(source))[1:]]
    assert len(rows) == len({p for p, r, h, H in rows}) == 1344
    return rows


def check_density(rows):
    groups = defaultdict(list)
    for p, r, h, H in rows:
        groups[h].append(H)
    assert len(groups) == 476
    missed = {h: lcm(*values) for h, values in groups.items()}
    assert 5 in groups and missed[2] % 5 == 0
    missed[2] = lcm(missed[2], missed[5])
    base = prod(1-Fraction(1,h) for h in groups)
    lower = 1-base-sum(Fraction(1,m) for m in missed.values())
    assert lower > Fraction(90150214,10**8)
    # A certified lower approximation to log_2(p), using integers only.
    mean_bits = sum(Fraction((p**256).bit_length()-1,256)*(Fraction(1,h)-Fraction(1,H))
                    for p, r, h, H in rows)
    assert mean_bits > Fraction(15345,100)
    # On m divisible by 11, outside the union of second periods in this group.
    group = [row for row in rows if row[2] == 11]
    assert len(group) == 14
    assert Fraction(1,11) - sum(Fraction(1,H) for p, r, h, H in group) > Fraction(9,100)
    assert prod(p for p, r, h, H in group) > 2**234
    # For m equal to the following product modulo the lcm of every second period.
    seed = prod(groups)
    primes = [p for p, r, h, H in rows if seed % H]
    assert len(primes) == 1113 and prod(primes) > 2**22079
    print("Number of certified primes and distinct first periods:", len(rows), len(groups))
    print("Density lower bound (rounded down):", lower.numerator*10**8//lower.denominator, "/ 10^8")
    print("Mean lower bound in bits (rounded down):", mean_bits.numerator*100//mean_bits.denominator, "/ 100")
    print("Simultaneous simple primes on the specified progression:", len(primes))


if __name__ == "__main__":
    records = read_rows()
    for record in records:
        check_row(*record)
    check_density(records)

"""Verify the full and partial factorizations of 2X_n+Z_n and local lift claims."""

import json
import math
from fractions import Fraction
from pathlib import Path

try:
    from cypari import pari
except ImportError:
    from cypari2 import Pari
    pari = Pari()
from flint import fmpz

from abc_octic_mixed_prime_indices import multiple
from abc_octic_mixed_wieferich import division_value


def marked_integer(n):
    x = Fraction(multiple(n)[0])
    return 2 * x.numerator + x.denominator


def factors(n):
    primes, powers = pari.factor(n)
    return [(int(p), int(e)) for p, e in zip(primes, powers)]


def verify_census():
    rows = json.loads(Path(__file__).with_suffix('.json').read_text())
    assert [r[0] for r in rows] == list(range(1, 51))
    certified = {}
    unresolved_product = 1
    complete = []
    for n, factors_of_term, residuals in rows:
        F = marked_integer(n)
        assert math.prod(p**e for p, e in factors_of_term) * math.prod(residuals) == F
        assert len({p for p,e in factors_of_term}) == len(factors_of_term)
        for p,e in factors_of_term:
            if p not in certified:
                assert pari.isprime(p)
                certified[p] = True
            assert e > 0 and F % (p**(e+1)) != 0
        assert all(c > 1 and not pari.isprime(c) for c in residuals)
        unresolved_product *= math.prod(residuals)
        if not residuals:
            complete.append(n)
    assert complete == list(range(1,21)) + [22,23,25,26,28]
    assert fmpz.primorial_ui(100_000_000).gcd(fmpz(unresolved_product)) == 1
    records = [(n,p,e) for n,factors_of_term,_ in rows for p,e in factors_of_term]
    repeated = [(n,p,e) for n,p,e in records if e > 1]
    assert repeated == [(25,19,2), (27,43,2), (41,11,2), (44,17,2)]
    assert len(records) == 670 and len(certified) == 456
    print('Complete rows',complete)
    print('Certified prime incidences',len(records),'distinct primes',len(certified))
    print('Greatest certified prime by number of digits',len(str(max(certified))))
    print('Repeated certified primes (n,p,e)',repeated)


def verify_lifts():
    increments = []
    for n in range(1,101):
        for p,k in factors(n*n+2):
            if p <= 7:
                continue
            point = multiple(n,p)
            if point is None:
                continue
            x,y = point
            if (2*x+1) % p or (7*n+4*y) % p:
                continue
            r = n*n+2
            for ell,e in factors(r):
                while r % ell == 0 and division_value(r//ell,p) == 0:
                    r //= ell
            assert r % p and division_value(r,p*p) % p == 0
            assert division_value(r,p*p) != 0
            F = marked_integer(n)
            assert F % p**(1+k) == 0 and F % p**(2+k) != 0
            increments.append((n,p,r,k))
    assert increments == [(25,19,11,1),(27,43,17,1),(41,11,9,1),
                          (44,17,6,1),(58,11,9,1),(58,17,6,1),(80,97,22,1)]
    print('All lift increments (n,p,rank,increment), n <= 100',increments)


if __name__ == '__main__':
    verify_census()
    verify_lifts()

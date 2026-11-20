"""Verify first-rank denominators and all prime certificates using only the standard library."""

from functools import cache
from fractions import Fraction
from math import gcd, isqrt, prod
from pathlib import Path
import json

DATA = json.loads(Path(__file__).with_name('abc_octic_scalar_rank_certificates.json').read_text())


def ec_add(left, right, modulus, a):
    """Addition on a short Weierstrass curve, with only certified unit denominators."""
    if left is None: return right
    if right is None: return left
    x, y = left
    u, v = right
    if x == u:
        if (y+v) % modulus == 0: return None
        assert y == v
        num, den = 3*x*x+a, 2*y
    else:
        num, den = v-y, u-x
    slope = num*pow(den, -1, modulus) % modulus
    z = (slope*slope-u-x) % modulus
    return z, (slope*(x-z)-y) % modulus


def ec_mul(index, point, modulus, a):
    result = None
    while index:
        if index % 2: result = ec_add(result, point, modulus, a)
        index //= 2
        if index: point = ec_add(point, point, modulus, a)
    return result


@cache
def is_proven_prime(p):
    if p <= 10**8:
        return p >= 2 and all(p % d for d in range(2, isqrt(p)+1))
    tag, *certificate = DATA['certificates'][str(p)]
    if tag == 'lucas':
        a, factors = certificate
        assert prod(q**e for q,e in factors) == p-1 and pow(a,p-1,p) == 1
        assert all(0 < q < p and e > 0 and is_proven_prime(q) and
                   gcd(pow(a,(p-1)//q,p)-1,p) == 1 for q,e in factors)
    else:
        assert tag == 'ecpp'
        chain, = certificate
        n = p
        for v, t, s, a, point in chain:
            assert n == v and n > 3 and gcd(n,6) == 1
            q, remainder = divmod(n+1-t,s)
            assert remainder == 0 and s > 0 and (isqrt(isqrt(n))+2)**2 < q < n
            x, y = point
            b = (y*y-x*x*x-a*x) % n
            assert gcd(4*a**3+27*b*b,n) == 1
            Q = ec_mul(s, (x % n, y % n), n, a)
            assert Q is not None and ec_mul(q, Q, n, a) is None
            n = q
        assert n < p and is_proven_prime(n)
    return True


def denominators(limit):
    """Exact abscissas of A,2A,... by addition of A=(1,1)."""
    ds = {}
    x = y = Fraction(1)
    for r in range(1,limit+1):
        ds[r] = isqrt(x.denominator)
        assert ds[r]**2 == x.denominator
        slope = (3*x*x-16*x+8)/(2*y) if r == 1 else (y-1)/(x-1)
        new_x = slope*slope+7-x
        y, x = slope*(x-new_x)-y, new_x
    return ds


def run():
    rows = {int(k):v for k,v in DATA['factors_at_first_rank'].items()}
    ds = denominators(max(37,max(rows)))
    witnesses = []
    for r, factors in sorted(rows.items()):
        part = ds[r]
        part //= part & -part
        for d in range(1,r):
            if r % d: continue
            while (g := gcd(part,ds[d])) > 1:
                part //= g
        assert len(set(p for p,e in factors)) == len(factors)
        assert all(e>0 and p%2 and is_proven_prime(p) for p,e in factors)
        assert prod(p**e for p,e in factors) == part
        witnesses += [(r,p,e) for p,e in factors if e>1]
    assert witnesses == [(3,3,2)]
    partial = DATA['partial_rank_37']
    known = partial['simple_factors']
    rest = partial['composite_cofactors']
    assert all(is_proven_prime(p) for p in known)
    assert len(set(known)) == len(known)
    assert all(pow(2,c-1,c) != 1 for c in rest)
    assert gcd(prod(known),prod(rest)) == gcd(*rest) == 1
    assert prod(known)*prod(rest) == ds[37]
    print('Certified ranks',sorted(rows))
    print('Distinct odd first-rank primes',sum(len(row) for row in rows.values()))
    print('All initial multiplicities exceeding one',witnesses)


if __name__ == '__main__':
    run()

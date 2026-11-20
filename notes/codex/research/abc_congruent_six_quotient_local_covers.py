"""Check simultaneous quadratic-character obstructions for every odd multiplier m."""

from csv import DictReader
from functools import cache
from math import isqrt, lcm
from pathlib import Path


@cache
def prime(p):
    return p >= 2 and all(p % i for i in range(2, isqrt(p)+1))


def add(P, Q, p):
    if P is None:
        return Q
    if Q is None:
        return P
    x,y = P
    u,v = Q
    if x == u:
        if (y+v) % p == 0:
            return None
        s = (3*x*x-36)*pow(2*y,-1,p)
    else:
        s = (v-y)*pow(u-x,-1,p)
    xx = (s*s-x-u) % p
    return xx,(s*(x-xx)-y) % p


@cache
def orbit(p):
    assert prime(p) and p > 3
    G = (-3 % p,9 % p)
    points = [None]
    point = G
    while point is not None:
        points.append(point)
        point = add(point,G,p)
    return points


def psi_odd(point,q,p):
    x,y = point
    a = -36
    initial = (0, 1, 1, (3*x**4+6*a*x*x-a*a) % p,
               (2*(x**6+5*a*x**4-5*a*a*x*x-a**3)) % p)
    factor = pow(2*y,4,p)

    @cache
    def term(n):
        if n < 5:
            return initial[n]
        k = n//2
        if n % 2:
            u = term(k+2)*term(k)**3
            v = term(k-1)*term(k+1)**3
            return (u-factor*v if k%2 else factor*u-v) % p
        return term(k)*(term(k+2)*term(k-1)**2-term(k-2)*term(k+1)**2) % p

    assert q % 2
    return term(q)


@cache
def excluded(q,p,h):
    point = orbit(p)[h]
    if point is None and p == q:
        return True
    a = q if point is None else psi_odd(point,q,p)
    if q % 4 == 3:
        a = -a
    return pow(a,(p-1)//2,p) == p-1


def verify_case(q,aux):
    modulus = 2
    allowed = [1]
    for p in aux:
        d = len(orbit(p))
        widened = lcm(modulus,d)
        survivors = []
        for block in range(0,widened,modulus):
            for n in allowed:
                h = block+n
                residue = min(h%d,(-h)%d)
                if not excluded(q,p,residue):
                    survivors.append(h)
        allowed = survivors
        modulus = widened
        if not allowed:
            return
    raise AssertionError((q,modulus,allowed[:20]))


def main():
    # Each finite point of order d has Legendre-symbol period dividing 4d in q.
    assert len(orbit(31)) == 16
    assert all(excluded(q,31,m) for q in range(1,64,2) if q%16 in (7,9)
               for m in range(1,16,2))
    assert len(orbit(13)) == 5
    assert all(pow(psi_odd(orbit(13)[m],q,13),6,13) == {0:0,1:1,4:12}[pow(q,2,5)]
               for q in range(1,21,2) for m in range(1,5))

    path = Path(__file__).with_name('abc_congruent_six_quotient_local_covers.csv')
    with path.open() as f:
        rows = list(DictReader(f))
    qs = [q for q in range(3,10000,2) if prime(q)]
    assert [int(row['q']) for row in rows] == [q for q in qs if q%8 in (1,7)]
    for row in rows:
        verify_case(int(row['q']),map(int,row['auxiliary_primes'].split()))
    print(f'{len(qs)} odd primes below 10000 verified, {len(rows)} by local covers.')


if __name__ == '__main__':
    main()

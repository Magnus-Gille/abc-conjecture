"""Prove the largest odd-exponent prime census through the inclusive bound 140449."""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import isqrt, prod

BOUND = 140449


def prime_list(limit):
    flags = bytearray([1]) * (limit + 1)
    flags[:2] = bytes(2)
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            flags[p*p::p] = bytes((limit - p*p)//p + 1)
    return [p for p, flag in enumerate(flags) if flag]


def factors(value):
    result = []
    p = 2
    while p * p <= value:
        if value % p == 0:
            result.append(p)
            while value % p == 0:
                value //= p
        p += 1 if p == 2 else 2
    if value > 1:
        result.append(value)
    return result


def add(P, Q, a2, a4, modulus):
    if P is None:
        return Q
    if Q is None:
        return P
    x, y = P
    u, v = Q
    if x == u:
        if ((y + v) % modulus if modulus else y + v) == 0:
            return None
        num, den = 3*x*x + 2*a2*x + a4, 2*y
    else:
        num, den = v-y, u-x
    slope = (num * pow(den, -1, modulus)) % modulus if modulus else Fraction(num, den)
    rx = slope*slope - a2 - x - u
    ry = slope*(x-rx)-y
    return (rx % modulus, ry % modulus) if modulus else (rx, ry)


def multiple(n, point, a2, a4, modulus=None):
    Q = tuple(c % modulus for c in point) if modulus else point
    R = None
    while n:
        if n & 1:
            R = add(R, Q, a2, a4, modulus)
        n //= 2
        if n:
            Q = add(Q, Q, a2, a4, modulus)
    return R


def exact_order(p, odd_part):
    def identity(k):
        return multiple(k, (-3,9), 0, -36, p) is None
    # The Gaussian representation only suggests annihilators. Checks below
    # prove the exact order independently of the CM order formula.
    possible = [p+1-2*odd_part, p+1+2*odd_part]
    order = next(m for m in possible if identity(m))
    for ell in factors(order):
        while order % ell == 0 and identity(order//ell):
            order //= ell
    assert identity(order) and all(not identity(order//ell) for ell in factors(order))
    return order


def symbol(n, p):
    z = pow(n % p, (p-1)//2, p)
    return -1 if z == p-1 else z


def permissible_kernels(q, bases, auxiliary):
    kernels = [prod(subset) for j in range(len(bases)+1) for subset in combinations(bases,j)]
    last = None
    for ell in auxiliary:
        if ell in bases:
            continue
        point = multiple(q, (-2,8), 36, 36, ell)
        chi = 1 if point is None else symbol(8*(6-point[0]), ell)
        if not chi:
            continue
        kernels = [k for k in kernels if symbol(k,ell) == chi]
        if not kernels:
            last = ell
            break
    return kernels, last


def denominator(n):
    x, _ = multiple(n, (-3,9), 0, -36)
    v = isqrt(x.denominator)
    assert v*v == x.denominator
    return v


def main():
    primes = prime_list(BOUND)
    prime_set = set(primes)
    gaussian_odd = {}
    for b in range(2,isqrt(BOUND)+1,2):
        for a in range(1,isqrt(BOUND-b*b)+1,2):
            p = a*a+b*b
            if p in prime_set:
                gaussian_odd[p] = a
    by_rank = defaultdict(list)
    good_primes = [p for p in primes if p % 12 == 1]
    for p in good_primes:
        r = exact_order(p, gaussian_odd[p])
        if r % 2:
            by_rank[r].append(p)

    candidates = sorted(q for q in by_rank if q in prime_set)
    auxiliary = [ell for ell in primes if 5 <= ell <= 89]
    survivors = {}
    witness_primes = []
    for q in candidates:
        left, last = permissible_kernels(q, by_rank[q], auxiliary)
        if left:
            survivors[q] = left
        else:
            witness_primes.append(last)
    assert len(candidates) == 404 and sum(len(by_rank[q]) for q in candidates) == 449
    assert survivors == {3:[37], 5:[40573], 7:[2005752169]}
    print('prime bases checked, odd-order bases, prime-order bases, candidate prime indices:',
          len(good_primes), sum(map(len,by_rank.values())), sum(len(by_rank[q]) for q in candidates), len(candidates))
    print('largest candidate index, largest number of bases at one prime index, largest auxiliary witness:',
          max(candidates),max(len(by_rank[q]) for q in candidates),max(witness_primes))
    print('prime-index survivors and kernels:',survivors)

    for d in (9,15,21,25,35,49):
        cofactor = denominator(d)
        small = []
        for rank, bases in by_rank.items():
            if d % rank:
                continue
            for p in bases:
                e = 0
                while cofactor % p == 0:
                    e += 1
                    cofactor //= p
                assert e > 0
                small.append((p,e))
        assert isqrt(cofactor)**2 != cofactor
        witness = next(ell for ell in primes if ell > 2 and symbol(cofactor,ell) == -1)
        print('divisor index, removed primes/exponents, residual bits, nonresidue witness:',
              d,sorted(small),cofactor.bit_length(),witness)

    for n, primes_n in [(1,()),(3,(37,)),(5,(13,3121)),(7,(14281,140449))]:
        assert all(p in prime_set for p in primes_n)
        assert denominator(n) == prod(primes_n)
    print('All positive odd indices with smooth squarefree kernel:', [1,3,5,7])


if __name__ == '__main__':
    main()

"""Exact census of positive odd indices whose squarefree part is 31,904,497-smooth.

Build abc_full_quartic_prime_rank_scan.cpp with C++17. Pass the resulting
executable as the only argument. The rank scan is rerun on every verification.
"""
from collections import defaultdict
from math import isqrt, prod
import subprocess
import sys

from abc_congruent_six_smooth_odd_support import add, denominator, multiple, prime_list, symbol


BOUND = 31_904_497


def source_characters(prime):
    """Signs of B_j at odd residues j, indexed by j mod the order of P."""
    point = None
    generator = (-2 % prime, 8 % prime)
    signs = []
    while True:
        signs.append(1 if point is None else symbol(8 * (6 - point[0]), prime))
        point = add(point, generator, 36, 36, prime)
        if point is None:
            return signs


def first_contradiction(index, cofactor, tests):
    for ell, signs in tests:
        sign = signs[index % len(signs)]
        if sign and cofactor % ell and symbol(cofactor, ell) != sign:
            return ell
    return None


def first_depths(candidates):
    hits = []
    for q, primes in candidates.items():
        for p in primes:
            modulus = p*p
            generator = (-3 % modulus, 9)
            half = multiple((q-1)//2, generator, 0, -36, modulus)
            following = add(half, generator, 0, -36, modulus)
            assert half[1] % p and (half[0] - following[0]) % p == 0
            assert (half[1] + following[1]) % p == 0
            if half[0] == following[0]:
                hits.append((q, p))
    return hits


def main():
    if len(sys.argv) != 2:
        sys.exit('Pass the path to the compiled prime-order scanner.')
    raw = subprocess.check_output([sys.argv[1], str(BOUND)], text=True)
    candidates = defaultdict(list)
    for line in raw.splitlines():
        q, p = map(int, line.split())
        candidates[q].append(p)
    assert first_depths(candidates) == []
    print('Every enumerated prime-order reduction has first denominator valuation one.')
    small_primes = prime_list(71)
    tests = [(p, source_characters(p)) for p in small_primes if p > 3]
    survivors = []
    witnesses = []
    for q, bases in sorted(candidates.items()):
        ell = first_contradiction(q, prod(bases), tests)
        if ell is None:
            survivors.append(q)
        else:
            witnesses.append(ell)
    print('Candidate prime indices:', len(candidates), 'with at most', max(map(len, candidates.values())), 'bases per index.')
    print('Surviving prime indices:', survivors, 'largest auxiliary prime needed:', max(witnesses))
    assert survivors == [3, 5, 7]

    allowed = {1: (), 3: (37,), 5: (13, 3121), 7: (14281, 140449), 9: (37, 2148661, 31904497)}
    sieve = bytearray(b'\x01') * (BOUND + 1)
    sieve[:2] = bytes(2)
    for p in range(2, isqrt(BOUND) + 1):
        if sieve[p]:
            sieve[p*p::p] = bytes((BOUND-p*p)//p + 1)
    for n, bases in allowed.items():
        assert all(sieve[p] for p in bases) and denominator(n) == prod(bases)

    excluded_divisors = (15, 21, 25, 27, 35, 49)
    residuals = {n: denominator(n) for n in excluded_divisors}
    for p in range(13, BOUND + 1, 12):
        if not sieve[p]:
            continue
        for n, value in residuals.items():
            while value % p == 0:
                value //= p
            residuals[n] = value
    for n, residual in residuals.items():
        assert residual != isqrt(residual)**2
        print('Excluded divisor:', n, 'remaining bits:', residual.bit_length())
    print('All eligible positive odd indices:', sorted(allowed))


if __name__ == '__main__':
    main()

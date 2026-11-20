"""Exact abc qualities of B^n + (A^n-B^n) = A^n for n=7,9 and A <= 500."""

import argparse
from functools import cache, lru_cache
from itertools import count
from math import gcd, isqrt, lcm, log, prod

from abc_average_order_check import prime_divisors
from abc_cyclotomic_large_square_scan import BOUNDS, cyclotomic
from abc_mersenne_quadratic_prime_scan import primes_through


@cache
def trial_radical(value):
    return prod(prime_divisors(value))


def sextic_radical(value, prime_product):
    """prime_product contains all eligible primes <= K*A^2, once each."""
    small_rad = gcd(value, prime_product)
    rest = value // small_rad
    while (common := gcd(rest, small_rad)) > 1:
        rest //= common
    # Phi_n < K*A^6. If any surviving p occurs twice, the complementary
    # factor is < K*A^2 and was fully removed. Thus rest is squarefree or p².
    root = isqrt(rest)
    return small_rad * (root if root*root == rest else rest)


def pari_checker():
    try:
        from cypari2 import Pari
        pari = Pari()
    except ModuleNotFoundError:
        from cypari import pari

    @lru_cache(maxsize=8192)
    def radical(value):
        factors = pari(value).factor()
        pairs = [(int(p), int(e)) for p, e in zip(factors[0], factors[1])]
        assert prod(p**e for p, e in pairs) == value
        assert all(e > 0 and pari(p).isprime() for p, e in pairs)
        return prod(p for p, e in pairs)

    return radical


def census(n, height, primes, pari_radical):
    k = BOUNDS[n]
    eligible = [p for p in primes if p <= k*height**2 and (n % p == 0 or (p-1) % n == 0)]
    # At p not dividing n, separability of T^n-1 gives ord_p(A/B)=n.
    index, prime_product, checked = 0, 1, 0
    hits = []
    for a in range(2, height + 1):
        c = a**n
        while index < len(eligible) and eligible[index] <= k*a*a:
            prime_product *= eligible[index]
            index += 1
        for b in range(1, a):
            if gcd(a, b) != 1:
                continue
            checked += 1
            phi = cyclotomic(n, a, b)
            lower = a-b if n == 7 else a**3-b**3
            assert phi * lower == c - b**n and phi < k*a**6
            rad_lower = trial_radical(a-b)
            if n == 9:
                rad_lower = lcm(rad_lower, trial_radical(a*a + a*b + b*b))
            r = lcm(trial_radical(a), trial_radical(b), rad_lower, sextic_radical(phi, prime_product))
            if pari_radical is not None:
                assert r == lcm(*(pari_radical(x) for x in (a, b, lower, phi)))
            if c > r:
                hits.append((a, b, r))
    return checked, hits


def top_three(n, hits):
    # Float scores propose groups and separators. Integer powers certify each
    # selected group lies strictly above every remaining quality, including ties.
    groups = {}
    for a, b, r in hits:
        groups.setdefault((a**n, r), []).append((a, b))
    ordered = sorted(groups, key=lambda pair: log(pair[0])/log(pair[1]), reverse=True)
    for rank, (c, r) in enumerate(ordered[:3], 1):
        remaining = ordered[rank:]
        high = log(c)/log(r)
        low = log(remaining[0][0])/log(remaining[0][1]) if remaining else 1.0
        assert low < high
        for denominator in count(1):
            numerator = int(low*denominator) + 1
            if numerator < high*denominator:
                break
        assert c**denominator > r**numerator
        assert all(x**denominator < y**numerator for x, y in remaining)
        for a, b in groups[c, r]:
            print(f'  {rank}. (A,B)=({a},{b}), C={c}, R={r}, quality={high:.12f}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pari', action='store_true', help='recheck every row by proved PARI factorization')
    parser.add_argument('--hits', action='store_true', help='also list every row with quality above 21/20')
    args = parser.parse_args()
    height = 500
    primes = primes_through(7*height**2)
    checker = pari_checker() if args.pari else None
    for n in (7, 9):
        checked, hits = census(n, height, primes, checker)
        strong = [(a, b, r) for a, b, r in hits if a**(20*n) > r**21]
        print(f'n={n}: {checked} coprime pairs, {len(hits)} above 1, {len(strong)} above 21/20.')
        top_three(n, hits)
        if args.hits:
            print('n,A,B,radical')
            for a, b, r in strong:
                print(n, a, b, r, sep=',')


if __name__ == '__main__':
    main()

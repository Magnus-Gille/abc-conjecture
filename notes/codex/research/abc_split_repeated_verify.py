"""Verify scalar valuations, CM packets and inherited-density sums in the C++ scan."""
from argparse import ArgumentParser
from collections import Counter
from itertools import combinations
from math import gcd, isqrt, prod
from pathlib import Path

from abc_odd_rank_quartic_cutoff import all_primes, full_packet, split_generator
from abc_odd_rank_squareclass_support import division_values, largest_prime_factors, small_prime_orders
from abc_octic_scalar_rank_verify import is_proven_prime


def abscissa(n, p, w):
    """x(nR), using the division polynomials on the displayed integral curve."""
    v = w(n)
    assert v
    return (-8 - w(n-1)*w(n+1)*pow(v*v, -1, p)) % p


def proper(q, p):
    a, b = split_generator(q)
    w = division_values(p)
    x, u = abscissa(a, p, w), abscissa(b, p, w)
    # x([tau]bR) is rational and conjugation negates its ordinate.
    return (2*u*x + u*u + 16*u + 32) % p == 0


def verify(path):
    rows = [tuple(map(int, line.split())) for line in Path(path).read_text().splitlines()]
    assert len(rows) == len(set(rows))
    trial_primes = all_primes(isqrt(max((p for _, p in rows), default=4)))

    def prime(n):
        if n < 2:
            return False
        for ell in trial_primes:
            if ell*ell > n:
                break
            if n % ell == 0:
                return False
        return True

    counts, full, repeated = Counter(), set(), []
    for q, p in rows:
        assert q >= 11 and q % 8 in (1,3) and p > q and prime(q) and prime(p)
        assert division_values(p)(q) == 0
        e = 1
        while division_values(p**(e+1))(q) == 0:
            e += 1
        packet = 'M' if proper(q, p) else 'C'
        if q < 100:
            assert (full_packet(q) % p == 0) == (packet == 'C')
        counts[packet] += 1
        if packet == 'C':
            full.add((q,p))
        if e > 1:
            repeated.append((q,p,e,packet))
    indices = {q for q,p in full}
    print('scalar pairs', len(rows), 'by packet', dict(counts), 'distinct full indices', len(indices),
          'max full q', max(indices, default=0), 'repeated', repeated)
    return full


def independent_check(full, bound):
    # The independent method traverses p and factors possible Frobenius group orders.
    factors = largest_prime_factors(bound + 3*isqrt(bound) + 10)
    buckets = small_prime_orders(bound, factors)
    independent = {(q,p) for q, ps in buckets.items() if q > 3 and q % 8 in (1,3)
                   for p in ps if not proper(q,p)}
    assert independent == {(q,p) for q,p in full if p <= bound}
    print('independent cutoff', bound, 'pairs', len(independent))


def density_sums(full):
    precision = 10**28
    moduli = [q*p for q,p in full]
    upper = sum(1 + (precision-1)//d for d in moduli)
    lower = sum(precision//d for d in moduli)
    for a,b in combinations(moduli, 2):
        lower -= 1 + (precision-1)//(a//gcd(a,b)*b)
    prime_weight = sum(1 + (precision-1)//p for _,p in full)
    print('scaled Bonferroni lower, union upper, harmonic upper, scale',
          lower, upper, prime_weight, precision)
    print('sum split prime indices from 11 through 11000',
          sum(q for q in all_primes(11000) if q >= 11 and q % 8 in (1,3)))


def small_exact():
    cases = {
        11: (82633, 1781803),
        17: (281297284141331716203233329,),
        19: (2243, 223902803, 22298211521, 519424618619),
    }
    for q, primes in cases.items():
        assert len(set(primes)) == len(primes)
        assert all(is_proven_prime(p) for p in primes)
        assert full_packet(q) == prod(primes)


if __name__ == '__main__':
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('path', nargs='?', default=Path(__file__).with_name('abc_split_repeated_pairs.tsv'))
    parser.add_argument('--independent-cutoff', type=int)
    args = parser.parse_args()
    small_exact()
    full = verify(args.path)
    density_sums(full)
    if args.independent_cutoff:
        independent_check(full, args.independent_cutoff)

"""Find all coprime 1 <= B < A <= 40, 2 <= n <= 300 with P+(A^n-B^n) <= n^2."""

import argparse
from math import gcd, log, prod

from abc_average_order_check import prime_divisors
from abc_mersenne_all_indices_scan import odd_prime_sieve


def prime_products(limit):
    flags = odd_prime_sieve(limit**2)
    primes = [2] + [p for p in range(3, limit**2 + 1, 2) if flags[p//2]]
    row_product = [1] * (limit + 1)
    full_product = [1] * (limit + 1)
    index = 0
    for n in range(2, limit + 1):
        full_product[n] = full_product[n-1]
        while index < len(primes) and primes[index] <= n*n:
            full_product[n] *= primes[index]
            index += 1
        step = 2*n if n % 2 else n
        row_product[n] = prod(prime_divisors(n)) * prod(
            p for p in range(1 + step, n*n + 1, step) if flags[p//2])
    return row_product, full_product


def smooth_radical(value, prime_product):
    """The exact radical if all factors lie in this squarefree product, else 0."""
    radical = gcd(value, prime_product)
    rest = value // radical
    while rest > 1:
        removable = gcd(rest, radical)
        if removable == 1:
            return 0
        rest //= removable
    return radical


def scan(height, limit):
    row_product, full_product = prime_products(limit)
    powers = [[a**n for n in range(limit + 1)] for a in range(height + 1)]
    hits = []
    cyclotomic_hits = []
    seeds = 0
    for a in range(2, height + 1):
        for b in range(1, a):
            if gcd(a, b) != 1:
                continue
            seeds += 1
            base_rad = prod(prime_divisors(a*b))
            terms = [x-y for x, y in zip(powers[a], powers[b])]
            phi = terms.copy()
            for d in range(1, limit + 1):
                for j in range(2*d, limit + 1, d):
                    phi[j], rem = divmod(phi[j], phi[d])
                    assert rem == 0
            for n in range(2, limit + 1):
                # For p dividing Phi_n(A,B) but not n, separability of T^n-1
                # gives ord_p(A/B)=n. Hence only p|n or p=1 mod n can occur.
                radical = 0
                row_rad = smooth_radical(phi[n], row_product[n])
                if row_rad:
                    cyclotomic_hits.append((a, b, n))
                    radical = smooth_radical(terms[n], full_product[n])
                if n <= 6 or (a <= 6 and n <= 12):
                    factors = tuple(prime_divisors(terms[n]))
                    assert radical == (prod(factors) if max(factors) <= n*n else 0)
                    assert bool(row_rad) == all(p <= n*n for p in prime_divisors(phi[n]))
                if radical:
                    hits.append((a, b, n, base_rad * radical))
    return seeds, hits, cyclotomic_hits


def report_best(hits):
    # Exactly one row exceeds 4/3. Its ranking follows from integer powers.
    winners = [(a, b, n, r) for a, b, n, r in hits if a**(3*n) > r**4]
    assert len(winners) == 1
    a, b, n, r = winners[0]
    print(f'Best (A,B,n): {(a, b, n)}, C={a**n}, radical={r}, '
          f'quality={n*log(a)/log(r):.12f}; unique row above 4/3.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--all', action='store_true', help='also print every qualifying row and radical')
    parser.add_argument('--by-seed', action='store_true', help='also group seeds by their largest qualifying n')
    args = parser.parse_args()
    height, limit = 40, 300
    seeds, hits, cyclotomic_hits = scan(height, limit)
    active = {(a, b) for a, b, n, r in hits}
    print(f'{seeds} coprime seeds, {seeds * (limit - 1)} rows; '
          f'{len(hits)} hits on {len(active)} seeds.')
    for minimum in (2, 3):
        largest = max(n for a, b, n, r in hits if a >= minimum)
        seeds_at_max = [(a, b) for a, b, n, r in hits if a >= minimum and n == largest]
        print(f'A >= {minimum}: maximum n={largest}, attained at {seeds_at_max}.')
    report_best(hits)
    print(f'Complete cyclotomic rows with all primes <= n^2: {len(cyclotomic_hits)} '
          f'on {len({(a, b) for a, b, n in cyclotomic_hits})} seeds.')
    for minimum in (2, 3):
        selected = [(a, b, n) for a, b, n in cyclotomic_hits if a >= minimum]
        largest = max(n for a, b, n in selected)
        seeds_at_max = [(a, b) for a, b, n in selected if n == largest]
        print(f'Cyclotomic, A >= {minimum}: {len(selected)} rows, maximum n={largest}, '
              f'attained at {seeds_at_max}.')
    if args.by_seed:
        # Each seed's rows are visited in ascending index order.
        maxima = {(a, b): n for a, b, n, r in hits}
        for n in sorted(set(maxima.values()), reverse=True):
            print(f'Maximum {n}:', ' '.join(f'({a},{b})' for (a, b), m in maxima.items() if m == n))
    if args.all:
        print('A,B,n,abc_radical')
        for row in hits:
            print(*row, sep=',')


if __name__ == '__main__':
    main()

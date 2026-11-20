"""Exact product checks for logarithmic sums over m < n <= N at fixed X.

A prime p <= X with p not dividing AB and r = ord_p(A/B) contributes p once
to the first-occurrence product if m < r <= N. Its exponent in the product
of truncated radicals of A^n-B^n is floor(N/r) - floor(m/r).
"""

from math import gcd, isqrt, prod


def primes_through(limit):
    sieve = bytearray(b'\x01') * (limit + 1)
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            sieve[p*p::p] = bytes(len(range(p*p, limit + 1, p)))
    return [p for p in range(2, limit + 1) if sieve[p]]


def prime_divisors(n):
    p = 2
    while p*p <= n:
        if n % p == 0:
            yield p
            while n % p == 0:
                n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        yield n


def order_counts(a, b, low, high, primes):
    first_product = radical_product = 1
    first_count = incidence_count = 0
    for p in primes:
        if a % p == 0 or b % p == 0:
            continue
        base = a * pow(b, -1, p) % p
        order = p - 1
        for q in prime_divisors(p - 1):
            while order % q == 0 and pow(base, order // q, p) == 1:
                order //= q
        if low < order <= high:
            first_product *= p
            first_count += 1
        count = high // order - low // order
        radical_product *= p**count
        incidence_count += count
    return (first_product, radical_product), (first_count, incidence_count)


def products_from_terms(radicals, low):
    seen = first_product = radical_product = 1
    for n, radical in enumerate(radicals, 1):
        new = radical // gcd(radical, seen)
        seen *= new
        if n > low:
            first_product *= new
            radical_product *= radical
    return first_product, radical_product


def main():
    pairs = ((2, 1), (3, 1), (5, 3), (7, 4), (15, 14))
    windows = ((0, 1), (0, 12), (4, 12), (11, 12))
    cutoffs = (1, 2, 3, 7, 31, 97)
    checked = 0
    for a, b in pairs:
        assert a > b >= 1 and gcd(a, b) == 1
        # Fully factor each actual term independently of the modular orders.
        support = [tuple(prime_divisors(a**n - b**n)) for n in range(1, 13)]
        for cutoff in cutoffs:
            primes = primes_through(cutoff)
            radicals = [prod(p for p in factors if p <= cutoff) for factors in support]
            for low, high in windows:
                expected, _ = order_counts(a, b, low, high, primes)
                actual = products_from_terms(radicals[:high], low)
                assert actual == expected and gcd(actual[1], a*b) == 1
                assert (actual[1] % 2 == 0) == (cutoff >= 2 and a % 2 == b % 2 == 1)
                checked += 1
    print(f'Direct trial factorization verified both identities in {checked} cases.')

    # A gcd with the squarefree primorial extracts the truncated radical exactly.
    low, high, cutoff = 0, 1000, 100_000
    primes = primes_through(cutoff)
    primorial = prod(primes)
    radicals = (gcd((1 << n) - 1, primorial) for n in range(1, high + 1))
    expected, (first, incidences) = order_counts(2, 1, low, high, primes)
    assert products_from_terms(radicals, low) == expected
    print(f'2^n-1, n <= {high}, p <= {cutoff}: {first} distinct primes, '
          f'{incidences} prime incidences; both weighted products agree exactly.')


if __name__ == '__main__':
    main()

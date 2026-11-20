"""Exact checks on signed binomial products and their arithmetic support."""

from math import comb, factorial, gcd, isqrt, prod


def primes_up_to(limit):
    sieve = bytearray(b"\1") * (limit + 1)
    sieve[:2] = b"\0\0"
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p :: p] = bytes((limit - p * p) // p + 1)
    return [p for p in range(2, limit + 1) if sieve[p]]


def v2(number):
    assert number > 0
    return (number & -number).bit_length() - 1


for n in range(2, 130, 2):
    x = 2 * n + 1
    terms = [x + 2 * j for j in range(n + 1)]
    weights = [(-1) ** j * comb(n, j) for j in range(n + 1)]
    exponent = n + v2(factorial(n - 1))
    modulus = 1 << (exponent + 1)
    ratio = 1
    for value, weight in zip(terms, weights):
        ratio = ratio * pow(value, weight, modulus) % modulus
    assert ratio == 1 + (1 << exponent)

    for p in primes_up_to(4 * n + 1):
        if p == 2:
            continue
        sums = [0] * p
        present = [False] * p
        for j, weight in enumerate(weights):
            sums[j % p] += weight
            present[j % p] = True
        assert all(bool(s) == seen for s, seen in zip(sums, present))
        if p * p > 4 * n + 1:
            valuation = sum(w for t, w in zip(terms, weights) if t % p == 0)
            allowed = p <= (4 * n + 1) // 3 or p >= 2 * n + 1
            assert bool(valuation) == allowed

    if n <= 10:
        numerator = prod(t ** w for t, w in zip(terms, weights) if w > 0)
        denominator = prod(t ** -w for t, w in zip(terms, weights) if w < 0)
        common = gcd(numerator, denominator)
        u, v = numerator // common, denominator // common
        assert gcd(u, v) == 1 and v2(abs(u - v)) == exponent
        if n == 4:
            assert sorted([u, v, abs(u - v)]) == [299872, 82055753, 82355625]

print("Verified exact dyadic depth and prime support at every even index through 128.")

"""Search every layer (4^(2*3^n) + 4^(3^n) + 1)/3 for primes up to a bound."""

import argparse
from itertools import compress
from math import isqrt


def primes_through(limit):
    if limit < 2:
        return
    yield 2
    root = isqrt(limit)
    small = bytearray([1]) * (root + 1)
    for p in range(2, isqrt(root) + 1):
        if small[p]:
            small[p * p :: p] = bytes((root - p * p) // p + 1)
    sieving_primes = list(compress(range(3, root + 1, 2), small[3::2]))
    span = 2 ** 21
    for low in range(3, limit + 1, span):
        high = min(low + span, limit + 1)
        odds = range(low, high, 2)
        flags = bytearray([1]) * len(odds)
        for p in sieving_primes:
            if p * p >= high:
                break
            first = max(p * p, low + (-low) % p)
            if first % 2 == 0:
                first += p
            offset = (first - low) // 2
            if offset < len(flags):
                flags[offset::p] = bytes((len(flags) - 1 - offset) // p + 1)
        yield from compress(odds, flags)


def layer_for_prime(base, p):
    """Find n with ord_p(base) = 3^(n+1), if it exists."""
    residue = base % p
    if residue in (0, 1):
        return None
    remaining = p - 1
    n = 0
    while remaining % 3 == 0:
        residue = pow(residue, 3, p)
        if residue == 1:
            return n
        n += 1
        remaining //= 3
    return None


def square_divides_layer(base, p, n):
    residue = pow(base, 3**n, p * p)
    return (residue * residue + residue + 1) % (p * p) == 0


def self_check():
    assert list(primes_through(20)) == [2, 3, 5, 7, 11, 13, 17, 19]
    # Positive control: 18^2 + 18 + 1 = 7^3.
    assert layer_for_prime(18, 7) == 0 and square_divides_layer(18, 7, 0)
    for n in range(5):
        x = 4 ** (3**n)
        u = (x * x + x + 1) // 3
        for p in primes_through(10000):
            if p in (2, 3):
                assert u % p != 0
                continue
            assert (layer_for_prime(4, p) == n) == (u % p == 0)
            assert square_divides_layer(4, p, n) == (u % (p * p) == 0)


def run(limit):
    self_check()
    count = 0
    divisors = []
    square_hits = []
    for p in primes_through(limit):
        count += 1
        if p % 3 != 1:
            continue
        n = layer_for_prime(4, p)
        if n is None:
            continue
        divisors.append((n, p))
        if square_divides_layer(4, p, n):
            square_hits.append((n, p))
    print(f"prime bound = {limit}, primes enumerated = {count}")
    print(f"ordinary divisors (n, p), count = {len(divisors)}: {sorted(divisors)}")
    print(f"square divisors (n, p), count = {len(square_hits)}: {sorted(square_hits)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=10**9)
    run(parser.parse_args().limit)

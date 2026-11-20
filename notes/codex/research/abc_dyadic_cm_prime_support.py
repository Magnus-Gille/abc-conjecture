"""Certify the prime support through n^4 for the dyadic packets up to n=8192."""

import math
import sys
from itertools import compress

from flint import fmpz


def roots_to(limit):
    roots = []
    for prime in range(3, limit + 1, 2):
        if any(prime % d == 0 for d in range(3, math.isqrt(prime) + 1, 2)):
            continue
        root = next((s for s in range(prime) if (s*s + 2) % prime == 0), None)
        roots.append((prime, root))
    return roots


def disk_gcd(n, w):
    """Remove certified composites from the disk and multiply the rest modulo w."""
    cutoff = n**4
    sieve = [(p, s, pow(n, -1, p)) for p, s in roots_to(min(521, 2*n*n - 1))]
    buckets = []
    seen = 0
    bits = w.bit_length()
    for b in range(1, math.isqrt(cutoff // 2) // n + 1):
        vertical = 2 * (n*b)**2
        width = math.isqrt(cutoff - vertical)
        low = -((width + 1) // n)
        high = (width - 1) // n
        length = high - low + 1
        if length <= 0:
            continue
        seen += length
        marks = bytearray([1]) * length
        for prime, root, inverse in sieve:
            if root is None:
                if b % prime:
                    continue
                offsets = [(-inverse - low) % prime]
            else:
                offsets = [(sign*root*b - inverse - low) % prime for sign in (1, -1)]
            for start in offsets:
                if start < length:
                    count = (length - 1 - start) // prime + 1
                    marks[start::prime] = bytes(count)
        terms = [(1 + n*a)**2 + vertical for a in compress(range(low, high+1), marks)]
        # Binary product tree keeps only logarithmically many partial products.
        for offset in range(0, len(terms), 64):
            value = fmpz(math.prod(terms[offset:offset+64]))
            level = 0
            while level < len(buckets) and buckets[level] is not None:
                value *= buckets[level]
                buckets[level] = None
                if value.bit_length() > 2*bits:
                    value %= w
                level += 1
            if level == len(buckets):
                buckets.append(value)
            else:
                buckets[level] = value
    product = fmpz(1)
    for value in buckets:
        if value is not None:
            product = product * value % w
    return product.gcd(w), seen


def decimal_digits(value):
    exponent = int(value.bit_length() * math.log10(2))
    base = fmpz(10)**exponent
    assert base <= 10*value and value < 10*base
    return exponent + 1 if value >= base else exponent


EXPECTED = {
    8: (61, 4, [(2273, 1)], 1),
    16: (268, 14, [], 14),
    32: (1102, 54, [], 54),
    64: (4482, 214, [], 214),
    128: (18068, 855, [(67649537, 1)], 847),
    256: (72526, 3417, [], 3417),
    512: (290642, 13666, [(339767297, 1)], 13657),
    1024: (1163655, 54662, [], 54662),
    2048: (4656634, 218645, [], 218645),
    4096: (18630663, 874580, [], 874580),
    8192: (74530936, 3498318, [(65229783041, 1)], 3498307),
}


def census(maximum):
    u, v = fmpz(31), fmpz(14)
    n = 8
    while n <= maximum:
        uu, vv = u*u, v*v
        quartic = uu*uu + 16*uu*vv + 32*vv*vv
        w = quartic.sqrt()
        assert w*w == quartic
        divisor, norm_count = disk_gcd(n, w)
        remainder = w
        factors = []
        for prime, _ in divisor.factor():
            assert prime.is_prime() and prime <= n**4
            exponent = 0
            while remainder % prime == 0:
                remainder //= prime
                exponent += 1
            factors.append((int(prime), exponent))
        assert remainder.gcd(divisor) == 1
        row = (norm_count, decimal_digits(w), factors, decimal_digits(remainder))
        assert row == EXPECTED[n]
        if n >= 16:
            assert remainder > 1
        if n in (16, 32):
            full = {16: [22151840117633],
                    32: [2401379840999699201, 100264636730315412574143047918721793]}[n]
            assert math.prod(full) == w and all(fmpz(p).is_prime() for p in full)
        print(n, *row, flush=True)
        if n == maximum:
            break
        u, v = abs(uu*uu - 32*vv*vv), 2*u*v*w
        assert u.gcd(v) == 1
        n *= 2


if __name__ == '__main__':
    maximum = int(sys.argv[1]) if len(sys.argv) > 1 else 8192
    if maximum not in EXPECTED:
        raise ValueError('Choose a power of two from 8 through 8192')
    census(maximum)

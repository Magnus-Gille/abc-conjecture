"""Exact census of n with every prime divisor of 2^n-1 at most n^2."""

import argparse
import json
from functools import cache
from math import gcd, isqrt, prod
from pathlib import Path


def odd_prime_sieve(limit):
    # Entry i tests 2*i+1. The default cutoff uses 50 MB for the sieve.
    flags = bytearray(b'\x01') * ((limit + 1) // 2)
    flags[0] = 0
    for p in range(3, isqrt(limit) + 1, 2):
        if flags[p//2]:
            start = p*p//2
            flags[start::p] = bytes(len(range(start, len(flags), p)))
    return flags


def cyclotomic_values(limit):
    values = [(1 << n) - 1 for n in range(limit + 1)]
    for d in range(2, limit + 1):
        for multiple in range(2*d, limit + 1, d):
            values[multiple], remainder = divmod(values[multiple], values[d])
            assert remainder == 0
    return values  # 2^n-1 = product of Phi_d(2) over all d | n, with Phi_1(2)=1


def strip_primes(value, candidates, prime_flags):
    factors = {}
    for p in candidates:
        if value == 1:
            break
        if prime_flags[p//2] and value % p == 0:
            exponent = 0
            while value % p == 0:
                value //= p
                exponent += 1
            factors[p] = exponent
    return factors, value


def primitive_row(n, phi, prime_flags):
    # For p not dividing n, X^n-1 is separable modulo p. Therefore a prime
    # dividing Phi_n(2) has order exactly n unless p divides n. A prime
    # dividing n itself cannot have order n, since its order divides p-1.
    part = phi
    common = gcd(part, n)
    while common > 1:
        part //= common
        common = gcd(part, n)
    step = n if n % 2 == 0 else 2*n  # odd primes of order n are 1 modulo n
    small, rest = strip_primes(part, range(step + 1, n*n + 1, step), prime_flags)
    assert part == rest * prod(p**e for p, e in small.items())
    return small, rest


def trial_factors(value):
    factors = {}
    p = 3
    while p*p <= value:
        while value % p == 0:
            factors[p] = factors.get(p, 0) + 1
            value //= p
        p += 2
    if value > 1:
        factors[value] = 1
    return factors


def check_small(n, small, rest, whole_is_smooth):
    factors = trial_factors((1 << n) - 1)
    primitive = {p: e for p, e in factors.items()
                 if next(j for j in range(1, n + 1) if pow(2, j, p) == 1) == n}
    assert small == {p: e for p, e in primitive.items() if p <= n*n}
    assert rest == prod(p**e for p, e in primitive.items() if p > n*n)
    assert whole_is_smooth == (max(factors) <= n*n)


def check_simple_witnesses():
    """Verify one exact-order prime of depth one per positive row."""
    path = Path(__file__).with_name('abc_mersenne_simple_prime_certificates.json')
    data = json.loads(path.read_text())

    @cache
    def prove_prime(p):
        if p <= 2**32:
            assert p == 2 or (p > 2 and p % 2 and
                              all(p % i for i in range(3, isqrt(p) + 1, 2)))
            return
        base, divisors = data['pocklington'][str(p)]
        assert 1 < base < p and pow(base, p - 1, p) == 1
        remainder = p - 1
        for q in divisors:
            assert 1 < q < p and remainder % q == 0
            prove_prime(q)
            while remainder % q == 0:
                remainder //= q
            assert gcd(pow(base, (p - 1)//q, p) - 1, p) == 1
        # Pocklington's theorem applies to the proved part F of p-1.
        proved_part = (p - 1) // remainder
        assert proved_part**2 > p

    limit = data['limit']
    rows = data['witnesses']  # Entry n-2 gives p, or zero for an exhausted row.
    assert len(rows) == limit - 1
    flags = odd_prime_sieve(limit*limit)
    primes = [2] + [q for q in range(3, limit + 1, 2) if flags[q//2]]
    values = cyclotomic_values(limit)
    absent = []
    for n, p in enumerate(rows, 2):
        if p == 0:
            _, rest = primitive_row(n, values[n], flags)
            assert rest == 1
            absent.append(n)
            continue
        prove_prime(p)
        assert p > n*n and pow(2, n, p) == 1 and pow(2, n, p*p) != 1
        assert all(pow(2, n//q, p) != 1 for q in primes if n % q == 0)
    print(f'Certified simple primes > n^2 of exact order n: {len(rows) - len(absent)} '
          f'of {len(rows)} indices from 2 through {limit}.')
    print('Exhausted rows:', *absent)


def main(limit=10_000):
    flags = odd_prime_sieve(limit*limit)
    values = cyclotomic_values(limit)
    primitive_smooth = []
    whole_smooth = []
    for n in range(2, limit + 1):
        small, rest = primitive_row(n, values[n], flags)
        whole_is_smooth = False
        if rest == 1:
            primitive_smooth.append((n, max(small, default=None)))
            whole, leftover = strip_primes((1 << n) - 1, range(3, n*n + 1, 2), flags)
            whole_is_smooth = leftover == 1
            if whole_is_smooth:
                whole_smooth.append((n, max(whole)))
        if n <= 30:
            check_small(n, small, rest, whole_is_smooth)

    print(f'Checked {limit - 1} indices from 2 through {limit}.')
    print(f'All primitive primes <= n^2 ({len(primitive_smooth)}):')
    print(' '.join(f'{n}:{p if p is not None else "empty"}' for n, p in primitive_smooth))
    print(f'All primes of 2^n-1 <= n^2 ({len(whole_smooth)}):')
    print(' '.join(f'{n}:{p}' for n, p in whole_smooth))
    print('Entries give n:largest prime in each row. Trial factorization agrees through 30.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--simple', action='store_true',
                        help='verify the included simple-prime certificates')
    if parser.parse_args().simple:
        check_simple_witnesses()
    else:
        main()

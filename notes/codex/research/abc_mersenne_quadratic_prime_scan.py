"""Certify which prime powers n <= 10,000 have no primitive p > n^2 in 2^n-1."""

from math import isqrt, prod


def primes_through(limit):
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[:2] = b'\x00\x00'
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            sieve[p*p::p] = bytes(len(range(p*p, limit + 1, p)))
    return [p for p in range(2, limit + 1) if sieve[p]]


def is_prime(n, trial_primes):
    for p in trial_primes:
        if p*p > n:
            break
        if n % p == 0:
            return False
    return n >= 2


def strip(value, factor):
    exponent = 0
    while value % factor == 0:
        value //= factor
        exponent += 1
    return value, exponent


def primitive_part(n, q, trial_primes):
    phi = ((1 << n) - 1) // ((1 << (n//q)) - 1)
    remaining, imprimitive = strip(phi, q)
    # If p | Phi and 2^(n/q) = 1 mod p, the q-term geometric sum gives p | q.
    # Moreover Phi = 1 mod q here, by 2^(q^j) = 2 mod q (also for q=2).
    assert imprimitive == 0
    factors = {}
    step = n if n % 2 == 0 else 2*n
    for candidate in range(1 + step, n*n + 1, step):
        if remaining % candidate or not is_prime(candidate, trial_primes):
            continue
        assert pow(2, n, candidate) == 1 and pow(2, n//q, candidate) != 1
        remaining, factors[candidate] = strip(remaining, candidate)
        if remaining == 1:
            break
    assert phi == remaining * prod(p**e for p, e in factors.items())
    return factors, remaining


def direct_factors(n):
    """Independent trial factorization of 2^n-1, followed by direct order tests."""
    value = (1 << n) - 1
    factors = {}
    p = 3
    while p*p <= value:
        if value % p == 0:
            value, factors[p] = strip(value, p)
        p += 2
    if value > 1:
        factors[value] = 1
    return {p: e for p, e in factors.items()
            if next(j for j in range(1, n + 1) if pow(2, j, p) == 1) == n}


def main(limit=10_000):
    # Candidates never exceed limit^2, so trial primes up to limit prove primality.
    primes = primes_through(limit)
    indices = []
    for q in primes:
        n = q
        while n <= limit:
            indices.append((n, q))
            n *= q

    exceptions = []
    small_hits = 0
    largest_hit = (0, 0)
    for n, q in sorted(indices):
        factors, remaining = primitive_part(n, q, primes)
        if n <= 25:
            direct = direct_factors(n)
            assert factors == {p: e for p, e in direct.items() if p <= n*n}
            assert remaining == prod(p**e for p, e in direct.items() if p > n*n)
        small_hits += len(factors)
        if factors:
            largest_hit = max(largest_hit, (max(factors), n))
        if remaining == 1:
            exceptions.append((n, factors))

    print(f'Prime-power indices through {limit}: {len(indices)}; '
          f'with a primitive prime > n^2: {len(indices) - len(exceptions)}.')
    print(f'Primitive primes <= n^2 across all indices: {small_hits}; '
          f'largest {largest_hit[0]} at n={largest_hit[1]}.')
    print('All exceptions (n, complete primitive factorization, largest prime):')
    for n, factors in exceptions:
        product = ' * '.join(str(p) if e == 1 else f'{p}^{e}' for p, e in factors.items())
        print(f'  {n}: {product or "1"}; largest {max(factors, default=None)}')
    print('Direct factorization agrees at every prime-power index through 25.')


if __name__ == '__main__':
    main()

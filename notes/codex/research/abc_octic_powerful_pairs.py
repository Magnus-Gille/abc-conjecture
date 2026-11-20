"""Enumerate squareful/cubeful pairs for (s-t)^2+t^2 and (s+t)^2+t^2."""

import argparse
from math import gcd, isqrt


def primes_through(bound):
    sieve = bytearray([1]) * (bound + 1)
    sieve[:2] = bytes(2)
    for p in range(2, isqrt(bound) + 1):
        if sieve[p]:
            sieve[p * p :: p] = bytes((bound - p * p) // p + 1)
    return [p for p in range(5, bound + 1, 4) if sieve[p]]


def cube_root(value):
    low, high = 0, 1
    while high**3 <= value:
        high *= 2
    while high - low > 1:
        mid = (high + low) // 2
        if mid**3 <= value:
            low = mid
        else:
            high = mid
    return low


def gaussian_prime(p):
    for y in range(2, isqrt(p) + 1, 2):
        x = isqrt(p - y * y)
        if x * x + y * y == p:
            return x, y
    raise ArithmeticError(f"No Gaussian factor of split prime {p}")


def multiply(z, w):
    x, y = z
    a, b = w
    return x * a - y * b, x * b + y * a


def squareful(n, split_primes):
    if isqrt(n)**2 == n:
        return True
    for p in split_primes:
        if p**3 > n:
            break
        if n % p:
            continue
        n //= p
        if n % p:
            return False
        while n % p == 0:
            n //= p
    return isqrt(n)**2 == n


def search(height):
    limit = 5 * height**2
    primes = primes_through(cube_root(limit))
    generators = [gaussian_prime(p) for p in primes]
    tested = 0
    matches = []

    def visit(first, norm, z):
        nonlocal tested
        x, t = abs(z[0]), abs(z[1])
        if 0 < t <= height:
            # x is odd, t is even, and x=|s+t| or |s-t|.
            for s, cubeful_sign in ((x - t, 1), (t + x, -1), (t - x, -1)):
                if 0 < s <= height:
                    tested += 1
                    other = (s - cubeful_sign * t)**2 + t * t
                    if squareful(other, primes):
                        matches.append((s, t, cubeful_sign, norm, other))
        for j in range(first, len(primes)):
            p = primes[j]
            new_norm = norm * p**3
            if new_norm > limit:
                break
            pi = generators[j]
            power = multiply(multiply(pi, pi), pi)
            while new_norm <= limit:
                visit(j + 1, new_norm, multiply(z, power))
                if first:
                    # Simultaneous conjugation preserves the absolute coordinates.
                    visit(j + 1, new_norm, multiply(z, (power[0], -power[1])))
                new_norm *= p
                power = multiply(power, pi)

    visit(0, 1, (1, 0))
    return tested, sorted(matches)


def check_small(height):
    """Independent enumeration and factorization for a small box."""
    def all_exponents_at_least(n, minimum):
        k = 2
        while k * k <= n:
            valuation = 0
            while n % k == 0:
                n //= k
                valuation += 1
            if 0 < valuation < minimum:
                return False
            k += 1
        return n == 1

    expected_tested = 0
    expected_matches = []
    for s in range(1, height + 1, 2):
        for t in range(2, height + 1, 2):
            if gcd(s, t) != 1:
                continue
            for sign in (1, -1):
                a = (s + sign * t)**2 + t * t
                b = (s - sign * t)**2 + t * t
                if all_exponents_at_least(a, 3):
                    expected_tested += 1
                    if all_exponents_at_least(b, 2):
                        expected_matches.append((s, t, sign, a, b))
    assert search(height) == (expected_tested, sorted(expected_matches))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("height", type=int)
    args = parser.parse_args()
    if args.height <= 0:
        parser.error("height must be positive")
    check_small(min(args.height, 128))
    n_tested, found = search(args.height)
    print(f"height={args.height}, cubeful orientations={n_tested}, matches={len(found)}")
    for row in found:
        print(*row)

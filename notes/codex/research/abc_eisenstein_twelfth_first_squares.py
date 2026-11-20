"""Check first-occurrence squares by division polynomials at P=(-2,8)."""

from argparse import ArgumentParser
from functools import cache
from math import isqrt


def prime_data(bound):
    prime = bytearray(b"\x01") * (bound + 1)
    prime[:2] = b"\x00\x00"
    for divisor in range(2, isqrt(bound) + 1):
        if prime[divisor]:
            length = (bound - divisor * divisor) // divisor + 1
            prime[divisor*divisor::divisor] = bytes(length)
    odd_part = {}
    for even in range(2, isqrt(bound) + 1, 2):
        for odd in range(1, isqrt(bound - even*even) + 1, 2):
            p = even*even + odd*odd
            if prime[p]:
                odd_part[p] = odd if (odd + even) % 4 == 1 else -odd
    return prime, odd_part


def division_at_point(index, modulus):
    initial = (0, 1, 16, -1536, 3670016)
    inverse = pow(16, -1, modulus)

    @cache
    def term(n):
        if n < len(initial):
            return initial[n] % modulus
        m = n // 2
        if n % 2:
            return (term(m+2) * pow(term(m), 3, modulus)
                    - term(m-1) * pow(term(m+1), 3, modulus)) % modulus
        middle = (term(m+2) * pow(term(m-1), 2, modulus)
                  - term(m-2) * pow(term(m+1), 2, modulus))
        return term(m) * inverse * middle % modulus

    value = term(index)
    term.cache_clear()
    return value


def first_index(multiple, prime):
    r = multiple
    remaining = multiple
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            while remaining % divisor == 0:
                remaining //= divisor
            while r % divisor == 0 and division_at_point(r // divisor, prime) == 0:
                r //= divisor
        divisor += 1
    if remaining > 1 and division_at_point(r // remaining, prime) == 0:
        r //= remaining
    return r


def scan(bound):
    prime, odd_part = prime_data(bound)
    checked, hits = 0, []
    for p in range(5, bound + 1, 2):
        if not prime[p]:
            continue
        multiple = p + 1
        if p % 4 == 1:
            twist = 1 if pow(24, (p-1)//2, p) == 1 else -1
            multiple -= 2 * odd_part[p] * twist
        value = division_at_point(multiple, p*p)
        if multiple % p == 0 or value % p:
            raise ArithmeticError(f"Invalid annihilating multiple for {p}")
        checked += 1
        if value == 0:
            r = first_index(multiple, p)
            exponent = 2
            while division_at_point(r, p ** (exponent+1)) == 0:
                exponent += 1
            hits.append((p, r, exponent))
    return checked, hits


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("bound", type=int, nargs="?", default=100000)
    args = parser.parse_args()
    count, hits = scan(args.bound)
    print(f"Checked {count} good primes through {args.bound}.")
    print(f"(prime, first index, valuation): {hits}")

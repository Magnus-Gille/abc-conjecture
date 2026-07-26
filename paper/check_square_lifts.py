#!/usr/bin/env python3
"""Search for square prime divisors in the quadratic abc orbit.

For each prime p, iterate

    c_0 = 9, d_0 = -7,
    c_{j+1} = c_j^2,
    d_{j+1} = c_j^2 - 2 d_j^2

modulo p^2.  A reported pair (p, j) is therefore an exact certificate
that p^2 divides d_j.  No large d_j is constructed.
"""

from __future__ import annotations

import argparse
import math


def primes_up_to(limit: int) -> list[int]:
    """Return all primes <= limit using the sieve of Eratosthenes."""
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (
                (limit - start) // p + 1
            )
    return [p for p, is_prime in enumerate(sieve) if is_prime]


def first_square_lift(p: int, max_j: int) -> int | None:
    """Return the first j <= max_j with p^2 | d_j, or None.

    Once p | d_j but p^2 does not divide d_j, pairwise coprimality of the
    integer sequence proves that p cannot occur at a later index.
    """
    modulus = p * p
    c = 9 % modulus
    d = -7 % modulus
    for j in range(max_j + 1):
        if d % p == 0:
            return j if d == 0 else None
        d = (c * c - 2 * d * d) % modulus
        c = c * c % modulus
    return None


def self_check() -> None:
    """Compare modular and exact recurrences on a small deterministic case."""
    exact_c, exact_d = 9, -7
    exact = []
    for _ in range(8):
        exact.append(exact_d)
        exact_d = exact_c * exact_c - 2 * exact_d * exact_d
        exact_c *= exact_c

    for p in primes_up_to(1_000):
        if p in (2, 3):
            continue
        expected = next(
            (j for j, d in enumerate(exact) if d % (p * p) == 0),
            None,
        )
        observed = first_square_lift(p, len(exact) - 1)
        if observed != expected:
            raise AssertionError(
                f"self-check failed for p={p}: {observed=} {expected=}"
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-limit", type=int, default=10_000_000)
    parser.add_argument("--max-j", type=int, default=50)
    parser.add_argument(
        "--skip-self-check",
        action="store_true",
        help="skip the exact-versus-modular test for primes <= 1000",
    )
    args = parser.parse_args()

    if args.prime_limit < 2:
        parser.error("--prime-limit must be at least 2")
    if args.max_j < 0:
        parser.error("--max-j must be nonnegative")
    if not args.skip_self_check:
        self_check()

    hits: list[tuple[int, int]] = []
    tested = 0
    for p in primes_up_to(args.prime_limit):
        if p in (2, 3):
            continue
        tested += 1
        j = first_square_lift(p, args.max_j)
        if j is not None:
            hits.append((p, j))

    print(f"prime_limit={args.prime_limit}")
    print(f"max_j={args.max_j}")
    print(f"tested_primes={tested}")
    print(f"square_lifts={len(hits)}")
    for p, j in hits:
        print(f"p={p} j={j} p_squared={p * p}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Search for p^2 | d_j in the Chebyshev abc orbit, without huge integers."""

from __future__ import annotations

import argparse
import math


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (
                (limit - p * p) // p + 1
            )
    return [p for p, is_prime in enumerate(sieve) if is_prime]


def first_hit(p: int, max_j: int) -> tuple[int, int] | None:
    """Return (j, v>=2 lower bound) if p^2 divides d_j."""
    modulus = p * p
    c = 9 % modulus
    d = -7 % modulus
    for j in range(max_j + 1):
        if d % p == 0:
            if d == 0:
                # The modular test proves v_p(d_j) >= 2, not its exact value.
                return j, 2
            # Pairwise coprimality of the d_j means p never returns.
            return None
        d = (c * c - 2 * d * d) % modulus
        c = c * c % modulus
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-limit", type=int, default=2_000_000)
    parser.add_argument("--max-j", type=int, default=40)
    args = parser.parse_args()

    hits: list[tuple[int, int]] = []
    tested = 0
    for p in primes_up_to(args.prime_limit):
        if p in (2, 3):
            continue
        tested += 1
        hit = first_hit(p, args.max_j)
        if hit is not None:
            hits.append((p, hit[0]))

    print(f"tested_primes={tested}")
    print(f"square_lifts={len(hits)}")
    for p, j in hits:
        print(f"p={p} j={j} p^2={p*p}")


if __name__ == "__main__":
    main()

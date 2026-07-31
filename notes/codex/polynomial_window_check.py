#!/usr/bin/env python3
"""Independent arithmetic helpers for the Phase 7 window reduction.

The Lucas implementation uses binary exponentiation in
Z[X]/(X^2-PX+Q), rather than the companion-matrix implementation in
Claude's checker.  If X^n = U_n X - Q U_{n-1}, the X coefficient is U_n.
"""

import argparse
import json
from math import isqrt


CANONICAL_PAIRS = {
    "quadratic": (14, 81),
    "cubic": (-2, 25),
    "quintic": (-6, 49),
}


def _quadratic_product(left, right, p_parameter, q_parameter, modulus):
    """Multiply two a*X+b residues modulo X^2-PX+Q and ``modulus``."""
    a, b = left
    c, d = right
    return (
        (a * c * p_parameter + a * d + b * c) % modulus,
        (b * d - a * c * q_parameter) % modulus,
    )


def lucas_u_mod(index, p_parameter, q_parameter, modulus):
    """Return U_index(P,Q) modulo ``modulus`` in O(log index) products."""
    if index < 0:
        raise ValueError("index must be nonnegative")
    if modulus <= 0:
        raise ValueError("modulus must be positive")

    result = (0, 1)  # 1
    power = (1, 0)  # X
    exponent = index
    while exponent:
        if exponent & 1:
            result = _quadratic_product(
                result, power, p_parameter, q_parameter, modulus
            )
        power = _quadratic_product(
            power, power, p_parameter, q_parameter, modulus
        )
        exponent >>= 1
    return result[0]


def _legendre(symbol_argument, prime):
    residue = symbol_argument % prime
    if residue == 0:
        return 0
    return 1 if pow(residue, (prime - 1) // 2, prime) == 1 else -1


def _primes_up_to(limit):
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for candidate in range(2, isqrt(limit) + 1):
        if sieve[candidate]:
            start = candidate * candidate
            sieve[start::candidate] = b"\x00" * (
                (limit - start) // candidate + 1
            )
    return [number for number in range(2, limit + 1) if sieve[number]]


def wieferich_hits(p_parameter, q_parameter, limit):
    """List unramified p<=limit with p^2 dividing U_{p-(D|p)}(P,Q)."""
    discriminant = p_parameter * p_parameter - 4 * q_parameter
    hits = []
    for prime in _primes_up_to(limit):
        if (
            prime == 2
            or q_parameter % prime == 0
            or discriminant % prime == 0
        ):
            continue
        character = _legendre(discriminant, prime)
        if (
            lucas_u_mod(
                prime - character,
                p_parameter,
                q_parameter,
                prime * prime,
            )
            == 0
        ):
            hits.append(prime)
    return hits


def super_wieferich_hits(p_parameter, q_parameter, limit):
    """List unramified p<=limit with p^3 dividing U_{p-(D|p)}(P,Q)."""
    discriminant = p_parameter * p_parameter - 4 * q_parameter
    hits = []
    for prime in _primes_up_to(limit):
        if (
            prime == 2
            or q_parameter % prime == 0
            or discriminant % prime == 0
        ):
            continue
        character = _legendre(discriminant, prime)
        if (
            lucas_u_mod(
                prime - character,
                p_parameter,
                q_parameter,
                prime**3,
            )
            == 0
        ):
            hits.append(prime)
    return hits


def census_pair(p_parameter, q_parameter, primes):
    """Return Wieferich, depth-three, and rank data in one prime pass.

    The expensive modulus-``p**3`` calculation is performed only after the
    modulus-``p**2`` test succeeds.  ``primes`` is supplied by the caller so
    a multi-pair census can share one sieve.
    """
    discriminant = p_parameter * p_parameter - 4 * q_parameter
    hits = []
    deep_hits = []
    for prime in primes:
        if (
            prime == 2
            or q_parameter % prime == 0
            or discriminant % prime == 0
        ):
            continue
        character = _legendre(discriminant, prime)
        index = prime - character
        if (
            lucas_u_mod(
                index,
                p_parameter,
                q_parameter,
                prime * prime,
            )
            != 0
        ):
            continue
        hits.append(prime)
        if (
            lucas_u_mod(
                index,
                p_parameter,
                q_parameter,
                prime**3,
            )
            == 0
        ):
            deep_hits.append(prime)

    return {
        "wieferich": hits,
        "super_wieferich": deep_hits,
        "ranks": {
            prime: lucas_rank(p_parameter, q_parameter, prime)
            for prime in hits
        },
    }


def _positive_divisors(number):
    low = []
    high = []
    for divisor in range(1, isqrt(number) + 1):
        if number % divisor == 0:
            low.append(divisor)
            if divisor * divisor != number:
                high.append(number // divisor)
    return low + list(reversed(high))


def lucas_rank(p_parameter, q_parameter, prime):
    """Return the rank of apparition modulo an odd unramified prime."""
    discriminant = p_parameter * p_parameter - 4 * q_parameter
    if (
        prime <= 2
        or q_parameter % prime == 0
        or discriminant % prime == 0
    ):
        raise ValueError("prime must be odd, unramified, and prime to Q")
    character = _legendre(discriminant, prime)
    group_exponent = prime - character
    for divisor in _positive_divisors(group_exponent):
        if lucas_u_mod(divisor, p_parameter, q_parameter, prime) == 0:
            return divisor
    raise AssertionError("rank must divide p-(D|p)")


def deep_split_coefficients(exponents, weights, cutoff):
    """Return exact (defect, truncated, tail) for symbolic log weights."""
    if cutoff < 0:
        raise ValueError("cutoff must be nonnegative")
    defect = 0
    truncated = 0
    tail = 0
    for prime, exponent in exponents.items():
        excess = max(exponent - 1, 0)
        weight = weights[prime]
        defect += excess * weight
        truncated += min(excess, cutoff) * weight
        tail += max(excess - cutoff, 0) * weight
    return defect, truncated, tail


def canonical_census(limit):
    """Return replayable Wieferich, depth-three, and rank data."""
    primes = _primes_up_to(limit)
    return {
        name: census_pair(p_parameter, q_parameter, primes)
        for name, (p_parameter, q_parameter) in CANONICAL_PAIRS.items()
    }


def main():
    parser = argparse.ArgumentParser(
        description="Census fixed-pair Lucas-Wieferich primes"
    )
    parser.add_argument("--limit", type=int, default=100_000)
    args = parser.parse_args()
    if args.limit < 2:
        parser.error("--limit must be at least 2")
    print(json.dumps(canonical_census(args.limit), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

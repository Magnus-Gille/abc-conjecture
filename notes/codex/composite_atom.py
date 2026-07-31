#!/usr/bin/env python3
"""Exact finite checks for composite-degree Chebyshev/Lucas atoms.

The Cayley parameter is

    zeta = (1 + s) / (1 - s),  s^2 = -rho.

Its exact order labels the homogeneous coordinate atom.  Squaring zeta
labels the corresponding atom in the fixed quadratic Lucas sequence.
All finite-field arithmetic below is standard-library only.
"""

from __future__ import annotations

import math


Pair = tuple[int, int]


def prime_divisors(number: int) -> tuple[int, ...]:
    """Return the distinct prime divisors of a positive integer."""
    if number < 1:
        raise ValueError("number must be positive")

    result: list[int] = []
    remaining = number
    candidate = 2

    while candidate * candidate <= remaining:
        if remaining % candidate == 0:
            result.append(candidate)
            while remaining % candidate == 0:
                remaining //= candidate
        candidate = 3 if candidate == 2 else candidate + 2

    if remaining > 1:
        result.append(remaining)

    return tuple(result)


def euler_phi(number: int) -> int:
    """Return Euler's totient function."""
    if number < 1:
        raise ValueError("number must be positive")

    result = number
    for prime in prime_divisors(number):
        result -= result // prime
    return result


def divisors(number: int) -> tuple[int, ...]:
    """Return the positive divisors in increasing order."""
    if number < 1:
        raise ValueError("number must be positive")

    small: list[int] = []
    large: list[int] = []

    for candidate in range(1, math.isqrt(number) + 1):
        if number % candidate:
            continue
        small.append(candidate)
        partner = number // candidate
        if partner != candidate:
            large.append(partner)

    return tuple(small + list(reversed(large)))


def layer_indices(degree: int, level: int) -> tuple[int, ...]:
    """Return the Lucas-atom indices born in a degree-d layer."""
    if degree < 2:
        raise ValueError("degree must be at least two")
    if level < 0:
        raise ValueError("level must be nonnegative")

    old = set(divisors(degree**level))
    return tuple(
        index
        for index in divisors(degree ** (level + 1))
        if index not in old
    )


def coordinate_indices(lucas_index: int) -> tuple[int, ...]:
    """Return the Omega/bar-Omega atom indices above one Lucas atom.

    Homogeneous cyclotomic factorization gives

      Phi_m(Omega^2,barOmega^2)
        = Phi_m(Omega,barOmega) Phi_2m(Omega,barOmega),  m odd,
        = Phi_2m(Omega,barOmega),                         m even.
    """
    if lucas_index < 2:
        raise ValueError("Lucas index must be at least two")
    if lucas_index % 2:
        return lucas_index, 2 * lucas_index
    return (2 * lucas_index,)


def compatibility_modulus(lucas_index: int) -> int:
    """Return the congruence modulus for a universal Lucas atom."""
    if lucas_index < 2:
        raise ValueError("Lucas index must be at least two")
    return lucas_index if lucas_index % 2 else 2 * lucas_index


def _is_prime(number: int) -> bool:
    if number < 2:
        return False
    if number % 2 == 0:
        return number == 2
    candidate = 3
    while candidate * candidate <= number:
        if number % candidate == 0:
            return False
        candidate += 2
    return True


def primes_upto(limit: int) -> list[int]:
    """Return all primes at most limit by an Eratosthenes sieve."""
    if limit < 2:
        return []

    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"

    for prime in range(2, math.isqrt(limit) + 1):
        if not sieve[prime]:
            continue
        start = prime * prime
        sieve[start : limit + 1 : prime] = b"\x00" * (
            (limit - start) // prime + 1
        )

    return [number for number in range(2, limit + 1) if sieve[number]]


def legendre_symbol(value: int, prime: int) -> int:
    """Return the Legendre symbol (value/prime)."""
    if prime == 2 or not _is_prime(prime):
        raise ValueError("prime must be an odd prime")
    value %= prime
    if value == 0:
        return 0
    residue = pow(value, (prime - 1) // 2, prime)
    return 1 if residue == 1 else -1


def _pair_mul(left: Pair, right: Pair, nonsquare: int, prime: int) -> Pair:
    a, b = left
    c, d = right
    return (
        (a * c + b * d * nonsquare) % prime,
        (a * d + b * c) % prime,
    )


def _pair_inv(value: Pair, nonsquare: int, prime: int) -> Pair:
    a, b = value
    denominator = (a * a - b * b * nonsquare) % prime
    if denominator == 0:
        raise ZeroDivisionError("zero finite-field denominator")
    inverse = pow(denominator, -1, prime)
    return a * inverse % prime, -b * inverse % prime


def _pair_pow(value: Pair, exponent: int, nonsquare: int, prime: int) -> Pair:
    result = (1, 0)
    base = value

    while exponent:
        if exponent & 1:
            result = _pair_mul(result, base, nonsquare, prime)
        base = _pair_mul(base, base, nonsquare, prime)
        exponent >>= 1

    return result


def _order_in_cyclic_group(
    value: Pair,
    group_order: int,
    nonsquare: int,
    prime: int,
) -> int:
    order = group_order
    for divisor in prime_divisors(group_order):
        while order % divisor == 0:
            candidate = order // divisor
            if _pair_pow(value, candidate, nonsquare, prime) != (1, 0):
                break
            order = candidate
    return order


def cayley_order(rho: int, prime: int) -> tuple[int, int] | None:
    """Return (exact order, splitting sign) for a projective seed ratio.

    The exceptional ratios rho=0,-1 have no atom label and return None.
    """
    if prime == 2 or not _is_prime(prime):
        raise ValueError("prime must be an odd prime")

    rho %= prime
    if rho in (0, prime - 1):
        return None

    radicand = -rho % prime
    chi = legendre_symbol(radicand, prime)

    if chi == 1:
        root = next(
            value
            for value in range(1, prime)
            if value * value % prime == radicand
        )
        denominator = (1 - root) % prime
        if denominator == 0:
            return None
        zeta = ((1 + root) * pow(denominator, -1, prime) % prime, 0)
        order = _order_in_cyclic_group(zeta, prime - 1, 1, prime)
        return order, 1

    # Work in F_p[u]/(u^2-radicand), where u is the chosen square root.
    one = (1, 0)
    root_pair = (0, 1)
    numerator = (1, 1)
    denominator = (1, -1)
    zeta = _pair_mul(
        numerator,
        _pair_inv(denominator, radicand, prime),
        radicand,
        prime,
    )
    if _pair_mul(zeta, _pair_pow(zeta, prime, radicand, prime), radicand, prime) != one:
        raise AssertionError("Cayley parameter is not norm one")
    order = _order_in_cyclic_group(zeta, prime + 1, radicand, prime)
    return order, -1


def coordinate_roots(index: int, prime: int) -> set[int]:
    """Return roots of the index-m coordinate atom over F_p."""
    if index < 3:
        raise ValueError("coordinate atom index must be at least three")
    if prime == 2 or not _is_prime(prime):
        raise ValueError("prime must be an odd prime")
    if index % prime == 0:
        raise ValueError("prime must not divide the atom index")

    return {
        rho
        for rho in range(prime)
        if (label := cayley_order(rho, prime)) is not None
        and label[0] == index
    }


def universal_roots(index: int, prime: int) -> set[int]:
    """Return roots of Phi_index(alpha,beta) for the fixed Lucas pair."""
    if index < 2:
        raise ValueError("Lucas index must be at least two")
    if prime == 2 or not _is_prime(prime):
        raise ValueError("prime must be an odd prime")
    if index % prime == 0:
        raise ValueError("prime must not divide the Lucas index")

    result: set[int] = set()
    for coordinate_index in coordinate_indices(index):
        roots = coordinate_roots(coordinate_index, prime)
        if not result.isdisjoint(roots):
            raise AssertionError("distinct coordinate atoms overlap")
        result.update(roots)
    return result


def truncated_composite_mean(
    degree: int,
    levels: int,
    prime_cutoff: int,
) -> float:
    """Return the finite-prime local defect mean for arbitrary degree."""
    if degree < 2:
        raise ValueError("degree must be at least two")
    if levels < 0:
        raise ValueError("levels must be nonnegative")
    if prime_cutoff < 0:
        raise ValueError("prime cutoff must be nonnegative")

    total = 0.0
    primes = primes_upto(prime_cutoff)

    for level in range(levels):
        for index in layer_indices(degree, level):
            modulus = compatibility_modulus(index)
            weight = euler_phi(index)

            for prime in primes:
                if prime == 2 or degree % prime == 0:
                    continue
                if (prime - 1) % modulus == 0 or (prime + 1) % modulus == 0:
                    total += weight * math.log(prime) / (prime * prime - 1)

    return total


def composite_mean_bound(degree: int) -> float:
    """Return an explicit bound uniform in the levels and prime cutoff.

    The bound sums every index supported on the primes dividing degree.
    For q=compatibility_modulus(m), the two progressions p=aq+-1 give

      sum log(p)/(p^2-1)
        <= 3/q^2 * (zeta(2) log(2q) + sum log(a)/a^2).

    Since m <= q <= 2m, the remaining smooth-index sums have closed
    Euler-product evaluations.
    """
    if degree < 2:
        raise ValueError("degree must be at least two")

    support = prime_divisors(degree)
    smooth_mass = 1.0
    for prime in support:
        smooth_mass *= 1 + 1 / prime

    weighted_log_mass = smooth_mass * sum(
        prime * math.log(prime) / (prime * prime - 1)
        for prime in support
    )
    nontrivial_mass = smooth_mass - 1
    zeta_two = math.pi * math.pi / 6
    log_sum_bound = math.log(2) / 4 + (math.log(2) + 1) / 2

    return 3 * (
        zeta_two
        * (math.log(4) * nontrivial_mass + weighted_log_mass)
        + log_sum_bound * nontrivial_mass
    )

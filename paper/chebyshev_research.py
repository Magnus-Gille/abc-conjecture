#!/usr/bin/env python3
"""Phase 5 computations for local averages and all-degree transfers.

The functions in this module are exact except for the explicitly named
floating-point local mean and its elementary upper bound.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from fractions import Fraction

import chebyshev_abc as cabc


def branch_value(
    ell: int,
    level: int,
    branch: str,
    a: int,
    b: int,
    modulus: int,
) -> int:
    """Evaluate a prime-degree branch polynomial at (a:b) modulo modulus.

    The modulus must be coprime to the transfer prime because the normalized
    A branch divides its raw value by ell.
    """
    if level < 0:
        raise ValueError("level must be nonnegative")
    if branch not in ("A", "B"):
        raise ValueError("branch must be A or B")
    if modulus <= 1:
        raise ValueError("modulus must exceed one")
    if math.gcd(ell, modulus) != 1:
        raise ValueError("modulus must be coprime to ell")

    a %= modulus
    b %= modulus

    for current_level in range(level + 1):
        s_value, c_value = cabc.sc(ell, a, b, modulus)

        if current_level == level:
            if branch == "A":
                return s_value * pow(ell, -1, modulus) % modulus
            return c_value

        a, b = (
            a * s_value * s_value % modulus,
            b * c_value * c_value % modulus,
        )

    raise AssertionError("unreachable")


def seed_density_constant(ell: int) -> Fraction:
    """Return k where the admissible-box density is k / zeta(2).

    The result includes primitivity, opposite parity, and the transfer-prime
    normalization. For ell=3 the exact v_3(S_3)=1 condition removes one
    third of the otherwise eligible 3-adic classes.
    """
    if not cabc.odd_prime(ell):
        raise ValueError("ell must be an odd prime")

    coefficient = Fraction(2, 3 * (ell + 1))

    if ell == 3:
        coefficient *= Fraction(2, 3)

    return coefficient


def truncated_local_mean(
    ell: int,
    levels: int,
    prime_cutoff: int,
) -> float:
    """Return the exact-density local mean truncated at prime_cutoff.

    This is

      sum_{j<levels} phi(ell^(j+1))
        sum_{odd p<=prime_cutoff, p=+-1 mod ell^(j+1)}
          log(p)/(p^2-1).

    It is the limiting first moment of the prime-truncated log-defect over
    admissible primitive seed boxes. It is not asserted to equal the mean
    of the untruncated integer values.
    """
    if not cabc.odd_prime(ell):
        raise ValueError("ell must be an odd prime")
    if levels < 0:
        raise ValueError("levels must be nonnegative")
    if prime_cutoff < 0:
        raise ValueError("prime cutoff must be nonnegative")

    total = 0.0
    primes = cabc.primes_upto(prime_cutoff)

    for level in range(levels):
        q = ell ** (level + 1)
        phi_q = q - q // ell

        for p in primes:
            if p in (2, ell):
                continue
            if (p - 1) % q == 0 or (p + 1) % q == 0:
                total += phi_q * math.log(p) / (p * p - 1)

    return total


def local_mean_bound(ell: int) -> float:
    """Return an elementary n- and cutoff-uniform upper bound.

    For odd q, every eligible odd prime has the form 2*r*q+1 or 2*r*q-1.
    Bounding those two progressions by all positive integers gives

      (5/8q^2) [zeta(2) log(3q) + B],

    where B=sum log(r)/r^2.  The value used below bounds B by its r=2 term
    plus the decreasing integral from 2 to infinity.
    """
    if not cabc.odd_prime(ell):
        raise ValueError("ell must be an odd prime")

    zeta_two = math.pi * math.pi / 6
    log_sum_bound = (
        math.log(2) / 4
        + (math.log(2) + 1) / 2
    )

    # We use phi(ell^k) <= ell^k. Summing the two geometric series
    # gives this slightly loose but transparent closed form.
    return 5 / 8 * (
        (zeta_two * math.log(3) + log_sum_bound) / (ell - 1)
        + zeta_two
        * math.log(ell)
        * ell
        / ((ell - 1) * (ell - 1))
    )


def chebyshev_t(index: int, x: Fraction) -> Fraction:
    """Evaluate T_index(x) exactly."""
    if index < 0:
        raise ValueError("index must be nonnegative")
    if index == 0:
        return Fraction(1)
    if index == 1:
        return x

    previous = Fraction(1)
    current = x

    for _ in range(1, index):
        previous, current = current, 2 * x * current - previous

    return current


def homogeneous_chebyshev(index: int, difference: int, total: int) -> int:
    """Return total^index T_index(difference/total) by integer recurrence."""
    if index < 0:
        raise ValueError("index must be nonnegative")
    if total == 0:
        raise ValueError("total must be nonzero")
    if index == 0:
        return 1
    if index == 1:
        return difference

    previous = 1
    current = difference

    for _ in range(1, index):
        previous, current = (
            current,
            2 * difference * current - total * total * previous,
        )

    return current


def universal_transfer(degree: int, a: int, b: int) -> tuple[int, int, int]:
    """Apply the integral Chebyshev transfer of arbitrary degree >= 2."""
    if degree < 2:
        raise ValueError("degree must be at least two")
    if a <= 0 or b <= 0:
        raise ValueError("a and b must be positive")
    if math.gcd(a, b) != 1:
        raise ValueError("a and b must be coprime")
    if (a - b) % 2 == 0:
        raise ValueError("a and b must have opposite parity")

    total = a + b
    difference = b - a
    chebyshev_value = homogeneous_chebyshev(
        degree,
        difference,
        total,
    )
    total_power = total**degree
    next_a = (total_power - chebyshev_value) // 2
    next_b = (total_power + chebyshev_value) // 2

    if next_a <= 0 or next_b <= 0:
        raise AssertionError("positive seed produced a zero coordinate")
    if next_a + next_b != total_power:
        raise AssertionError("transfer identity failed")

    return next_a, next_b, total_power


def lucas_u(index: int, a: int, b: int) -> int:
    """Return U_index for roots with sum 2(b-a) and product (a+b)^2."""
    if index < 0:
        raise ValueError("index must be nonnegative")

    difference = b - a
    total = a + b
    previous = 0
    current = 1

    for _ in range(index):
        previous, current = (
            current,
            2 * difference * current - total * total * previous,
        )

    return previous


def prime_divisors(n: int) -> tuple[int, ...]:
    """Return the distinct prime divisors of n."""
    if n < 1:
        raise ValueError("n must be positive")

    result: list[int] = []
    remaining = n
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


def degree_admissibility_errors(
    degree: int,
    a: int,
    b: int,
) -> list[str]:
    """Return failed hypotheses for the all-degree normalization theorem."""
    errors: list[str] = []

    if degree < 2:
        return ["degree must be at least two"]
    if a <= 0 or b <= 0:
        errors.append("a and b must be positive")
        return errors
    if math.gcd(a, b) != 1:
        errors.append("gcd(a,b) != 1")
    if (a - b) % 2 == 0:
        errors.append("a and b must have opposite parity")

    for prime in prime_divisors(degree):
        if prime == 2:
            continue
        if a % prime:
            errors.append(f"{prime} must divide a")
            continue
        if b % prime == 0:
            errors.append(f"{prime} must not divide b")
            continue
        lucas_value = lucas_u(prime, a, b)
        if lucas_value == 0 or cabc.vp(lucas_value, prime) != 1:
            errors.append(f"v_{prime}(U_{prime}) != 1")

    return errors


def normalized_layer(
    degree: int,
    a: int,
    b: int,
    level: int,
) -> int:
    """Return |U_(d^(j+1))/U_(d^j)| / d."""
    if level < 0:
        raise ValueError("level must be nonnegative")

    errors = degree_admissibility_errors(degree, a, b)
    if errors:
        raise ValueError("; ".join(errors))

    lower = lucas_u(degree**level, a, b)
    upper = lucas_u(degree ** (level + 1), a, b)

    if lower == 0 or upper % lower:
        raise AssertionError("Lucas divisibility failed")

    quotient = upper // lower

    if quotient % degree:
        raise AssertionError("degree normalization failed")

    return abs(quotient) // degree


def divisors(n: int) -> tuple[int, ...]:
    """Return the positive divisors of n in increasing order."""
    if n < 1:
        raise ValueError("n must be positive")

    small: list[int] = []
    large: list[int] = []

    for candidate in range(1, math.isqrt(n) + 1):
        if n % candidate:
            continue
        small.append(candidate)
        partner = n // candidate
        if partner != candidate:
            large.append(partner)

    return tuple(small + list(reversed(large)))


def layer_indices(degree: int, level: int) -> tuple[int, ...]:
    """Return atom indices newly appearing from d^level to d^(level+1)."""
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


def radical(n: int) -> int:
    """Return the radical of a nonzero integer by trial division."""
    if n == 0:
        raise ValueError("radical(0) is undefined")

    remaining = abs(n)
    result = 1
    candidate = 2

    while candidate * candidate <= remaining:
        if remaining % candidate == 0:
            result *= candidate
            while remaining % candidate == 0:
                remaining //= candidate
        candidate = 3 if candidate == 2 else candidate + 2

    if remaining > 1:
        result *= remaining

    return result


@dataclass(frozen=True)
class UniversalRow:
    """One row of an arbitrary-degree Chebyshev transfer orbit."""

    n: int
    a: int
    b: int
    c: int


def universal_orbit(
    degree: int,
    a: int,
    b: int,
    steps: int,
) -> list[UniversalRow]:
    """Return rows zero through steps of the arbitrary-degree orbit."""
    if steps < 0:
        raise ValueError("steps must be nonnegative")

    errors = degree_admissibility_errors(degree, a, b)
    if errors:
        raise ValueError("; ".join(errors))

    rows: list[UniversalRow] = []

    for level in range(steps + 1):
        rows.append(UniversalRow(level, a, b, a + b))

        if level < steps:
            a, b, _ = universal_transfer(degree, a, b)

    return rows

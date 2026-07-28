#!/usr/bin/env python3
"""
chebyshev_abc.py

Research CLI for prime-degree Chebyshev abc-orbits.

Core commands:
  orbit          Generate exact orbit data.
  verify         Verify transfer, primitivity, support separation
                 and Chebyshev identities.
  square-search  Search modulo p^2 for repeated prime factors in A_n or B_n.
  local-roots    Enumerate roots of a level/branch polynomial modulo p.
  program        Construct a seed with prescribed prime birth data.
  self-test      Run regression tests.

The core uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import asdict, dataclass
from fractions import Fraction
from typing import Sequence


# ---------------------------------------------------------------------------
# Elementary arithmetic
# ---------------------------------------------------------------------------

def vp(n: int, p: int) -> int:
    """Return the p-adic valuation of a nonzero integer n."""
    if n == 0:
        raise ValueError("vp(0,p) is infinite")

    n = abs(n)
    exponent = 0

    while n % p == 0:
        n //= p
        exponent += 1

    return exponent


def odd_prime(n: int) -> bool:
    """Simple deterministic primality test for odd integers."""
    if n < 3 or n % 2 == 0:
        return False

    divisor = 3

    while divisor * divisor <= n:
        if n % divisor == 0:
            return n == divisor
        divisor += 2

    return True


def primes_upto(limit: int) -> list[int]:
    """Return all primes not exceeding limit."""
    if limit < 2:
        return []

    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"

    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (
                (limit - start) // p + 1
            )

    return [p for p, flag in enumerate(sieve) if flag]


def legendre(a: int, p: int) -> int:
    """Return the Legendre symbol (a/p), for odd prime p."""
    a %= p

    if a == 0:
        return 0

    result = pow(a, (p - 1) // 2, p)
    return -1 if result == p - 1 else result


def crt_pair(
    a1: int,
    m1: int,
    a2: int,
    m2: int,
) -> tuple[int, int]:
    """Combine two congruences with coprime moduli."""
    if math.gcd(m1, m2) != 1:
        raise ValueError("CRT moduli must be coprime")

    multiplier = ((a2 - a1) * pow(m1, -1, m2)) % m2
    modulus = m1 * m2
    residue = (a1 + m1 * multiplier) % modulus

    return residue, modulus


def crt(
    congruences: Sequence[tuple[int, int]],
) -> tuple[int, int]:
    """Combine a sequence of pairwise-coprime congruences."""
    residue = 0
    modulus = 1

    for next_residue, next_modulus in congruences:
        residue, modulus = crt_pair(
            residue,
            modulus,
            next_residue % next_modulus,
            next_modulus,
        )

    return residue, modulus


# ---------------------------------------------------------------------------
# Prime-degree transfer polynomials
# ---------------------------------------------------------------------------

def sc(
    ell: int,
    a: int,
    b: int,
    mod: int | None = None,
) -> tuple[int, int]:
    """
    Evaluate S_ell(a,b) and C_ell(a,b).

    S_ell(a,b)
      = sum_r (-1)^r binom(ell,2r+1) a^r b^(m-r)

    C_ell(a,b)
      = sum_r (-1)^r binom(ell,2r) a^r b^(m-r)

    where m=(ell-1)/2.
    """
    if not odd_prime(ell):
        raise ValueError("ell must be an odd prime")

    m = (ell - 1) // 2
    s_value = 0
    c_value = 0

    for r in range(m + 1):
        sign = -1 if r & 1 else 1

        if mod is None:
            monomial = a**r * b ** (m - r)
        else:
            monomial = (
                pow(a, r, mod)
                * pow(b, m - r, mod)
            )

        s_value += (
            sign
            * math.comb(ell, 2 * r + 1)
            * monomial
        )

        c_value += (
            sign
            * math.comb(ell, 2 * r)
            * monomial
        )

    if mod is None:
        return s_value, c_value

    return s_value % mod, c_value % mod


def admissibility_errors(
    ell: int,
    a: int,
    b: int,
) -> list[str]:
    """Return all failed seed conditions."""
    errors: list[str] = []

    if not odd_prime(ell):
        return ["ell is not an odd prime"]

    if a <= 0 or b <= 0:
        errors.append("a and b must be positive")

    if math.gcd(a, b) != 1:
        errors.append("gcd(a,b) != 1")

    if (a - b) % 2 == 0:
        errors.append("a and b must have opposite parity")

    if a % ell:
        errors.append("ell must divide a")

    if b % ell == 0:
        errors.append("ell must not divide b")

    if a > 0 and b > 0:
        s_value, _ = sc(ell, a, b)

        if s_value == 0 or vp(s_value, ell) != 1:
            errors.append("v_ell(S_ell(a,b)) != 1")

    return errors


@dataclass(frozen=True)
class Row:
    """One generation of a Chebyshev abc-orbit."""

    n: int
    a: int
    b: int
    c: int
    S: int
    C: int
    A: int
    B: int
    E: int


def orbit(
    ell: int,
    a: int,
    b: int,
    steps: int,
) -> list[Row]:
    """
    Generate rows n=0,...,steps.

    A_n = |S_n| / ell
    B_n = |C_n|
    E_n = A_n B_n
    """
    errors = admissibility_errors(ell, a, b)

    if errors:
        raise ValueError("; ".join(errors))

    rows: list[Row] = []

    for n in range(steps + 1):
        c = a + b
        s_value, c_value = sc(ell, a, b)

        if s_value % ell:
            raise AssertionError("ell does not divide S")

        A = abs(s_value) // ell
        B = abs(c_value)

        rows.append(
            Row(
                n=n,
                a=a,
                b=b,
                c=c,
                S=s_value,
                C=c_value,
                A=A,
                B=B,
                E=A * B,
            )
        )

        next_a = a * s_value * s_value
        next_b = b * c_value * c_value

        if next_a + next_b != c**ell:
            raise AssertionError(
                "prime-degree transfer identity failed"
            )

        a, b = next_a, next_b

    return rows


# ---------------------------------------------------------------------------
# Exact Chebyshev checks
# ---------------------------------------------------------------------------

def cheb_t(
    n: int,
    x: Fraction,
) -> Fraction:
    """Evaluate the Chebyshev polynomial T_n exactly."""
    if n == 0:
        return Fraction(1)

    if n == 1:
        return x

    previous = Fraction(1)
    current = x

    for _ in range(2, n + 1):
        previous, current = (
            current,
            2 * x * current - previous,
        )

    return current


def cheb_u(
    n: int,
    x: Fraction,
) -> Fraction:
    """Evaluate the Chebyshev polynomial U_n exactly."""
    if n == 0:
        return Fraction(1)

    if n == 1:
        return 2 * x

    previous = Fraction(1)
    current = 2 * x

    for _ in range(2, n + 1):
        previous, current = (
            current,
            2 * x * current - previous,
        )

    return current


def verify(
    ell: int,
    a0: int,
    b0: int,
    steps: int,
) -> dict[str, int | bool]:
    """
    Verify the finite-instance versions of the paper's structural claims.

    This checks:
      * a_n+b_n=c_n;
      * primitivity;
      * parity;
      * transfer identity;
      * exclusion of seed and existing support;
      * pairwise branch coprimality;
      * coordinate factorisation;
      * Chebyshev T and U identities.
    """
    rows = orbit(ell, a0, b0, steps)

    seen_factors: list[int] = []
    expected_a = a0
    expected_b = b0
    checks = 0

    for index, row in enumerate(rows):
        assert row.a + row.b == row.c
        assert math.gcd(row.a, row.b) == 1
        assert (row.a - row.b) % 2
        assert row.a == expected_a
        assert row.b == expected_b
        checks += 5

        assert (
            row.a * row.S**2
            + row.b * row.C**2
            == row.c**ell
        )
        checks += 1

        assert math.gcd(
            row.E,
            row.a * row.b * row.c,
        ) == 1
        checks += 1

        assert math.gcd(row.A, row.B) == 1
        checks += 1

        for old_factor in seen_factors:
            assert math.gcd(row.A, old_factor) == 1
            assert math.gcd(row.B, old_factor) == 1
            checks += 2

        seen_factors.extend((row.A, row.B))

        x = Fraction(
            row.b - row.a,
            row.c,
        )

        assert Fraction(
            row.S * row.C,
            row.c ** (ell - 1),
        ) == cheb_u(ell - 1, x)
        checks += 1

        if index + 1 < len(rows):
            next_row = rows[index + 1]

            assert Fraction(
                next_row.b - next_row.a,
                next_row.c,
            ) == cheb_t(ell, x)
            checks += 1

        expected_a *= (ell * row.A) ** 2
        expected_b *= row.B**2

    return {
        "passed": True,
        "checks": checks,
        "levels": len(rows),
    }


# ---------------------------------------------------------------------------
# Search for square prime divisors modulo p^2
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class SquareLift:
    p: int
    level: int
    branch: str


def square_lift_for_prime(
    ell: int,
    a0: int,
    b0: int,
    p: int,
    max_level: int,
) -> SquareLift | None:
    """
    Search one prime p.

    The orbit is evaluated modulo p^2, so no huge integers are produced.
    Once p divides one level factor without p^2 dividing it, the search
    stops because the support-separation theorem prevents p from
    appearing at a later generation.
    """
    if p in (2, ell):
        return None

    if (a0 * b0 * (a0 + b0)) % p == 0:
        return None

    modulus = p * p
    inverse_ell = pow(ell, -1, modulus)

    a = a0 % modulus
    b = b0 % modulus

    for level in range(max_level + 1):
        s_value, c_value = sc(
            ell,
            a,
            b,
            modulus,
        )

        A = s_value * inverse_ell % modulus
        B = c_value % modulus

        if A % p == 0:
            if A == 0:
                return SquareLift(
                    p=p,
                    level=level,
                    branch="A",
                )

            return None

        if B % p == 0:
            if B == 0:
                return SquareLift(
                    p=p,
                    level=level,
                    branch="B",
                )

            return None

        a, b = (
            a * s_value * s_value % modulus,
            b * c_value * c_value % modulus,
        )

    return None


def square_search(
    ell: int,
    a: int,
    b: int,
    prime_limit: int,
    max_level: int,
) -> dict[str, object]:
    """Search all primes p <= prime_limit."""
    errors = admissibility_errors(ell, a, b)

    if errors:
        raise ValueError("; ".join(errors))

    hits: list[SquareLift] = []
    tested = 0

    excluded = 2 * ell * a * b * (a + b)

    for p in primes_upto(prime_limit):
        if excluded % p == 0:
            continue

        tested += 1

        hit = square_lift_for_prime(
            ell,
            a,
            b,
            p,
            max_level,
        )

        if hit is not None:
            hits.append(hit)

    return {
        "tested_primes": tested,
        "square_lifts": [
            asdict(hit)
            for hit in hits
        ],
    }


# ---------------------------------------------------------------------------
# Dual-number evaluation for derivatives
# ---------------------------------------------------------------------------

def sc_dual(
    ell: int,
    a: int,
    b: int,
    da: int,
    db: int,
    mod: int,
) -> tuple[int, int, int, int]:
    """
    Return S, C, dS and dC modulo mod.

    The derivatives are with respect to the original seed variable x,
    where a=a(x) and b=b(x).
    """
    m = (ell - 1) // 2

    s_value = 0
    c_value = 0
    ds_value = 0
    dc_value = 0

    a %= mod
    b %= mod
    da %= mod
    db %= mod

    for r in range(m + 1):
        t = m - r
        sign = -1 if r & 1 else 1

        a_power = pow(a, r, mod)
        b_power = pow(b, t, mod)
        monomial = a_power * b_power % mod

        derivative = 0

        if r:
            derivative += (
                r
                * pow(a, r - 1, mod)
                * da
                * b_power
            )

        if t:
            derivative += (
                t
                * a_power
                * pow(b, t - 1, mod)
                * db
            )

        derivative %= mod

        s_coefficient = (
            sign
            * math.comb(ell, 2 * r + 1)
        )

        c_coefficient = (
            sign
            * math.comb(ell, 2 * r)
        )

        s_value += s_coefficient * monomial
        c_value += c_coefficient * monomial
        ds_value += s_coefficient * derivative
        dc_value += c_coefficient * derivative

    return (
        s_value % mod,
        c_value % mod,
        ds_value % mod,
        dc_value % mod,
    )


def branch_value_derivative(
    ell: int,
    level: int,
    branch: str,
    x: int,
    mod: int,
) -> tuple[int, int]:
    """
    Evaluate F_{level,branch}(x,1) and its derivative.

    Branch A:
        F = S_level / ell

    Branch B:
        F = C_level
    """
    if not odd_prime(ell):
        raise ValueError("ell must be an odd prime")

    if level < 0:
        raise ValueError("level must be nonnegative")

    if branch not in ("A", "B"):
        raise ValueError("branch must be A or B")

    a = x % mod
    b = 1
    da = 1
    db = 0

    for current_level in range(level + 1):
        s_value, c_value, ds_value, dc_value = sc_dual(
            ell,
            a,
            b,
            da,
            db,
            mod,
        )

        if current_level == level:
            if branch == "A":
                inverse_ell = pow(ell, -1, mod)

                return (
                    s_value * inverse_ell % mod,
                    ds_value * inverse_ell % mod,
                )

            return c_value, dc_value

        next_a = (
            a
            * s_value
            * s_value
            % mod
        )

        next_da = (
            da * s_value * s_value
            + 2 * a * s_value * ds_value
        ) % mod

        next_b = (
            b
            * c_value
            * c_value
            % mod
        )

        next_db = (
            db * c_value * c_value
            + 2 * b * c_value * dc_value
        ) % mod

        a = next_a
        b = next_b
        da = next_da
        db = next_db

    raise AssertionError("unreachable")


# ---------------------------------------------------------------------------
# Local roots and Hensel lifting
# ---------------------------------------------------------------------------

def local_roots(
    ell: int,
    p: int,
    level: int,
    branch: str,
) -> list[int]:
    """Enumerate all simple roots modulo p by direct search."""
    if not odd_prime(ell):
        raise ValueError("ell must be an odd prime")

    if not odd_prime(p) or p == ell:
        raise ValueError(
            "p must be an odd prime different from ell"
        )

    if level < 0:
        raise ValueError("level must be nonnegative")

    if branch not in ("A", "B"):
        raise ValueError("branch must be A or B")

    roots: list[int] = []

    for x in range(p):
        value, derivative = branch_value_derivative(
            ell,
            level,
            branch,
            x,
            p,
        )

        if value == 0:
            if derivative == 0:
                raise AssertionError(
                    "multiple root found"
                )

            roots.append(x)

    return roots


def hensel(
    ell: int,
    p: int,
    level: int,
    branch: str,
    root: int,
    exponent: int,
) -> int:
    """
    Lift a simple root modulo p to a root modulo p**exponent.
    """
    if exponent < 1:
        raise ValueError("exponent must be positive")

    value, derivative = branch_value_derivative(
        ell,
        level,
        branch,
        root,
        p,
    )

    if value != 0 or derivative == 0:
        raise ValueError(
            "the supplied value is not a simple root modulo p"
        )

    lifted = root % p
    modulus = p

    for _ in range(1, exponent):
        next_modulus = modulus * p

        value, derivative = branch_value_derivative(
            ell,
            level,
            branch,
            lifted,
            next_modulus,
        )

        if value % modulus:
            raise AssertionError(
                "Hensel invariant failed"
            )

        digit = (
            -(value // modulus)
            * pow(derivative % p, -1, p)
        ) % p

        lifted = (
            lifted
            + digit * modulus
        ) % next_modulus

        modulus = next_modulus

    final_value, _ = branch_value_derivative(
        ell,
        level,
        branch,
        lifted,
        modulus,
    )

    if final_value:
        raise AssertionError(
            "final Hensel lift is not a root"
        )

    return lifted


# ---------------------------------------------------------------------------
# Construct seeds with programmed prime genealogies
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Condition:
    """
    One requested prime birth condition.

    chi:
      +1 means split;
      -1 means inert.
    """

    p: int
    level: int
    branch: str
    valuation: int
    chi: int


def parse_condition(
    text: str,
) -> Condition:
    """
    Parse:

        p:level:branch:valuation:chi

    Example:

        17:1:A:2:-1
    """
    try:
        p, level, branch, valuation, chi = text.split(":")

        condition = Condition(
            p=int(p),
            level=int(level),
            branch=branch.upper(),
            valuation=int(valuation),
            chi=int(chi),
        )

    except Exception as exc:
        raise argparse.ArgumentTypeError(
            "use p:level:branch:valuation:chi"
        ) from exc

    if not odd_prime(condition.p):
        raise argparse.ArgumentTypeError(
            "p must be an odd prime"
        )

    if condition.level < 0:
        raise argparse.ArgumentTypeError(
            "level must be nonnegative"
        )

    if condition.branch not in ("A", "B"):
        raise argparse.ArgumentTypeError(
            "branch must be A or B"
        )

    if condition.valuation < 1:
        raise argparse.ArgumentTypeError(
            "valuation must be positive"
        )

    if condition.chi not in (-1, 1):
        raise argparse.ArgumentTypeError(
            "chi must be -1 or 1"
        )

    return condition


def branch_index(
    ell: int,
    level: int,
    branch: str,
) -> int:
    if not odd_prime(ell):
        raise ValueError("ell must be an odd prime")

    if level < 0:
        raise ValueError("level must be nonnegative")

    if branch not in ("A", "B"):
        raise ValueError("branch must be A or B")

    base = ell ** (level + 1)
    return base if branch == "A" else 2 * base


def program_seed(
    ell: int,
    conditions: Sequence[Condition],
) -> tuple[
    int,
    int,
    list[dict[str, int | str]],
]:
    """
    Construct an admissible seed satisfying all requested conditions.

    For every condition, the resulting prime:
      * first occurs at the requested level;
      * occurs in the requested branch;
      * has the requested exact valuation;
      * has the requested Legendre/splitting sign.
    """
    if not odd_prime(ell):
        raise ValueError("ell must be an odd prime")

    if len({condition.p for condition in conditions}) != len(
        conditions
    ):
        raise ValueError(
            "condition primes must be distinct"
        )

    a_congruences: list[tuple[int, int]] = []
    b_congruences: list[tuple[int, int]] = []
    details: list[dict[str, int | str]] = []

    for condition in conditions:
        if not odd_prime(condition.p):
            raise ValueError("condition p must be an odd prime")

        if condition.p == ell:
            raise ValueError(
                "condition prime must differ from ell"
            )

        if condition.level < 0:
            raise ValueError("condition level must be nonnegative")

        if condition.branch not in ("A", "B"):
            raise ValueError("condition branch must be A or B")

        if condition.valuation < 1:
            raise ValueError("condition valuation must be positive")

        if condition.chi not in (-1, 1):
            raise ValueError("condition chi must be -1 or 1")

        index = branch_index(
            ell,
            condition.level,
            condition.branch,
        )

        if (condition.p - condition.chi) % index:
            raise ValueError(
                f"incompatible condition: {condition}"
            )

        roots = [
            root
            for root in local_roots(
                ell,
                condition.p,
                condition.level,
                condition.branch,
            )
            if root not in (0, condition.p - 1)
            and legendre(-root, condition.p)
            == condition.chi
        ]

        if not roots:
            raise ValueError(
                f"no matching local root: {condition}"
            )

        exponent = condition.valuation + 1
        modulus = condition.p**exponent
        root = roots[0]

        lifted_root = hensel(
            ell,
            condition.p,
            condition.level,
            condition.branch,
            root,
            exponent,
        )

        # Moving p^valuation away from the lifted root gives
        # exact valuation equal to condition.valuation.
        a_residue = (
            lifted_root
            + condition.p**condition.valuation
        ) % modulus

        a_congruences.append(
            (a_residue, modulus)
        )

        b_congruences.append(
            (1, modulus)
        )

        details.append(
            {
                "p": condition.p,
                "level": condition.level,
                "branch": condition.branch,
                "valuation": condition.valuation,
                "chi": condition.chi,
                "root_mod_p": root,
                "lifted_root": lifted_root,
                "modulus": modulus,
                "a_residue": a_residue,
            }
        )

    # Opposite parity.
    a_congruences.append((0, 2))
    b_congruences.append((1, 2))

    # Transfer-prime normalisation.
    if ell == 3:
        a_congruences.append((3, 9))
        b_congruences.append((2, 9))
    else:
        a_congruences.append(
            (ell, ell * ell)
        )
        b_congruences.append(
            (1, ell * ell)
        )

    a_residue, modulus_a = crt(
        a_congruences
    )

    b_residue, modulus_b = crt(
        b_congruences
    )

    if modulus_a != modulus_b:
        raise AssertionError(
            "internal CRT moduli differ"
        )

    modulus = modulus_a

    b0 = (
        b_residue
        if b_residue > 0
        else b_residue + modulus
    )

    if math.gcd(b0, modulus) != 1:
        raise AssertionError(
            "b is not a unit modulo the CRT modulus"
        )

    # Add a == 1 mod b0 to force gcd(a0,b0)=1.
    a0, combined_modulus = crt_pair(
        a_residue,
        modulus,
        1,
        b0,
    )

    if a0 <= 0:
        a0 += combined_modulus

    errors = admissibility_errors(
        ell,
        a0,
        b0,
    )

    if errors:
        raise AssertionError(
            "; ".join(errors)
        )

    maximum_level = max(
        (
            condition.level
            for condition in conditions
        ),
        default=0,
    )

    rows = orbit(
        ell,
        a0,
        b0,
        maximum_level,
    )

    # Independent exact verification of every condition.
    for condition in conditions:
        row = rows[condition.level]

        target = (
            row.A
            if condition.branch == "A"
            else row.B
        )

        opposite = (
            row.B
            if condition.branch == "A"
            else row.A
        )

        assert vp(
            target,
            condition.p,
        ) == condition.valuation

        assert opposite % condition.p

        assert all(
            previous.E % condition.p
            for previous in rows[
                : condition.level
            ]
        )

        assert (a0 + b0) % condition.p

        assert legendre(
            -a0 * b0,
            condition.p,
        ) == condition.chi

    return a0, b0, details


# ---------------------------------------------------------------------------
# Regression tests
# ---------------------------------------------------------------------------

def self_test() -> None:
    """Run deterministic internal tests."""
    for ell in (3, 5, 7, 11):
        a = ell
        b = 2

        s_value, c_value = sc(
            ell,
            a,
            b,
        )

        assert (
            a * s_value * s_value
            + b * c_value * c_value
            == (a + b) ** ell
        )

    cubic = orbit(
        3,
        3,
        2,
        2,
    )

    assert (
        cubic[1].a,
        cubic[1].b,
        cubic[1].c,
    ) == (
        27,
        98,
        125,
    )

    assert (
        cubic[2].a,
        cubic[2].b,
        cubic[2].c,
    ) == (
        1_924_803,
        28_322,
        1_953_125,
    )

    quintic = orbit(
        5,
        5,
        2,
        1,
    )

    assert (
        quintic[1].a,
        quintic[1].b,
        quintic[1].c,
    ) == (
        15_125,
        1_682,
        16_807,
    )

    assert verify(
        3,
        3,
        2,
        3,
    )["passed"]

    assert verify(
        5,
        5,
        2,
        2,
    )["passed"]

    # Program 17 to appear in the A branch at level 1,
    # with exact valuation 2 and inert sign.
    condition = Condition(
        p=17,
        level=1,
        branch="A",
        valuation=2,
        chi=-1,
    )

    a0, b0, _ = program_seed(
        3,
        [condition],
    )

    programmed_rows = orbit(
        3,
        a0,
        b0,
        1,
    )

    assert vp(
        programmed_rows[1].A,
        17,
    ) == 2

    assert programmed_rows[0].E % 17
    assert programmed_rows[1].B % 17

    print("all self-tests passed")


# ---------------------------------------------------------------------------
# Command-line interface
# ---------------------------------------------------------------------------

def main(
    argv: Sequence[str] | None = None,
) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Research software for prime-degree "
            "Chebyshev abc-orbits."
        )
    )

    subcommands = parser.add_subparsers(
        dest="command",
        required=True,
    )

    orbit_parser = subcommands.add_parser(
        "orbit",
        help="generate an exact orbit",
    )

    orbit_parser.add_argument(
        "--ell",
        type=int,
        required=True,
    )

    orbit_parser.add_argument(
        "--a",
        type=int,
        required=True,
    )

    orbit_parser.add_argument(
        "--b",
        type=int,
        required=True,
    )

    orbit_parser.add_argument(
        "--steps",
        type=int,
        default=2,
    )

    verify_parser = subcommands.add_parser(
        "verify",
        help="verify the finite orbit identities",
    )

    verify_parser.add_argument(
        "--ell",
        type=int,
        required=True,
    )

    verify_parser.add_argument(
        "--a",
        type=int,
        required=True,
    )

    verify_parser.add_argument(
        "--b",
        type=int,
        required=True,
    )

    verify_parser.add_argument(
        "--steps",
        type=int,
        default=3,
    )

    square_parser = subcommands.add_parser(
        "square-search",
        help="search modulo p^2 for square prime divisors",
    )

    square_parser.add_argument(
        "--ell",
        type=int,
        required=True,
    )

    square_parser.add_argument(
        "--a",
        type=int,
        required=True,
    )

    square_parser.add_argument(
        "--b",
        type=int,
        required=True,
    )

    square_parser.add_argument(
        "--prime-limit",
        type=int,
        required=True,
    )

    square_parser.add_argument(
        "--max-level",
        type=int,
        default=20,
    )

    roots_parser = subcommands.add_parser(
        "local-roots",
        help="enumerate local branch roots modulo p",
    )

    roots_parser.add_argument(
        "--ell",
        type=int,
        required=True,
    )

    roots_parser.add_argument(
        "--p",
        type=int,
        required=True,
    )

    roots_parser.add_argument(
        "--level",
        type=int,
        required=True,
    )

    roots_parser.add_argument(
        "--branch",
        choices=("A", "B"),
        required=True,
    )

    program_parser = subcommands.add_parser(
        "program",
        help="construct a programmed seed",
    )

    program_parser.add_argument(
        "--ell",
        type=int,
        required=True,
    )

    program_parser.add_argument(
        "--condition",
        type=parse_condition,
        action="append",
        required=True,
        help=(
            "p:level:branch:valuation:chi; "
            "repeat for multiple conditions"
        ),
    )

    subcommands.add_parser(
        "self-test",
        help="run deterministic regression tests",
    )

    args = parser.parse_args(argv)

    try:
        if args.command == "orbit":
            rows = orbit(
                args.ell,
                args.a,
                args.b,
                args.steps,
            )

            print(
                json.dumps(
                    [
                        asdict(row)
                        for row in rows
                    ],
                    indent=2,
                )
            )

        elif args.command == "verify":
            print(
                json.dumps(
                    verify(
                        args.ell,
                        args.a,
                        args.b,
                        args.steps,
                    ),
                    indent=2,
                )
            )

        elif args.command == "square-search":
            print(
                json.dumps(
                    square_search(
                        args.ell,
                        args.a,
                        args.b,
                        args.prime_limit,
                        args.max_level,
                    ),
                    indent=2,
                )
            )

        elif args.command == "local-roots":
            roots = local_roots(
                args.ell,
                args.p,
                args.level,
                args.branch,
            )

            output = []

            for root in roots:
                _, derivative = branch_value_derivative(
                    args.ell,
                    args.level,
                    args.branch,
                    root,
                    args.p,
                )

                output.append(
                    {
                        "root": root,
                        "chi": legendre(
                            -root,
                            args.p,
                        ),
                        "derivative_mod_p": derivative,
                    }
                )

            print(
                json.dumps(
                    output,
                    indent=2,
                )
            )

        elif args.command == "program":
            a0, b0, details = program_seed(
                args.ell,
                args.condition,
            )

            print(
                json.dumps(
                    {
                        "ell": args.ell,
                        "a0": a0,
                        "b0": b0,
                        "c0": a0 + b0,
                        "conditions": details,
                    },
                    indent=2,
                )
            )

        else:
            self_test()

    except (
        ValueError,
        AssertionError,
    ) as exc:
        print(
            f"error: {exc}",
            file=sys.stderr,
        )

        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

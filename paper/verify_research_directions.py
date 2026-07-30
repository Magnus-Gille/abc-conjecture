#!/usr/bin/env python3
"""Deterministic verification for the Phase 5 research directions."""

from __future__ import annotations

import json
import math
from fractions import Fraction

import chebyshev_abc as cabc
import chebyshev_research as research


COMPOSITE_CASES = (
    (6, 3, 2),
    (9, 9, 2),
    (10, 5, 2),
    (12, 3, 2),
    (15, 15, 4),
    (30, 15, 4),
)


def verify_density() -> dict[str, int | str]:
    """Count one primitive projective density exactly modulo p^2."""
    ell = 3
    level = 0
    branch = "A"
    p = 7
    exponent = 2
    modulus = p**exponent
    divisible = 0
    primitive = 0

    for a in range(modulus):
        for b in range(modulus):
            if a % p == 0 and b % p == 0:
                continue
            primitive += 1
            if (
                research.branch_value(
                    ell,
                    level,
                    branch,
                    a,
                    b,
                    modulus,
                )
                == 0
            ):
                divisible += 1

    observed = Fraction(divisible, primitive)
    predicted = Fraction(1, p ** (exponent - 1) * (p + 1))
    assert observed == predicted

    return {
        "ell": ell,
        "level": level,
        "branch": branch,
        "p": p,
        "exponent": exponent,
        "primitive_pairs": primitive,
        "divisible_pairs": divisible,
        "density": str(observed),
    }


def verify_local_means() -> list[dict[str, int | float]]:
    """Check the explicit uniform bound for several transfer primes."""
    rows: list[dict[str, int | float]] = []

    for ell in (3, 5, 7, 11):
        value = research.truncated_local_mean(ell, 8, 20_000)
        bound = research.local_mean_bound(ell)
        assert value <= bound
        rows.append(
            {
                "ell": ell,
                "levels": 8,
                "prime_cutoff": 20_000,
                "local_mean": round(value, 12),
                "elementary_bound": round(bound, 12),
            }
        )

    return rows


def verify_composite_layers() -> list[dict[str, object]]:
    """Check normalization and support separation in composite examples."""
    rows: list[dict[str, object]] = []

    for degree, a, b in COMPOSITE_CASES:
        assert research.degree_admissibility_errors(degree, a, b) == []
        layers = [
            research.normalized_layer(degree, a, b, level)
            for level in range(2)
        ]
        seed_support = degree * a * b * (a + b)
        assert all(math.gcd(layer, seed_support) == 1 for layer in layers)
        assert math.gcd(layers[0], layers[1]) == 1
        rows.append(
            {
                "degree": degree,
                "seed": [a, b, a + b],
                "layer_digits": [len(str(layer)) for layer in layers],
                "seed_gcds": [
                    math.gcd(layer, seed_support)
                    for layer in layers
                ],
                "cross_layer_gcd": math.gcd(layers[0], layers[1]),
            }
        )

    assert research.degree_admissibility_errors(15, 15, 2)
    return rows


def verify_specializations() -> dict[str, object]:
    """Check exact recovery of the quadratic and odd-prime transfers."""
    quadratic = research.universal_transfer(2, 1, 8)
    assert quadratic == (32, 49, 81)

    prime_rows: list[dict[str, object]] = []

    for ell, a, b in ((3, 3, 2), (5, 5, 2), (7, 7, 2)):
        s_value, c_value = cabc.sc(ell, a, b)
        expected = (
            a * s_value * s_value,
            b * c_value * c_value,
            (a + b) ** ell,
        )
        actual = research.universal_transfer(ell, a, b)
        assert actual == expected
        prime_rows.append(
            {
                "degree": ell,
                "seed": [a, b, a + b],
                "transfer": list(actual),
            }
        )

    return {
        "quadratic": list(quadratic),
        "odd_prime_cases": prime_rows,
    }


def main() -> int:
    result = {
        "passed": True,
        "primitive_density": verify_density(),
        "local_means": verify_local_means(),
        "composite_layers": verify_composite_layers(),
        "specializations": verify_specializations(),
        "bad_three_adic_seed_rejected": [15, 15, 2],
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

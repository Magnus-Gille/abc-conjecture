#!/usr/bin/env python3
"""Bounded factorization probe for the canonical fixed Chebyshev orbits.

This is diagnostic code, not an input to any theorem.  SymPy's factorint
is deliberately given a finite trial/ECM limit.  A returned composite
cofactor is recorded as unresolved, and no squarefreeness conclusion is
drawn from it.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Mapping, Sequence

try:
    from sympy import factorint, isprime
except ImportError as exc:  # pragma: no cover - environment diagnostic
    raise SystemExit(
        "fixed_orbit_probe.py requires the optional SymPy package"
    ) from exc


REPO_ROOT = Path(__file__).resolve().parents[2]
PAPER_DIR = REPO_ROOT / "paper"

if str(PAPER_DIR) not in sys.path:
    sys.path.insert(0, str(PAPER_DIR))

import chebyshev_abc as cabc  # noqa: E402
import chebyshev_research as research  # noqa: E402


# Factors found during the bounded Phase 6 computation.  Keeping them here
# turns the expensive discovery step into a cheap, deterministic certificate:
# audit_factorization checks both primality and exact multiplication afresh.
KNOWN_FACTORIZATIONS: dict[tuple[str, int], dict[int, int]] = {
    ("quadratic", 0): {7: 1},
    ("quadratic", 1): {17: 1},
    ("quadratic", 2): {31: 1, 193: 1},
    ("quadratic", 3): {2_753: 1, 10_369: 1},
    ("quadratic", 4): {127: 1, 19_841: 1, 88_613_249: 1},
    ("quadratic", 5): {
        257: 1,
        25_221_377: 1,
        29_675_263: 1,
        17_332_651_258_369: 1,
    },
    ("quadratic", 6): {
        6_143: 1,
        2_030_591: 1,
        419_726_966_783: 1,
        5_391_849_492_481: 1,
        369_840_101_107_459_107_383_427_583: 1,
    },
    ("cubic", 0): {7: 1},
    ("cubic", 1): {17: 1, 89: 1},
    ("cubic", 2): {613_279: 1, 5_746_087: 1},
    ("cubic", 3): {
        9_719: 1,
        11_177: 1,
        9_855_271: 1,
        12_911_399: 1,
        1_665_138_539_814_839: 1,
    },
    ("quintic", 0): {11: 1, 29: 1},
    ("quintic", 1): {199: 1, 11_549: 1, 892_254_749: 1},
}


@dataclass(frozen=True)
class LayerValue:
    """One exact integer layer in a named canonical orbit."""

    orbit: str
    degree: int
    level: int
    value: int

    @property
    def order_modulus(self) -> int:
        """Return the modulus in the forced p = +/-1 congruence."""
        if self.orbit == "quadratic":
            # The quadratic layer is the signed atom of order 2^(j+2).
            return 2 ** (self.level + 2)

        # For the odd-prime E_j product, the common consequence of the
        # two branch orders ell^(j+1) and 2*ell^(j+1) is modulo ell^(j+1).
        return self.degree ** (self.level + 1)

    def prime_has_forced_congruence(self, prime: int) -> bool:
        """Check the theorem's necessary p = +/-1 mod order condition."""
        residue = prime % self.order_modulus
        return residue in (1, self.order_modulus - 1)


@dataclass(frozen=True)
class FactorizationAudit:
    """Metrics extracted only from a certified complete factorization."""

    log_defect: float
    excess_exponent: int
    largest_squared_prime: int | None


@dataclass(frozen=True)
class FactorComponent:
    """One prime or unresolved-composite component from bounded factoring."""

    value: str
    exponent: int
    status: str


def audit_factorization(
    value: int,
    factors: Mapping[int, int],
) -> FactorizationAudit:
    """Validate a complete prime factorization and compute its defect."""
    if value < 1:
        raise ValueError("value must be positive")

    product = 1
    log_defect = 0.0
    excess_exponent = 0
    largest_squared_prime: int | None = None

    for prime, exponent in factors.items():
        if prime < 2 or not bool(isprime(prime)):
            raise ValueError(f"{prime} is not a certified prime factor")
        if exponent < 1:
            raise ValueError("factor exponents must be positive")

        product *= prime**exponent

        if exponent >= 2:
            log_defect += (exponent - 1) * math.log(prime)
            excess_exponent += exponent - 1
            if largest_squared_prime is None or prime > largest_squared_prime:
                largest_squared_prime = prime

    if product != value:
        raise ValueError("factorization does not multiply to the input value")

    return FactorizationAudit(
        log_defect=log_defect,
        excess_exponent=excess_exponent,
        largest_squared_prime=largest_squared_prime,
    )


def canonical_layers(
    quadratic_levels: int,
    cubic_levels: int,
    quintic_levels: int,
) -> list[LayerValue]:
    """Generate exact layers for the three canonical fixed orbits."""
    counts = (quadratic_levels, cubic_levels, quintic_levels)
    if any(count < 0 for count in counts):
        raise ValueError("level counts must be nonnegative")

    layers = [
        LayerValue(
            orbit="quadratic",
            degree=2,
            level=level,
            value=research.normalized_layer(2, 1, 8, level),
        )
        for level in range(quadratic_levels)
    ]

    if cubic_levels:
        rows = cabc.orbit(3, 3, 2, cubic_levels - 1)
        layers.extend(
            LayerValue("cubic", 3, row.n, row.E)
            for row in rows
        )

    if quintic_levels:
        rows = cabc.orbit(5, 5, 2, quintic_levels - 1)
        layers.extend(
            LayerValue("quintic", 5, row.n, row.E)
            for row in rows
        )

    return layers


def bounded_factorization(
    value: int,
    limit: int,
) -> tuple[dict[int, int], bool]:
    """Factor with a finite effort bound and mark unresolved cofactors."""
    if value < 1:
        raise ValueError("value must be positive")
    if limit < 2:
        raise ValueError("factor limit must be at least two")

    factors = {
        int(component): int(exponent)
        for component, exponent in factorint(value, limit=limit).items()
    }
    product = math.prod(
        component**exponent
        for component, exponent in factors.items()
    )

    if product != value:
        raise AssertionError("bounded factorization lost a component")

    complete = all(bool(isprime(component)) for component in factors)
    return factors, complete


def analyze_layer(
    layer: LayerValue,
    factor_limit: int,
) -> dict[str, object]:
    """Return a JSON-safe, conservatively labeled layer report."""
    stored_factors = KNOWN_FACTORIZATIONS.get((layer.orbit, layer.level))

    if stored_factors is not None:
        audit_factorization(layer.value, stored_factors)
        factors = dict(stored_factors)
        complete = True
        factorization_method = "stored-certificate"
    else:
        factors, complete = bounded_factorization(layer.value, factor_limit)
        factorization_method = "bounded-search"

    components = [
        FactorComponent(
            value=str(component),
            exponent=exponent,
            status="prime" if bool(isprime(component)) else "unresolved-composite",
        )
        for component, exponent in sorted(factors.items())
    ]
    certified_primes = [
        component
        for component in factors
        if bool(isprime(component))
    ]

    report: dict[str, object] = {
        "orbit": layer.orbit,
        "degree": layer.degree,
        "level": layer.level,
        "value_digits": len(str(layer.value)),
        "order_modulus": layer.order_modulus,
        "factorization_complete": complete,
        "factorization_method": factorization_method,
        "components": [asdict(component) for component in components],
        "certified_primes_obey_congruence": all(
            layer.prime_has_forced_congruence(prime)
            for prime in certified_primes
        ),
    }

    if complete:
        audit = audit_factorization(layer.value, factors)
        report.update(
            {
                "log_defect": audit.log_defect,
                "normalized_log_defect": (
                    audit.log_defect / layer.degree**layer.level
                ),
                "excess_exponent": audit.excess_exponent,
                "largest_squared_prime": audit.largest_squared_prime,
                "squarefree": audit.excess_exponent == 0,
            }
        )
    else:
        report.update(
            {
                "log_defect": None,
                "normalized_log_defect": None,
                "excess_exponent": None,
                "largest_squared_prime": None,
                "squarefree": None,
            }
        )

    return report


def build_report(
    quadratic_levels: int = 8,
    cubic_levels: int = 5,
    quintic_levels: int = 3,
    factor_limit: int = 100_000,
) -> dict[str, object]:
    """Build the complete bounded diagnostic report."""
    layers = canonical_layers(
        quadratic_levels,
        cubic_levels,
        quintic_levels,
    )

    return {
        "scope": {
            "quadratic_seed": [1, 8, 9],
            "cubic_seed": [3, 2, 5],
            "quintic_seed": [5, 2, 7],
            "factor_limit": factor_limit,
            "warning": (
                "A composite residual makes the layer unresolved; "
                "this report supplies no asymptotic evidence."
            ),
        },
        "layers": [
            analyze_layer(layer, factor_limit)
            for layer in layers
        ],
    }


def parse_args(
    argv: Sequence[str] | None = None,
) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--quadratic-levels", type=int, default=8)
    parser.add_argument("--cubic-levels", type=int, default=5)
    parser.add_argument("--quintic-levels", type=int, default=3)
    parser.add_argument("--factor-limit", type=int, default=100_000)
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    report = build_report(
        quadratic_levels=args.quadratic_levels,
        cubic_levels=args.cubic_levels,
        quintic_levels=args.quintic_levels,
        factor_limit=args.factor_limit,
    )
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

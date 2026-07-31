#!/usr/bin/env python3
"""Generate and verify replayable Pocklington primality certificates.

Verification uses only Python's standard library.  SymPy is imported solely
by the optional ``--generate`` path that discovers complete factorizations of
``n - 1`` and suitable witnesses; it is not part of the proof replay.
"""

from __future__ import annotations

import argparse
import json
import math
from collections.abc import Mapping


LEVEL_SEVEN = int(
    "7899993675270888986790467637030360278248237512403075459722095"
    "7868119418164413649973647970771585795292694673449586011206657"
)

LEVEL_SEVEN_FACTORS = (
    189_439,
    750_692_351,
    9_825_841_153,
    298_196_593_663,
    991_245_449_894_911,
    6_726_631_000_961_507_661_177_857,
    28_434_404_151_626_641_091_139_435_909_034_910_237_447_173_121,
)


def _as_positive_int(value: object, label: str) -> int:
    """Parse a decimal JSON value without accepting booleans or signs."""
    if isinstance(value, bool):
        raise ValueError(f"{label} must be a positive integer")
    if isinstance(value, int):
        number = value
    elif isinstance(value, str) and value.isdecimal():
        number = int(value)
    else:
        raise ValueError(f"{label} must be a positive decimal integer")
    if number < 1:
        raise ValueError(f"{label} must be positive")
    return number


def verify_bundle(bundle: Mapping[str, object]) -> bool:
    """Verify exact factor multiplication and every Pocklington node.

    Each non-base node contains the complete prime factorization of ``n-1``.
    For every distinct prime divisor ``q`` it also contains a witness ``a``
    satisfying

        a**(n-1) == 1 (mod n),
        gcd(a**((n-1)/q) - 1, n) == 1.

    Pocklington's theorem then proves ``n`` prime.  Recursive nodes certify
    the prime divisors of ``n-1``; the recursion bottoms out at 2.
    """
    if not isinstance(bundle, Mapping):
        raise ValueError("certificate bundle must be a mapping")

    layer = _as_positive_int(bundle.get("layer"), "layer")
    raw_roots = bundle.get("roots")
    raw_certificates = bundle.get("certificates")
    if not isinstance(raw_roots, list) or not raw_roots:
        raise ValueError("roots must be a nonempty list")
    if not isinstance(raw_certificates, Mapping):
        raise ValueError("certificates must be a mapping")

    roots = [_as_positive_int(value, "root") for value in raw_roots]
    if len(roots) != len(set(roots)):
        raise ValueError("root factors must be distinct")
    if math.prod(roots) != layer:
        raise ValueError("root factors do not multiply to the layer")

    verified: set[int] = {2}
    visiting: set[int] = set()

    def verify_prime(number: int) -> None:
        if number in verified:
            return
        if number in visiting:
            raise ValueError("certificate graph contains a cycle")
        if number < 3 or number % 2 == 0:
            raise ValueError(f"unsupported non-base candidate {number}")

        raw_node = raw_certificates.get(str(number))
        if not isinstance(raw_node, Mapping):
            raise ValueError(f"missing certificate node for {number}")
        raw_factors = raw_node.get("factors")
        raw_witnesses = raw_node.get("witnesses")
        if not isinstance(raw_factors, Mapping) or not raw_factors:
            raise ValueError(f"missing n-1 factorization for {number}")
        if not isinstance(raw_witnesses, Mapping):
            raise ValueError(f"missing witnesses for {number}")

        factors: dict[int, int] = {}
        product = 1
        for raw_q, raw_exponent in raw_factors.items():
            q = _as_positive_int(raw_q, "factor")
            exponent = _as_positive_int(raw_exponent, "exponent")
            if q in factors:
                raise ValueError(f"duplicate n-1 factor {q}")
            factors[q] = exponent
            product *= q**exponent
        if product != number - 1:
            raise ValueError(f"n-1 factors are inexact for {number}")

        visiting.add(number)
        for q in factors:
            verify_prime(q)

        for q in factors:
            witness = _as_positive_int(
                raw_witnesses.get(str(q)),
                f"witness for {number}, q={q}",
            )
            if not 1 < witness < number:
                raise ValueError(f"witness out of range for {number}, q={q}")
            if pow(witness, number - 1, number) != 1:
                raise ValueError(f"Fermat condition fails for {number}, q={q}")
            residue = pow(witness, (number - 1) // q, number)
            if math.gcd(residue - 1, number) != 1:
                raise ValueError(
                    f"Pocklington gcd condition fails for {number}, q={q}"
                )

        visiting.remove(number)
        verified.add(number)

    for root in roots:
        verify_prime(root)
    return True


def generate_bundle() -> dict[str, object]:
    """Discover the static certificate bundle (requires SymPy)."""
    try:
        import sympy
        from sympy import factorint, isprime
    except ImportError as exc:  # pragma: no cover - generation-only path
        raise SystemExit("certificate generation requires SymPy") from exc

    certificates: dict[str, object] = {}

    def generate_prime(number: int) -> None:
        if number == 2 or str(number) in certificates:
            return
        if not bool(isprime(number)):
            raise ValueError(f"generation candidate is composite: {number}")
        factors = {
            int(q): int(exponent)
            for q, exponent in factorint(number - 1).items()
        }
        if math.prod(q**exponent for q, exponent in factors.items()) != number - 1:
            raise ValueError(f"incomplete n-1 factorization for {number}")
        for q in factors:
            if not bool(isprime(q)):
                raise ValueError(f"composite n-1 component {q}")
            generate_prime(q)

        witnesses: dict[str, int] = {}
        for q in sorted(factors):
            for witness in range(2, number):
                if (
                    pow(witness, number - 1, number) == 1
                    and math.gcd(
                        pow(witness, (number - 1) // q, number) - 1,
                        number,
                    )
                    == 1
                ):
                    witnesses[str(q)] = witness
                    break
            else:  # pragma: no cover - impossible for a prime candidate
                raise ValueError(f"no witness found for {number}, q={q}")

        certificates[str(number)] = {
            "factors": {
                str(q): exponent for q, exponent in sorted(factors.items())
            },
            "witnesses": witnesses,
        }

    for root in LEVEL_SEVEN_FACTORS:
        generate_prime(root)

    bundle: dict[str, object] = {
        "method": "Pocklington with complete recursive factorizations of n-1",
        "generator": f"SymPy {sympy.__version__}",
        "layer": str(LEVEL_SEVEN),
        "roots": [str(root) for root in LEVEL_SEVEN_FACTORS],
        "certificates": dict(
            sorted(certificates.items(), key=lambda item: int(item[0]))
        ),
    }
    verify_bundle(bundle)
    return bundle


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate or verify the quadratic level-seven certificate"
    )
    parser.add_argument("--generate", action="store_true")
    parser.add_argument("certificate", nargs="?")
    args = parser.parse_args()

    if args.generate:
        print(json.dumps(generate_bundle(), indent=2, sort_keys=False))
        return
    if not args.certificate:
        parser.error("provide a certificate path or use --generate")
    with open(args.certificate, encoding="utf-8") as handle:
        bundle = json.load(handle)
    verify_bundle(bundle)
    print("certificate verified")


if __name__ == "__main__":
    main()

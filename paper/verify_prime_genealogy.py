#!/usr/bin/env python3
"""Deterministic verification harness for the prime-genealogy proposal."""

from __future__ import annotations

import json

import chebyshev_abc as cabc


ORBIT_TARGETS = {
    3: 40,
    5: 40,
    7: 40,
    11: 40,
    13: 40,
    17: 40,
    19: 38,
}

# Four degree-21 cases, two degree-10 cases, and two degree-3 cases
# contribute 110 roots. Four incompatible cases contribute none.
LOCAL_CASES = (
    (7, 197, 1, "A", 1, 21),
    (7, 197, 1, "B", 1, 21),
    (7, 97, 1, "A", -1, 21),
    (7, 97, 1, "B", -1, 21),
    (5, 101, 1, "A", 1, 10),
    (5, 149, 1, "B", -1, 10),
    (3, 19, 1, "A", 1, 3),
    (3, 17, 1, "B", -1, 3),
    (7, 101, 1, "A", None, 0),
    (5, 29, 1, "B", None, 0),
    (3, 13, 1, "B", None, 0),
    (11, 7, 0, "A", None, 0),
)


def first_admissible_seeds(
    ell: int,
    count: int,
) -> list[tuple[int, int]]:
    """Return a deterministic prefix of small admissible seeds."""
    seeds: list[tuple[int, int]] = []

    for multiplier in range(1, 200):
        a = ell * multiplier

        for b in range(1, 300):
            if not cabc.admissibility_errors(ell, a, b):
                seeds.append((a, b))

                if len(seeds) == count:
                    return seeds

    raise AssertionError(
        f"only found {len(seeds)} admissible seeds for ell={ell}"
    )


def verify_orbits() -> tuple[int, int]:
    """Verify exact orbit identities and support separation."""
    orbit_count = 0
    assertion_count = 0

    for ell, target in ORBIT_TARGETS.items():
        for a, b in first_admissible_seeds(ell, target):
            result = cabc.verify(ell, a, b, 2)
            assert result["passed"]
            orbit_count += 1
            assertion_count += int(result["checks"])

    return orbit_count, assertion_count


def verify_local_cases() -> tuple[int, int]:
    """Verify root counts, signs, simplicity, and Hensel lifts."""
    root_count = 0
    lift_count = 0

    for ell, p, level, branch, chi, expected_count in LOCAL_CASES:
        roots = cabc.local_roots(ell, p, level, branch)
        assert len(roots) == expected_count

        for root in roots:
            assert chi is not None
            assert cabc.legendre(-root, p) == chi

            _, derivative = cabc.branch_value_derivative(
                ell,
                level,
                branch,
                root,
                p,
            )
            assert derivative % p

            lifted = cabc.hensel(
                ell,
                p,
                level,
                branch,
                root,
                3,
            )
            value, _ = cabc.branch_value_derivative(
                ell,
                level,
                branch,
                lifted,
                p**3,
            )
            assert value == 0

            root_count += 1
            lift_count += 1

    return root_count, lift_count


def verify_programmed_example() -> dict[str, int | str]:
    """Reproduce the proposed 17^2 inert A-branch example."""
    condition = cabc.Condition(
        p=17,
        level=1,
        branch="A",
        valuation=2,
        chi=-1,
    )
    a0, b0, _ = cabc.program_seed(3, (condition,))
    rows = cabc.orbit(3, a0, b0, 1)

    assert (a0, b0) == (304_260_006, 39_305)
    assert rows[0].E % 17
    assert cabc.vp(rows[1].A, 17) == 2
    assert rows[1].B % 17
    assert cabc.legendre(-a0 * b0, 17) == -1

    return {
        "ell": 3,
        "a0": a0,
        "b0": b0,
        "p": 17,
        "level": 1,
        "branch": "A",
        "valuation": 2,
        "chi": -1,
    }


def verify_canonical_orbits() -> None:
    """Reproduce the cubic and quintic examples in the manuscript."""
    cubic = cabc.orbit(3, 3, 2, 2)
    assert (
        cubic[2].a,
        cubic[2].b,
        cubic[2].c,
    ) == (
        1_924_803,
        28_322,
        1_953_125,
    )

    quintic = cabc.orbit(5, 5, 2, 2)
    assert (
        quintic[2].a,
        quintic[2].b,
        quintic[2].c,
    ) == (
        1_997_240_239_809_753_125,
        1_339_071_379_424_155_147_682,
        1_341_068_619_663_964_900_807,
    )


def main() -> int:
    orbit_count, orbit_assertions = verify_orbits()
    root_count, lift_count = verify_local_cases()
    programmed = verify_programmed_example()
    verify_canonical_orbits()

    print(
        json.dumps(
            {
                "passed": True,
                "orbit_count": orbit_count,
                "orbit_assertions": orbit_assertions,
                "transfer_primes": list(ORBIT_TARGETS),
                "local_case_count": len(LOCAL_CASES),
                "local_root_count": root_count,
                "hensel_lift_count": lift_count,
                "programmed_example": programmed,
                "canonical_orbits": ["cubic", "quintic"],
            },
            indent=2,
        )
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Independent regression tests for the proposed prime-genealogy CLI."""

from __future__ import annotations

import math
import unittest

import chebyshev_abc as cabc


def branch_value(
    ell: int,
    level: int,
    branch: str,
    a: int,
    b: int,
    modulus: int,
) -> int:
    """Evaluate a branch polynomial at an arbitrary projective point."""
    a %= modulus
    b %= modulus

    for current_level in range(level + 1):
        s_value, c_value = cabc.sc(ell, a, b, modulus)

        if current_level == level:
            if branch == "A":
                return s_value * pow(ell, -1, modulus) % modulus
            if branch == "B":
                return c_value
            raise ValueError("branch must be A or B")

        a, b = (
            a * s_value * s_value % modulus,
            b * c_value * c_value % modulus,
        )

    raise AssertionError("unreachable")


class LocalClassificationTests(unittest.TestCase):
    def test_small_prime_root_counts_and_signs(self) -> None:
        for ell in (3, 5, 7):
            for level in (0, 1):
                degree = ell**level * (ell - 1) // 2

                for branch in ("A", "B"):
                    index = cabc.branch_index(ell, level, branch)

                    for p in cabc.primes_upto(199):
                        if p in (2, ell):
                            continue

                        compatible_signs = [
                            chi
                            for chi in (1, -1)
                            if (p - chi) % index == 0
                        ]
                        roots = cabc.local_roots(
                            ell,
                            p,
                            level,
                            branch,
                        )

                        expected_count = degree if compatible_signs else 0
                        self.assertEqual(
                            len(roots),
                            expected_count,
                            (ell, level, branch, p),
                        )

                        if compatible_signs:
                            self.assertEqual(len(compatible_signs), 1)
                            chi = compatible_signs[0]
                            self.assertTrue(
                                all(
                                    cabc.legendre(-root, p) == chi
                                    for root in roots
                                )
                            )
                            self.assertTrue(
                                all(root not in (0, p - 1) for root in roots)
                            )

    def test_hensel_distance_has_exact_valuation(self) -> None:
        cases = (
            (3, 7, 0, "A"),
            (3, 7, 0, "B"),
            (3, 17, 1, "A"),
            (3, 37, 1, "B"),
            (5, 11, 0, "A"),
            (5, 11, 0, "B"),
        )

        for ell, p, level, branch in cases:
            root = cabc.local_roots(ell, p, level, branch)[0]

            for h in (1, 2, 3):
                modulus = p ** (h + 1)
                lifted = cabc.hensel(
                    ell,
                    p,
                    level,
                    branch,
                    root,
                    h + 1,
                )

                for unit in (1, 2, p - 1):
                    if unit % p == 0:
                        continue

                    value, _ = cabc.branch_value_derivative(
                        ell,
                        level,
                        branch,
                        lifted + unit * p**h,
                        modulus,
                    )
                    self.assertEqual(
                        cabc.vp(value, p),
                        h,
                        (ell, p, level, branch, h, unit),
                    )

    def test_homogeneous_specialization_used_by_crt(self) -> None:
        cases = (
            (3, 17, 1, "A", 2),
            (3, 37, 1, "B", 2),
            (5, 11, 0, "A", 3),
            (5, 11, 0, "B", 3),
        )

        for ell, p, level, branch, exponent in cases:
            modulus = p**exponent
            degree = ell**level * (ell - 1) // 2

            for a, b in ((2, 3), (7, 5), (p + 4, 1 + p)):
                if math.gcd(b, p) != 1:
                    continue

                ratio = a * pow(b, -1, modulus) % modulus
                specialized, _ = cabc.branch_value_derivative(
                    ell,
                    level,
                    branch,
                    ratio,
                    modulus,
                )
                expected = pow(b, degree, modulus) * specialized % modulus

                self.assertEqual(
                    branch_value(
                        ell,
                        level,
                        branch,
                        a,
                        b,
                        modulus,
                    ),
                    expected,
                )


class RealizationTests(unittest.TestCase):
    def test_multiple_conditions_are_realized_simultaneously(self) -> None:
        conditions = (
            cabc.Condition(7, 0, "B", 1, 1),
            cabc.Condition(17, 1, "A", 2, -1),
            cabc.Condition(37, 1, "B", 3, 1),
        )

        a0, b0, _ = cabc.program_seed(3, conditions)
        self.assertEqual(cabc.admissibility_errors(3, a0, b0), [])

        rows = cabc.orbit(3, a0, b0, 1)

        for condition in conditions:
            target = (
                rows[condition.level].A
                if condition.branch == "A"
                else rows[condition.level].B
            )
            opposite = (
                rows[condition.level].B
                if condition.branch == "A"
                else rows[condition.level].A
            )

            self.assertEqual(
                cabc.vp(target, condition.p),
                condition.valuation,
            )
            self.assertNotEqual(opposite % condition.p, 0)
            self.assertTrue(
                all(
                    row.E % condition.p
                    for row in rows[: condition.level]
                )
            )
            self.assertNotEqual(
                a0 * b0 * (a0 + b0) % condition.p,
                0,
            )
            self.assertEqual(
                cabc.legendre(-a0 * b0, condition.p),
                condition.chi,
            )

    def test_incompatible_condition_is_rejected(self) -> None:
        condition = cabc.Condition(5, 1, "A", 1, 1)

        with self.assertRaisesRegex(ValueError, "incompatible condition"):
            cabc.program_seed(3, (condition,))

    def test_realization_uses_the_ell_at_least_five_normalization(self) -> None:
        conditions = (
            cabc.Condition(11, 0, "A", 1, 1),
            cabc.Condition(19, 0, "B", 2, -1),
        )

        a0, b0, _ = cabc.program_seed(5, conditions)
        self.assertEqual(cabc.admissibility_errors(5, a0, b0), [])

        row = cabc.orbit(5, a0, b0, 0)[0]
        self.assertEqual(cabc.vp(row.A, 11), 1)
        self.assertEqual(cabc.vp(row.B, 19), 2)
        self.assertNotEqual(a0 * b0 * (a0 + b0) % 11, 0)
        self.assertNotEqual(a0 * b0 * (a0 + b0) % 19, 0)
        self.assertEqual(cabc.legendre(-a0 * b0, 11), 1)
        self.assertEqual(cabc.legendre(-a0 * b0, 19), -1)

    def test_programmed_example_is_reproduced_exactly(self) -> None:
        condition = cabc.Condition(17, 1, "A", 2, -1)
        a0, b0, _ = cabc.program_seed(3, (condition,))

        self.assertEqual((a0, b0), (304_260_006, 39_305))


class InputValidationTests(unittest.TestCase):
    def test_branch_index_rejects_unknown_branch(self) -> None:
        with self.assertRaisesRegex(ValueError, "branch must be A or B"):
            cabc.branch_index(3, 0, "C")

    def test_local_roots_rejects_negative_level(self) -> None:
        with self.assertRaisesRegex(ValueError, "level must be nonnegative"):
            cabc.local_roots(3, 7, -1, "A")

    def test_hensel_rejects_nonpositive_exponent(self) -> None:
        with self.assertRaisesRegex(ValueError, "exponent must be positive"):
            cabc.hensel(3, 7, 0, "A", 2, 0)

    def test_program_seed_validates_transfer_prime_first(self) -> None:
        condition = cabc.Condition(7, 0, "A", 1, 1)

        with self.assertRaisesRegex(ValueError, "ell must be an odd prime"):
            cabc.program_seed(9, (condition,))


if __name__ == "__main__":
    unittest.main()

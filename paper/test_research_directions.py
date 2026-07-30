#!/usr/bin/env python3
"""Regression tests for the Phase 5 average and all-degree directions."""

from __future__ import annotations

import math
import json
import unittest
from fractions import Fraction
from pathlib import Path

import chebyshev_abc as cabc
import chebyshev_research as research
import verify_research_directions as verification


class LocalMeanTests(unittest.TestCase):
    def test_branch_value_requires_transfer_prime_unit(self) -> None:
        with self.assertRaisesRegex(ValueError, "coprime"):
            research.branch_value(
                ell=3,
                level=0,
                branch="A",
                a=1,
                b=1,
                modulus=9,
            )

    def test_primitive_projective_density_by_direct_count(self) -> None:
        """The conditional density has the claimed p+1 correction."""
        ell = 3
        level = 0
        branch = "A"
        p = 7
        exponent = 2
        modulus = p**exponent
        roots = cabc.local_roots(ell, p, level, branch)
        degree = ell**level * (ell - 1) // 2

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

        self.assertEqual(len(roots), degree)
        self.assertEqual(
            Fraction(divisible, primitive),
            Fraction(degree, p ** (exponent - 1) * (p + 1)),
        )

    def test_local_mean_matches_direct_prime_sum(self) -> None:
        ell = 3
        levels = 3
        cutoff = 500
        expected = 0.0

        for level in range(levels):
            q = ell ** (level + 1)
            phi_q = q - q // ell

            for p in cabc.primes_upto(cutoff):
                if p in (2, ell):
                    continue
                if (p - 1) % q == 0 or (p + 1) % q == 0:
                    expected += phi_q * math.log(p) / (p * p - 1)

        self.assertAlmostEqual(
            research.truncated_local_mean(ell, levels, cutoff),
            expected,
            places=14,
        )

    def test_two_is_not_a_local_defect_prime(self) -> None:
        """The congruence 3 | 2^2-1 must not add a spurious 2-adic term."""
        self.assertEqual(
            research.truncated_local_mean(3, levels=1, prime_cutoff=2),
            0.0,
        )

    def test_explicit_bound_is_uniform_in_level_and_cutoff(self) -> None:
        for ell in (3, 5, 7, 11):
            bound = research.local_mean_bound(ell)

            for levels in (1, 2, 4, 8):
                value = research.truncated_local_mean(
                    ell,
                    levels,
                    20_000,
                )
                self.assertLessEqual(value, bound)

    def test_seed_box_density_constants(self) -> None:
        self.assertEqual(
            research.seed_density_constant(3),
            Fraction(2, 3) * Fraction(2, 3 * 4),
        )
        self.assertEqual(
            research.seed_density_constant(5),
            Fraction(2, 3 * 6),
        )


class UniversalTransferTests(unittest.TestCase):
    def test_degree_two_recovers_quadratic_transfer(self) -> None:
        self.assertEqual(
            research.universal_transfer(2, 1, 8),
            (32, 49, 81),
        )

    def test_odd_prime_recovers_existing_transfer(self) -> None:
        for ell, a, b in ((3, 3, 2), (5, 5, 2), (7, 7, 2)):
            s_value, c_value = cabc.sc(ell, a, b)
            self.assertEqual(
                research.universal_transfer(ell, a, b),
                (
                    a * s_value * s_value,
                    b * c_value * c_value,
                    (a + b) ** ell,
                ),
            )

    def test_composite_transfers_are_primitive_and_semiconjugate(self) -> None:
        for degree, a, b in (
            (6, 3, 2),
            (9, 9, 2),
            (10, 5, 2),
            (12, 3, 2),
            (15, 15, 4),
        ):
            next_a, next_b, next_c = research.universal_transfer(
                degree,
                a,
                b,
            )
            self.assertEqual(next_a + next_b, next_c)
            self.assertEqual(math.gcd(next_a, next_b), 1)
            self.assertNotEqual(next_a % 2, next_b % 2)

            x = Fraction(b - a, a + b)
            next_x = Fraction(next_b - next_a, next_c)
            self.assertEqual(
                next_x,
                research.chebyshev_t(degree, x),
            )

    def test_transfers_commute_and_compose(self) -> None:
        for first, second in ((2, 3), (3, 5), (4, 6)):
            a, b = 3, 2
            first_row = research.universal_transfer(first, a, b)
            composed = research.universal_transfer(
                second,
                first_row[0],
                first_row[1],
            )
            direct = research.universal_transfer(first * second, a, b)
            reverse_row = research.universal_transfer(second, a, b)
            reversed_composition = research.universal_transfer(
                first,
                reverse_row[0],
                reverse_row[1],
            )

            self.assertEqual(composed, direct)
            self.assertEqual(reversed_composition, direct)

    def test_coordinate_factor_split_for_every_degree(self) -> None:
        a, b = 3, 2

        for degree in range(2, 21):
            next_a, next_b, _ = research.universal_transfer(degree, a, b)

            if degree % 2:
                self.assertEqual(next_a % a, 0)
                self.assertEqual(next_b % b, 0)
                left_square = next_a // a
                right_square = next_b // b
            else:
                self.assertEqual(next_a % (a * b), 0)
                left_square = next_a // (a * b)
                right_square = next_b

            self.assertEqual(math.isqrt(left_square) ** 2, left_square)
            self.assertEqual(math.isqrt(right_square) ** 2, right_square)

    def test_lucas_layer_normalization_and_support_separation(self) -> None:
        cases = (
            (2, 1, 8),
            (3, 3, 2),
            (5, 5, 2),
            (6, 3, 2),
            (9, 9, 2),
            (10, 5, 2),
            (12, 3, 2),
            (15, 15, 4),
            (30, 15, 4),
        )

        for degree, a, b in cases:
            self.assertEqual(
                research.degree_admissibility_errors(degree, a, b),
                [],
            )
            layers = [
                research.normalized_layer(degree, a, b, level)
                for level in range(2)
            ]
            seed_support = degree * a * b * (a + b)

            self.assertTrue(all(layer > 0 for layer in layers))
            self.assertTrue(
                all(math.gcd(layer, seed_support) == 1 for layer in layers)
            )
            self.assertEqual(math.gcd(layers[0], layers[1]), 1)

    def test_normalization_sweep_through_degree_twenty(self) -> None:
        for degree in range(2, 21):
            seed = None

            for a in range(1, 200):
                for b in range(1, 80):
                    if not research.degree_admissibility_errors(
                        degree,
                        a,
                        b,
                    ):
                        seed = (a, b)
                        break
                if seed is not None:
                    break

            self.assertIsNotNone(seed, degree)
            assert seed is not None
            a, b = seed
            layers = [
                research.normalized_layer(degree, a, b, level)
                for level in range(2)
            ]
            seed_support = degree * a * b * (a + b)
            self.assertTrue(
                all(math.gcd(layer, seed_support) == 1 for layer in layers)
            )
            self.assertEqual(math.gcd(layers[0], layers[1]), 1)

    def test_bad_three_adic_seed_is_rejected(self) -> None:
        self.assertNotEqual(
            research.degree_admissibility_errors(15, 15, 2),
            [],
        )
        self.assertNotEqual(
            research.degree_admissibility_errors(3, 3, 1),
            [],
        )

    def test_layer_indices_partition_divisors(self) -> None:
        degree = 12
        layers = [set(research.layer_indices(degree, j)) for j in range(3)]

        self.assertTrue(all(layers[i].isdisjoint(layers[j])
                            for i in range(3)
                            for j in range(i)))
        self.assertEqual(
            set().union(*layers),
            set(research.divisors(degree**3)) - {1},
        )

    def test_exact_radical_telescope_for_new_degrees(self) -> None:
        for degree, a, b, steps in (
            (2, 1, 8, 2),
            (3, 3, 2, 2),
            (6, 3, 2, 1),
            (9, 9, 2, 1),
            (10, 5, 2, 1),
        ):
            rows = research.universal_orbit(degree, a, b, steps)
            layers = [
                research.normalized_layer(degree, a, b, level)
                for level in range(steps)
            ]
            expected_radical = research.radical(a * b * (a + b))

            for index, row in enumerate(rows):
                actual_radical = research.radical(
                    row.a * row.b * row.c
                )
                self.assertEqual(actual_radical, expected_radical)

                if index < len(layers):
                    expected_radical *= research.radical(layers[index])


class RecordedVerificationTests(unittest.TestCase):
    def test_recorded_results_match_harness(self) -> None:
        expected = json.loads(
            Path("verification-results-research-directions.json").read_text(
                encoding="utf-8"
            )
        )
        actual = {
            "passed": True,
            "primitive_density": verification.verify_density(),
            "local_means": verification.verify_local_means(),
            "composite_layers": verification.verify_composite_layers(),
            "specializations": verification.verify_specializations(),
            "bad_three_adic_seed_rejected": [15, 15, 2],
        }
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

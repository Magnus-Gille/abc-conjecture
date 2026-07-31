#!/usr/bin/env python3
"""Independent regression tests for the Phase 7 polynomial-window checks."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from polynomial_window_check import (
    deep_split_coefficients,
    lucas_rank,
    lucas_u_mod,
    super_wieferich_hits,
    wieferich_hits,
)


class LucasArithmeticTests(unittest.TestCase):
    def test_binary_algebra_matches_direct_recurrence(self):
        for p_parameter, q_parameter in ((14, 81), (-2, 25), (-6, 49)):
            for modulus in (49, 121, 289):
                direct = [0, 1]
                for _ in range(2, 26):
                    direct.append(
                        (p_parameter * direct[-1] - q_parameter * direct[-2])
                        % modulus
                    )
                for index, expected in enumerate(direct):
                    self.assertEqual(
                        lucas_u_mod(index, p_parameter, q_parameter, modulus),
                        expected,
                    )

    def test_canonical_wieferich_census(self):
        self.assertEqual(wieferich_hits(14, 81, 100_000), [65_519])
        self.assertEqual(wieferich_hits(-2, 25, 100_000), [47])
        self.assertEqual(wieferich_hits(-6, 49, 100_000), [53])

    def test_hit_ranks_are_not_orbit_prime_powers(self):
        cases = (
            (14, 81, 65_519, 455, 2),
            (-2, 25, 47, 24, 3),
            (-6, 49, 53, 26, 5),
        )
        for p_parameter, q_parameter, prime, expected_rank, orbit_degree in cases:
            rank = lucas_rank(p_parameter, q_parameter, prime)
            self.assertEqual(rank, expected_rank)
            while rank % orbit_degree == 0:
                rank //= orbit_degree
            self.assertNotEqual(rank, 1)

    def test_no_canonical_super_wieferich_hit_below_bound(self):
        self.assertEqual(super_wieferich_hits(14, 81, 100_000), [])
        self.assertEqual(super_wieferich_hits(-2, 25, 100_000), [])
        self.assertEqual(super_wieferich_hits(-6, 49, 100_000), [])


class TruncationIdentityTests(unittest.TestCase):
    def test_exact_layer_cake_split(self):
        # Symbolic integer weights avoid hiding an indexing error in floats.
        exponents = {7: 2, 17: 5, 89: 1, 97: 9}
        weights = {7: 3, 17: 5, 89: 7, 97: 11}
        for cutoff in range(1, 10):
            defect, truncated, tail = deep_split_coefficients(
                exponents, weights, cutoff
            )
            self.assertEqual(defect, truncated + tail)
        self.assertEqual(deep_split_coefficients(exponents, weights, 2), (111, 35, 76))


if __name__ == "__main__":
    unittest.main()

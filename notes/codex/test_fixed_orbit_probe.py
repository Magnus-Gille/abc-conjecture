#!/usr/bin/env python3
"""Regression tests for the bounded fixed-orbit factorization probe."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fixed_orbit_probe as probe


class FactorizationAuditTests(unittest.TestCase):
    def test_rejects_inexact_factorization(self) -> None:
        with self.assertRaises(ValueError):
            probe.audit_factorization(45, {3: 2})

    def test_rejects_composite_factor_as_prime(self) -> None:
        with self.assertRaises(ValueError):
            probe.audit_factorization(45, {9: 1, 5: 1})

    def test_exact_defect(self) -> None:
        audit = probe.audit_factorization(2**3 * 3 * 5**2, {2: 3, 3: 1, 5: 2})

        self.assertAlmostEqual(
            audit.log_defect,
            2 * probe.math.log(2) + probe.math.log(5),
        )
        self.assertEqual(audit.largest_squared_prime, 5)
        self.assertEqual(audit.excess_exponent, 3)


class CanonicalLayerTests(unittest.TestCase):
    def test_expected_initial_values(self) -> None:
        layers = probe.canonical_layers(
            quadratic_levels=3,
            cubic_levels=2,
            quintic_levels=2,
        )
        values = {
            (layer.orbit, layer.level): layer.value
            for layer in layers
        }

        self.assertEqual(values["quadratic", 0], 7)
        self.assertEqual(values["quadratic", 1], 17)
        self.assertEqual(values["quadratic", 2], 31 * 193)
        self.assertEqual(values["cubic", 0], 7)
        self.assertEqual(values["cubic", 1], 17 * 89)
        self.assertEqual(values["quintic", 0], 11 * 29)
        self.assertEqual(
            values["quintic", 1],
            199 * 11_549 * 892_254_749,
        )

    def test_congruence_floor(self) -> None:
        quadratic = probe.LayerValue("quadratic", 2, 3, 31 * 193)
        cubic = probe.LayerValue("cubic", 3, 2, 613_279 * 5_746_087)

        self.assertEqual(quadratic.order_modulus, 32)
        self.assertTrue(quadratic.prime_has_forced_congruence(31))
        self.assertTrue(quadratic.prime_has_forced_congruence(193))
        self.assertEqual(cubic.order_modulus, 27)
        self.assertTrue(cubic.prime_has_forced_congruence(613_279))
        self.assertTrue(cubic.prime_has_forced_congruence(5_746_087))

    def test_discovered_factorization_is_a_replayable_certificate(self) -> None:
        layer = probe.canonical_layers(7, 0, 0)[6]
        report = probe.analyze_layer(layer, factor_limit=100)

        self.assertTrue(report["factorization_complete"])
        self.assertEqual(report["factorization_method"], "stored-certificate")
        self.assertTrue(report["squarefree"])

    def test_quadratic_level_seven_factorization_certificate(self) -> None:
        layer = probe.canonical_layers(8, 0, 0)[7]
        report = probe.analyze_layer(layer, factor_limit=100)

        self.assertTrue(report["factorization_complete"])
        self.assertEqual(report["factorization_method"], "stored-certificate")
        self.assertTrue(report["certified_primes_obey_congruence"])
        self.assertTrue(report["squarefree"])
        self.assertEqual(
            [int(component["value"]) for component in report["components"]],
            [
                189_439,
                750_692_351,
                9_825_841_153,
                298_196_593_663,
                991_245_449_894_911,
                6_726_631_000_961_507_661_177_857,
                28_434_404_151_626_641_091_139_435_909_034_910_237_447_173_121,
            ],
        )


if __name__ == "__main__":
    unittest.main()

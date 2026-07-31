#!/usr/bin/env python3
"""Regression tests for the level-seven Pocklington certificate bundle."""

import copy
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from pocklington_certificate import verify_bundle


HERE = Path(__file__).resolve().parent
CERTIFICATE = HERE / "quadratic-level7-pocklington.json"


class PocklingtonCertificateTests(unittest.TestCase):
    def test_level_seven_bundle_verifies(self) -> None:
        bundle = json.loads(CERTIFICATE.read_text())
        self.assertTrue(verify_bundle(bundle))

    def test_tampered_witness_is_rejected(self) -> None:
        bundle = json.loads(CERTIFICATE.read_text())
        tampered = copy.deepcopy(bundle)
        root = tampered["roots"][-1]
        first_q = next(iter(tampered["certificates"][root]["witnesses"]))
        tampered["certificates"][root]["witnesses"][first_q] = 1
        with self.assertRaises(ValueError):
            verify_bundle(tampered)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
"""Regression tests for the all-index Cayley atom classification."""

from __future__ import annotations

import math
import unittest

import composite_atom as atoms


def lucas_u_mod(index: int, a: int, b: int, prime: int) -> int:
    """Evaluate the fixed Lucas sequence modulo prime."""
    previous, current = 0, 1
    trace = 2 * (b - a) % prime
    norm = (a + b) ** 2 % prime

    for _ in range(index):
        previous, current = current, (trace * current - norm * previous) % prime

    return previous


def exact_rank_roots(index: int, prime: int) -> set[int]:
    """Brute-force projective ratios whose Lucas rank is exactly index."""
    result: set[int] = set()

    for rho in range(prime):
        if lucas_u_mod(index, rho, 1, prime):
            continue
        if any(
            lucas_u_mod(index // divisor, rho, 1, prime) == 0
            for divisor in atoms.prime_divisors(index)
        ):
            continue
        result.add(rho)

    return result


class CoordinateAtomTests(unittest.TestCase):
    def test_general_root_count_sign_and_simplicity_proxy(self) -> None:
        indices = (3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 30)

        for index in indices:
            for prime in atoms.primes_upto(199):
                if prime == 2 or index % prime == 0:
                    continue

                roots = atoms.coordinate_roots(index, prime)
                split = (prime - 1) % index == 0
                inert = (prime + 1) % index == 0
                expected = atoms.euler_phi(index) // 2 if split or inert else 0

                self.assertEqual(len(roots), expected, (index, prime))
                self.assertNotIn(0, roots)
                self.assertNotIn(prime - 1, roots)

                if roots:
                    chi = 1 if split else -1
                    self.assertTrue(
                        all(atoms.legendre_symbol(-rho, prime) == chi for rho in roots)
                    )

    def test_distinct_indices_have_disjoint_root_sets(self) -> None:
        indices = (3, 4, 5, 6, 8, 9, 10, 12, 15, 18)

        for prime in atoms.primes_upto(251):
            if prime == 2:
                continue
            seen: dict[int, int] = {}

            for index in indices:
                if index % prime == 0:
                    continue
                for rho in atoms.coordinate_roots(index, prime):
                    self.assertNotIn(rho, seen, (prime, rho, seen.get(rho), index))
                    seen[rho] = index


class UniversalAtomTests(unittest.TestCase):
    def test_square_index_conversion(self) -> None:
        self.assertEqual(atoms.coordinate_indices(3), (3, 6))
        self.assertEqual(atoms.coordinate_indices(4), (8,))
        self.assertEqual(atoms.coordinate_indices(15), (15, 30))
        self.assertEqual(atoms.coordinate_indices(18), (36,))

    def test_universal_atom_roots_equal_exact_lucas_rank(self) -> None:
        for index in (2, 3, 4, 5, 6, 8, 9, 10, 12, 15):
            for prime in atoms.primes_upto(199):
                if prime == 2 or index % prime == 0:
                    continue
                self.assertEqual(
                    atoms.universal_roots(index, prime),
                    exact_rank_roots(index, prime),
                    (index, prime),
                )

    def test_layer_counts_are_additive(self) -> None:
        for degree in (4, 6, 10, 12, 15, 30):
            for level in (0, 1):
                indices = atoms.layer_indices(degree, level)
                for prime in atoms.primes_upto(251):
                    if prime == 2 or degree % prime == 0:
                        continue

                    roots: set[int] = set()
                    expected = 0
                    for index in indices:
                        atom_roots = atoms.universal_roots(index, prime)
                        self.assertTrue(roots.isdisjoint(atom_roots))
                        roots.update(atom_roots)
                        modulus = atoms.compatibility_modulus(index)
                        if (prime - 1) % modulus == 0 or (prime + 1) % modulus == 0:
                            expected += atoms.euler_phi(index)

                    self.assertEqual(len(roots), expected, (degree, level, prime))


class CompositeMeanTests(unittest.TestCase):
    def test_finite_mean_matches_direct_formula(self) -> None:
        degree, levels, cutoff = 12, 3, 1000
        direct = 0.0

        for level in range(levels):
            for index in atoms.layer_indices(degree, level):
                modulus = atoms.compatibility_modulus(index)
                for prime in atoms.primes_upto(cutoff):
                    if prime == 2 or degree % prime == 0:
                        continue
                    if (prime - 1) % modulus == 0 or (prime + 1) % modulus == 0:
                        direct += (
                            atoms.euler_phi(index)
                            * math.log(prime)
                            / (prime * prime - 1)
                        )

        self.assertAlmostEqual(
            atoms.truncated_composite_mean(degree, levels, cutoff),
            direct,
            places=14,
        )

    def test_smooth_index_bound_is_uniform(self) -> None:
        for degree in (4, 6, 10, 12, 15, 30):
            bound = atoms.composite_mean_bound(degree)
            for levels in (1, 2, 3, 4):
                self.assertLessEqual(
                    atoms.truncated_composite_mean(degree, levels, 20_000),
                    bound,
                )


if __name__ == "__main__":
    unittest.main()

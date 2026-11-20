"""Certified interval for the density of twists with no repeated full split-prime factor.

Integer rounding gives bounds for the sum of the local probabilities. The
analytic tail and conversion to an Euler product are in the companion note.
"""

from fractions import Fraction
from math import isqrt

from sympy import isprime, primerange

from abc_odd_rank_squareclass_support import division_values
from abc_split_repeated_verify import proper


def density_bounds(max_q=12000, max_norm=3500, prime_sum_limit=10**6):
    unit = 10**19
    shifts = [
        (2 * j, b, 4 * j * j + 2 * b * b)
        for b in range(1, isqrt(max_norm // 2) + 1)
        for j in range(-isqrt((max_norm - 2 * b * b) // 4),
                       isqrt((max_norm - 2 * b * b) // 4) + 1)
    ]
    qs = [q for q in primerange(11, prime_sum_limit + 1) if q % 8 in (1, 3)]
    partial_sum = 0
    number_pairs = 0
    seed_hits = 0
    for q in qs:
        if q > max_q:
            break
        for a, b, d in shifts:
            p = q*q*d + 2*q*a + 1
            assert p < 2**64  # sympy.isprime is deterministic in this range.
            if not isprime(p):
                continue
            seed = division_values(p)(q) == 0 and not proper(q, p)
            roots = (q - 1)**2 - int(seed)
            partial_sum += unit * roots // (p*p)
            number_pairs += 1
            seed_hits += int(seed)
    def reciprocal_upper(indices):
        return Fraction(sum((unit + q*q - 1) // (q*q) for q in indices), unit)
    q_small = reciprocal_upper(q for q in qs if q <= max_q)
    q_large = reciprocal_upper(q for q in qs if q > max_q) + Fraction(1, prime_sum_limit)
    tail = Fraction(4, 3) * (Fraction(2, 3)*q_large + Fraction(2, max_norm)*q_small)
    local_lower = Fraction(partial_sum, unit)
    local_upper = Fraction(partial_sum + number_pairs, unit) + tail
    lower = 1 - local_upper
    upper = 1 - local_lower + local_upper**2 / 2
    print("split prime/rational prime pairs", number_pairs, "seed incidences", seed_hits)
    print("outward-rounded avoidance probability",
          lower.numerator * 10**7 // lower.denominator, "/ 10000000 through",
          -(-upper.numerator * 10**7 // upper.denominator), "/ 10000000")
    return lower, upper


if __name__ == "__main__":
    density_bounds()

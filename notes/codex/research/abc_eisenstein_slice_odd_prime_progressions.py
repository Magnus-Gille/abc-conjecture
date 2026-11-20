"""Certify simultaneously compatible, independently liftable quartic contacts."""

import csv
from fractions import Fraction
from hashlib import sha256
from math import gcd, isqrt, lcm
from pathlib import Path

from abc_eisenstein_slice_paired_quartic import poly_value, prime_factors, times


def prime(p):
    return p >= 2 and all(p % j for j in range(2, isqrt(p) + 1))


def certificate():
    archive = Path(__file__).with_name("abc_eisenstein_slice_paired_quartic_1m.csv")
    choices = {}
    with archive.open() as stream:
        for row in csv.DictReader(stream):
            p, r, period, root = (int(row[key]) for key in ("p", "r", "odd_period", "h"))
            if 10_000 <= p <= 1_000_000:
                choices.setdefault(p, []).append((r, period, root))

    n, modulus, product = 1, 2, 1
    selected = []
    for p, rows in sorted(choices.items()):
        r, period, _ = rows[0]
        assert all(row[:2] == (r, period) for row in rows)
        common = gcd(period, modulus)
        if modulus % p == 0 or gcd(product, period) != 1:
            continue
        root = next((h for _, _, h in rows if (h - n) % common == 0), None)
        if root is None:
            continue

        assert prime(p) and lcm(2, r) == period
        Q = (-8 % p, -64 % p)
        assert times(r, Q, p) is None
        assert all(times(r // factor, Q, p) is not None for factor in prime_factors(r))
        initial = poly_value(root, p * p)
        translated = poly_value(root + period, p * p)
        assert initial % p == translated % p == 0 and initial != translated

        new_factor = period // common
        step = (root - n) // common * pow(modulus // common, -1, new_factor)
        n += modulus * (step % new_factor)
        modulus *= new_factor
        product *= p
        selected.append((p, period, root))

    assert gcd(modulus, product) == 1
    assert all((n - h) % period == 0 for p, period, h in selected)
    loss = sum((Fraction(1, p) for p, _, _ in selected), Fraction())
    assert loss < Fraction(45, 10_000)
    for offset in range(537):
        witness = n + modulus * offset
        if all(poly_value(witness % (p * period), p * p) != 0
               for p, period, _ in selected):
            break
    else:
        raise AssertionError("The elementary union bound guarantees a witness.")
    print("selected, base period bits, prime product bits", len(selected),
          modulus.bit_length(), product.bit_length())
    print("base period and prime product coprime", gcd(modulus, product) == 1)
    print("union-bound retention", float(1 - loss))
    print("first witness offset and index bits", offset, witness.bit_length())
    print("prime list digest", sha256(",".join(str(p) for p, _, _ in selected).encode()).hexdigest())
    print("base index and period digest", sha256(f"{n},{modulus}".encode()).hexdigest())


if __name__ == "__main__":
    certificate()

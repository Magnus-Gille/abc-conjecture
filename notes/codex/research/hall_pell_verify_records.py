"""Certify the earliest and best log(D)/n records for the published prime pool."""

from csv import DictReader
from itertools import groupby
from math import prod
from pathlib import Path

from hall_pell_crt import SquareClass, combine, poly_value


RECORDS = [
    (163, (31,)),
    (62119, (31, 59)),
    (5996803, (31, 59, 79)),
    (757479583, (31, 41, 101, 809)),
    (416401035379, (31, 59, 181, 271, 479)),
]


def beats(d, n, d0, n0):
    """Compare log(d)/n and log(d0)/n0 using integer bounds only.

    Both products are squarefree integers > 1. Equality is possible only
    when the products and indices both agree, by unique factorization.
    """
    if d == d0:
        return n < n0
    if d <= d0 and n >= n0:
        return False
    precision = 1
    while True:
        x = (d**precision).bit_length() - 1
        y = (d0**precision).bit_length() - 1
        if (x + 1) * n0 <= y * n:
            return False
        if x * n0 >= (y + 1) * n:
            return True
        precision *= 2


def verify(groups, n0, primes):
    k = len(primes)
    d0 = prod(primes)
    j0, remainder = divmod(n0 - 7, 12)
    assert remainder == 0
    active = {
        c.prime for _, group in groups for c in group
        if j0 % c.modulus == c.residue and poly_value(j0, c.label, c.prime**2) == 0
    }
    assert set(primes) <= active
    if k == 1:
        for p, group in groups:
            for c in group:
                n = 7 + 12*c.residue
                assert n >= n0 and not beats(p, n, d0, n0)
        return
    # Each eligible k-tuple has exactly one pair of largest primes p < q.
    for i, (p, group) in enumerate(groups):
        if i < k - 2:
            continue
        lower = [(c.residue, c.modulus, c.prime)
                 for _, smaller in reversed(groups[:i]) for c in smaller]
        for q, other in groups[i+1:]:
            # D <= q*p^(k-1). Beyond this n ceiling even that upper bound
            # cannot beat the record. The ceiling also covers every n < n0.
            max_d = q * p**(k-1)
            ceiling = max(n0, n0 * max_d.bit_length() // (d0.bit_length() - 1))
            jmax = (ceiling - 7) // 12
            for c in group:
                for b in other:
                    pair = combine(c.residue, c.modulus, b.residue, b.modulus)
                    if pair is None:
                        continue
                    a, m = pair
                    for j in range(a, jmax + 1, m):
                        take = k - 2
                        d = p*q
                        if take:
                            for r, modulus, small_p in lower:
                                if j % modulus == r:
                                    # Classes for the same prime are disjoint.
                                    d *= small_p
                                    take -= 1
                                    if take == 0:
                                        break
                        if take == 0:
                            n = 7 + 12*j
                            assert n >= n0 and not beats(d, n, d0, n0), (k, n, d)


def main():
    path = Path(__file__).with_name('hall_pell_classes.csv')
    with path.open(newline='') as f:
        classes = sorted(
            (SquareClass(int(row['prime']), row['factor'], int(row['j_residue']),
                         int(row['j_modulus'])) for row in DictReader(f)),
            key=lambda c: c.prime,
        )
    groups = [(p, list(rows)) for p, rows in groupby(classes, key=lambda c: c.prime)]
    assert len(classes) == 530 and len(groups) == 249
    for n, primes in RECORDS:
        verify(groups, n, primes)
        print(f'Certified k={len(primes)}, n={n}, D={prod(primes)}')


if __name__ == '__main__':
    main()

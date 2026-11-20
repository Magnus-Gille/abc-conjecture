"""Check complete early factorizations and find repeated primes in an index/prime box."""

import argparse
import json
from math import log, prod
from pathlib import Path

from flint import fmpz

from hall_pell_first_square import first_divisibility


def lucas_terms(last_n):
    u, v, f, g = fmpz(29), fmpz(9349), fmpz(13), fmpz(4181)
    for n in range(7, last_n + 1, 12):
        yield n, (u - 11, f, (u - 6)**2 - 20, (u - 9)**2 - 5)
        u, v = v, 322 * v - u
        f, g = g, 322 * g - f


def verify_factorizations():
    data = Path(__file__).with_name('hall_pell_early_factors.jsonl')
    rows = [json.loads(line) for line in data.read_text().splitlines()]
    assert rows and [row['n'] for row in rows] == list(range(7, rows[-1]['n'] + 1, 12))
    early_squares = []
    for (n, values), row in zip(lucas_terms(rows[-1]['n']), rows):
        primes = {2, 3, 5}
        for name, value in zip('tzAB', values):
            factors = row[name]
            assert len({p for p, e in factors}) == len(factors)
            assert all(e > 0 and fmpz(p).is_prime() for p, e in factors)
            assert prod(p**e for p, e in factors) == value
            primes.update(p for p, e in factors)
            early_squares.extend((n, name, p, e) for p, e in factors if name in 'AB' and e >= 2)
        t, z, a, b = values
        height = a**3
        radical = prod(primes)
        assert 1728 * t + 5 * (z*b)**2 == height
        assert (height**10 > fmpz(radical)**11) == (n == 7)
        if n in (7, 163, 223):
            print("n, abc quality:", n, log(int(height))/log(radical))
    print("All repeated primes in A and B through", rows[-1]['n'], ":", early_squares)


def batch_remainders(values, limit):
    layers = [values]
    while len(layers[-1]) > 1:
        layer = layers[-1]
        layers.append([layer[i] * layer[i + 1] if i + 1 < len(layer) else layer[i]
                       for i in range(0, len(layer), 2)])
    residues = [fmpz.primorial_ui(limit) % layers[-1][0]]
    for layer in reversed(layers[:-1]):
        residues = [residues[i // 2] % value for i, value in enumerate(layer)]
    return residues


def square_census(last_n, limit):
    if last_n < 7 or limit < 2:
        raise ValueError("Need last_n >= 7 and prime limit >= 2.")
    values = [a * b for n, (t, z, a, b) in lucas_terms(last_n)]
    residues = batch_remainders(values, limit)
    rows = []
    for (n, (t, z, a, b)), value, residue in zip(lucas_terms(last_n), values, residues):
        small_radical = value.gcd(residue)
        repeated = small_radical.gcd(value // small_radical)
        if repeated == 1:
            continue
        for p, exponent in repeated.factor():
            assert p.is_prime() and exponent == 1
            label, term = ('A', a) if a % p == 0 else ('B', b)
            depth = 0
            while term % p == 0:
                depth += 1
                term //= p
            assert depth >= 2
            rows.append((n, int(p), label, depth))
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--last-n', type=int, default=20_000)
    parser.add_argument('--prime-limit', type=int, default=1_000_000_000)
    parser.add_argument('--early-only', action='store_true')
    args = parser.parse_args()
    verify_factorizations()
    if args.early_only:
        return
    rows = square_census(args.last_n, args.prime_limit)
    print("Square hits:", len(rows), "Distinct primes:", sorted({p for n, p, label, e in rows}))
    print("First appearances:", [(n, p, label) for n, p, label, e in rows
                                if first_divisibility(p, (n-7)//12) == (n-7)//12])
    print("Valuations above two:", [row for row in rows if row[-1] > 2])


if __name__ == '__main__':
    main()

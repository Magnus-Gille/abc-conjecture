"""Exhaust all lifted square classes from the finite paired-quartic census."""

import argparse
import csv
from collections import Counter
from math import prod
from pathlib import Path

from abc_eisenstein_slice_paired_quartic import poly_value


def highest_hit(p, index, period, upper_bound):
    """Return the exact highest depth and one witness in this root class."""
    level = 2
    if index > upper_bound:
        return 1, None
    modulus = p * p
    while True:
        next_modulus = modulus * p
        first = poly_value(index, next_modulus)
        next_value = poly_value(index + period, next_modulus)
        assert first % modulus == next_value % modulus == 0
        slope = ((next_value - first) // modulus) % p
        assert slope != 0
        digit = -(first // modulus) * pow(slope, -1, p) % p
        next_index = index + digit * period
        assert 0 < next_index < period * p and next_index % 2
        if next_index > upper_bound:
            return level, index
        index = next_index
        period *= p
        modulus = next_modulus
        level += 1


def independent_abscissa_polynomial(n, modulus):
    """Montgomery differential ladder, independently of the division polynomials."""
    b = -576
    fixed_x = -8
    def double(A):
        x,z = A
        return ((x*x-b*z*z)**2 % modulus,
                4*x*z*(x*x+b*z*z) % modulus)
    def differential_add(A,B):
        x,z = A
        y,w = B
        return ((x*y-b*z*w)**2 % modulus,
                fixed_x*(x*w-y*z)**2 % modulus)
    A, B = (1,0), (fixed_x,1)
    for bit in bin(n)[2:]:
        plus = differential_add(A,B)
        if bit == '0':
            A, B = double(A), plus
        else:
            A, B = plus, double(B)
    x,z = A
    result = x*pow(z,-1,modulus) % modulus
    return (result*result+336*result+576) % modulus


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('classes', type=Path)
    parser.add_argument('upper_bound', type=int)
    args = parser.parse_args()
    if args.upper_bound < 3:
        parser.error('the odd prefix starts at 3')
    per_prime = {}
    rows = 0
    with args.classes.open() as stream:
        for row in csv.DictReader(stream):
            p, r, odd_period, h, index, period, _ = map(int, row.values())
            assert period == odd_period * p
            assert 0 < index < period and index % odd_period == h
            depth, witness = highest_hit(p, index, period, args.upper_bound)
            if depth > per_prime.get(p, (0, None))[0]:
                per_prime[p] = (depth, witness)
            rows += 1
    product = prod(p ** (depth - 1) for p, (depth, _) in per_prime.items())
    maximum = max(depth for depth, _ in per_prime.values())
    for p, (depth, witness) in per_prime.items():
        if witness is None:
            continue
        modulus = p ** (depth + 1)
        value = independent_abscissa_polynomial(witness, modulus)
        assert value and value % (p ** depth) == 0
    print('prefix bound, classes, represented primes', args.upper_bound, rows, len(per_prime))
    print('prime counts by maximum valuation', sorted(Counter(v[0] for v in per_prime.values()).items()))
    print('maximum (p,depth,witness)', sorted((p,d,w) for p,(d,w) in per_prime.items() if d==maximum))
    print('bits of universal good-small-prime excess multiple', product.bit_length())
    print('bits including the fixed dyadic excess', (256 * product).bit_length())
    print('bits of full small-prime lcm including 2', (512 * product * prod(per_prime)).bit_length())


if __name__ == '__main__':
    main()

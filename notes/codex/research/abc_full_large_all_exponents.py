"""Test every possible power exponent in the recorded >n^4 full CM factors."""

from argparse import ArgumentParser
from csv import DictReader
from functools import cache
from math import isqrt
from pathlib import Path

from abc_odd_rank_quartic_cutoff import (
    Integer, all_primes, norm_denominator, prime_divisors, remove_support, split_generator,
)


@cache
def scalar_term(n):
    """The signed division polynomial after removal of 2^{5(n²−(n mod 2))/4}."""
    if n < 5:
        return Integer((0, 1, 1, -9, -14)[n])
    j = n // 2
    if not n % 2:
        return scalar_term(j) * (scalar_term(j+2)*scalar_term(j-1)**2
                                 - scalar_term(j-2)*scalar_term(j+1)**2)
    left = scalar_term(j+2)*scalar_term(j)**3
    right = scalar_term(j-1)*scalar_term(j+1)**3
    return left - 32*right if j % 2 else 32*left - right


def full_term(n):
    value = abs(scalar_term(n))
    for p in prime_divisors(n):
        m = n // p
        gen = split_generator(p)
        if gen is None:
            smaller = abs(scalar_term(m))
        else:
            a, b = gen
            smaller = norm_denominator(m*a, m*b)
        value = remove_support(value, smaller)
    return value


@cache
def test_prime(k, j):
    # Each returned prime has a subgroup of nonzero k-th powers of proper index k.
    h = 1 if not j else test_prime(k, j-1)
    while True:
        h += 2*k
        if all(h % t for t in range(3, isqrt(h)+1, 2)):
            return h


def check(limit):
    count = split = tests = largest_index = 0
    records = Path(__file__).with_name('abc_odd_rank_quartic_cutoff.csv')
    for row in DictReader(records.open()):
        n = int(row['n'])
        if not 7 <= n <= limit:
            continue
        full = full_term(n)
        small = int(row['small_full_part'])
        value, rem = divmod(full, small)
        digits = int(row['residual_bits'])
        assert not rem and value > 1 and value.bit_length() == digits
        # Any integral root would be at least n^4+1 since every prime factor is >n^4.
        bound = (digits-1) // ((n**4+1).bit_length()-1)
        for k in all_primes(bound):
            for j in range(100):
                h = test_prime(k, j)
                residue = int(value % h)
                if residue and pow(residue, (h-1)//k, h) != 1:
                    tests += 1
                    largest_index = max(largest_index, j+1)
                    break
            else:
                raise ArithmeticError(f'No local obstruction for n={n}, k={k}')
        count += 1
        split += prime_divisors(n) == (n,) and split_generator(n) is not None
    return count, split, tests, largest_index


if __name__ == '__main__':
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('--limit', type=int, default=1009)
    args = parser.parse_args()
    print('indices, split prime indices, exponents eliminated, largest test-prime index')
    print(check(args.limit))

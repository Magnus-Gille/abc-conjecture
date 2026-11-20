"""Rational upper bounds for the finite parts of the Pell square density."""

from csv import DictReader
from math import gcd
from pathlib import Path

from flint import fmpz

from abc_pell11_early_squares import compatible_primes, product
from abc_pell11_square_periods import projective_order


SCALE = 10**16


def rounded_upper(numerator, denominator):
    return (SCALE*numerator + denominator - 1)//denominator


def primes_dividing(primes, number):
    if number == 1 or not primes:
        return []
    if len(primes) <= 1000:
        return [p for p in primes if number % p == 0]
    mid = len(primes)//2
    left, right = primes[:mid], primes[mid:]
    factor = number.gcd(product([fmpz(p) for p in left]))
    return primes_dividing(left, factor) + primes_dividing(right, number//factor)


def main():
    small_limit, large_limit, order_limit = 10**7, 10**9, 4000
    archive = Path(__file__).with_name("abc_pell11_square_periods.csv")
    with archive.open() as source:
        rows = list(DictReader(source))
    compatible = compatible_primes(large_limit)
    assert [int(r["p"]) for r in rows] == [p for p in compatible if p <= small_limit]
    small_sum = sum(rounded_upper(int(r["root_classes"]),
                                  int(r["p"])*int(r["projective_period"]))
                    for r in rows)
    # Every odd prime with ord((1+sqrt(2))^4)=r divides a_(2r).
    a, b = 0, 1
    witnesses = []
    for _ in range(order_limit):
        a, b = 3*a+2*b, 4*a+3*b
        witnesses.append(fmpz(a))
    candidates = [p for p in compatible if p > small_limit]
    common = product(witnesses).gcd(product([fmpz(p) for p in candidates]))
    short = primes_dividing(candidates, common)
    assert product([fmpz(p) for p in short]) == common
    middle_sum = sum(rounded_upper(50, p*order_limit) for p in candidates)
    for p in short:
        # g is the square of the projective generator, in torus coordinates.
        m = projective_order(p)
        r = m//gcd(m, 2)
        assert r <= order_limit
        middle_sum += rounded_upper(50, p*r) - rounded_upper(50, p*order_limit)
    print("Scale", SCALE)
    print("Finite census upper numerator", small_sum)
    print("Middle upper numerator", middle_sum)
    print("Compatible middle primes and short orders", len(candidates), len(short))
    assert small_sum + middle_sum < 34*SCALE//100000


if __name__ == "__main__":
    main()

"""Verify lower bounds for C/(n rad(ABC)) using python-flint real balls."""
from math import prod

from flint import acb, arb, ctx


def main():
    ctx.prec = 500
    half = acb(1) / 2
    quarter = acb(1) / 4
    integral = acb.elliptic_k(half).real
    rotation = acb.elliptic_f(quarter, half, pi=True).real / integral
    cases = [
        ((13, 1, 0, 0, 0), 138),
        ((5, 0, 3, 2, 4), 9857),
        ((1, 5, 5, 0, 8), 15297),
        ((20, 0, 3, 0, 13), 142685),
    ]
    for exponents, lower_bound in cases:
        n = prod(p**e for p, e in zip((3, 11, 23, 37, 47), exponents))
        assert n % 3 == 0
        phase = n * rotation
        closest = (phase + arb(1) / 2).floor().unique_fmpz()
        assert closest is not None
        distance = abs(phase - closest)
        assert 0 < distance < arb(1) / 2
        ratio = 1 / (2 * arb(3).sqrt() * integral * distance)
        assert lower_bound < ratio < lower_bound + 1
        print(n, 'has C/(nR) greater than', lower_bound)


if __name__ == '__main__':
    main()

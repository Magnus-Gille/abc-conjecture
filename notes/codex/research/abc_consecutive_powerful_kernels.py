"""Exclude three consecutive powerful integers with bounded squarefree kernels."""

from argparse import ArgumentParser
from decimal import Decimal, localcontext
from fractions import Fraction
from functools import cache
from itertools import product
from math import gcd, isqrt


EXPONENT_BOUND = 10**30


def prime(n):
    return n >= 2 and all(n % k for k in range(2, isqrt(n) + 1))


def admissible_kernels(limit):
    kernels = [n for n in range(1, limit + 1)
               if all(n % (k*k) for k in range(2, isqrt(n) + 1))]
    moduli = [512, 81, 25, 49, 121, 169]
    moduli.extend(p for p in range(17, limit + 1) if prime(p))
    masks = []
    for modulus in moduli:
        squares = {t*t % modulus for t in range(modulus)}
        rows = {}
        for d in kernels:
            residues = {d**3 * s % modulus for s in squares}
            for shift in (-1, 0, 1):
                rows[d, shift] = sum(1 << ((r - shift) % modulus) for r in residues)
        masks.append(rows)
    for a, b, c in product(kernels, repeat=3):
        if gcd(a, b) > 1 or gcd(a, c) > 1 or gcd(b, c) > 1:
            continue
        if (a, b, c).count(1) >= 2:
            continue
        if all(row[a, -1] & row[b, 0] & row[c, 1] for row in masks):
            yield a, b, c


@cache
def pell_unit(d):
    """The least positive x,y satisfying x²−d y²=1, from sqrt(d)'s convergents."""
    base = isqrt(d)
    assert base*base < d
    offset, denominator, term = 0, 1, base
    p0, p1, q0, q1 = 0, 1, 1, 0
    while True:
        x, y = term*p1+p0, term*q1+q0
        if x*x-d*y*y == 1:
            assert (2*x).bit_length() <= 10000
            return x, y
        offset = denominator*term-offset
        denominator = (d-offset*offset)//denominator
        term = (base+offset)//denominator
        p0, p1, q0, q1 = p1, x, q1, y


@cache
def log_unit_interval(d):
    """Enclose log(x + sqrt(x²−1)). Decimal.sqrt and .ln are correctly rounded."""
    x, _ = pell_unit(d)
    with localcontext() as ctx:
        ctx.prec = 140
        root = Decimal(x*x - 1).sqrt()
        lo = (Decimal(x) + root.next_minus()).next_minus()
        hi = (Decimal(x) + root.next_plus()).next_plus()
        return Fraction(lo.ln().next_minus()), Fraction(hi.ln().next_plus())


def height_bound(left_d, right_d):
    low1, high1 = log_unit_interval(left_d)
    low2, high2 = log_unit_interval(right_d)
    low, high = low1/high2, high1/low2
    num, den = ((low + high) / 2).as_integer_ratio()
    p0, p1, q0, q1 = 0, 1, 1, 0
    while den:
        term, rem = divmod(num, den)
        p, q = term*p1 + p0, term*q1 + q0
        if q > 2*EXPONENT_BOUND:
            error = max(abs(q*low-p), abs(q*high-p))
            assert 2*EXPONENT_BOUND*error < 1
            return 4*q
        num, den = den, rem
        p0, p1, q0, q1 = p1, p, q1, q
    raise ArithmeticError('Insufficient logarithm precision')


def square_quotient(value, divisor):
    quotient, remainder = divmod(value, divisor)
    return remainder == 0 and isqrt(quotient)**2 == quotient


def check(limit):
    considered, steps, max_bound, max_bits = 0, 0, 0, 0
    hits = []
    for a, b, c in admissible_kernels(limit):
        considered += 1
        d, other_d = a*b, b*c
        for radicand in (d, other_d):
            rational_part, _ = pell_unit(radicand)
            max_bits = max(max_bits, (2*rational_part).bit_length())
        bound = height_bound(d, other_d)
        max_bound = max(max_bound, bound)
        x, y = pell_unit(d)
        u, v = x, y
        while u <= 2*bound:
            steps += 1
            if u % 2:
                n = (u+1)//2
                if n >= 2 and all(square_quotient(n+i, h**3)
                                  for i, h in zip((-1, 0, 1), (a, b, c))):
                    hits.append((a, b, c, n))
            u, v = x*u + d*y*v, y*u + x*v
    return considered, steps, max_bound, max_bits, hits


if __name__ == '__main__':
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('limit', nargs='?', type=int, default=500)
    args = parser.parse_args()
    print('local survivors, recurrence terms, largest height bound, largest unit bit bound, hits')
    print(check(args.limit))

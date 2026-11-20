"""Exact finite search for prime divisors above n^4 in the full CM packet of B_n.

Python 3.9+. python-flint accelerates the rational point arithmetic but is optional.
Start with --odd-limit 35 --prime-limit 61 to exercise the pure-Python version.
"""
import argparse
import csv
import sys
from fractions import Fraction
from functools import cache
from itertools import compress
from math import gcd, isqrt, lcm, prod

try:
    from flint import fmpq as Rational, fmpz as Integer
except ImportError:
    Rational, Integer = Fraction, int


def common_divisor(x, y):
    return x.gcd(y) if Integer is not int else gcd(x, y)


def integer_sqrt(x):
    return x.isqrt() if Integer is not int else isqrt(x)


@cache
def multiple(n):
    if n == 1:
        return Rational(-8), Rational(16)
    if n % 2:
        x, y = multiple(n-1)
        u, v = multiple(1)
        slope = (y-v)/(x-u)
    else:
        x, y = multiple(n//2)
        u = x
        slope = (3*x*x+32*x+32)/(2*y)
    z = slope*slope-16-x-u
    return z, slope*(x-z)-y


@cache
def denominator(n):
    x, _ = multiple(n)
    value = integer_sqrt(x.denominator)
    assert value*value == x.denominator and value % 2
    return value


@cache
def norm_denominator(a, b):
    """Odd norm of the square-root abscissa denominator ideal for [a+b*tau]R."""
    x, y = multiple(a)
    u, v = multiple(b)
    u, c = -(u+16+32/u)/2, v*(1-32/u**2)/4  # coordinates of [b*tau]R are (u,c*tau)
    real = (y*y-2*c*c)/(u-x)**2-16-x-u
    imag = -2*y*c/(u-x)**2
    w = Integer(lcm(real.denominator, imag.denominator))
    m, j = Integer((real*w).numerator), Integer((imag*w).numerator)
    assert common_divisor(w, common_divisor(m, j)) == 1
    norm = w*w//common_divisor(w, m*m+2*j*j)
    value = integer_sqrt(norm)
    assert value*value == norm
    return value//(value & -value)


@cache
def prime_divisors(n):
    factors = []
    for p in range(2, isqrt(n)+1):
        if n % p == 0:
            factors.append(p)
            while n % p == 0:
                n //= p
    if n > 1:
        factors.append(n)
    return tuple(factors)


@cache
def split_generator(p):
    for b in range(1, isqrt(p//2)+1):
        a = isqrt(p-2*b*b)
        if a*a+2*b*b == p:
            return a, b
    return None


def remove_support(target, product):
    divisor = common_divisor(target, product)
    while divisor != 1:
        target //= divisor
        divisor = common_divisor(target, divisor)
    return target


def full_packet(n):
    target = denominator(n)
    for p in prime_divisors(n):
        m = n//p
        generator = split_generator(p)
        if generator is None:
            divisor = denominator(m)
        else:
            a, b = generator
            divisor = norm_denominator(m*a, m*b)
        target = remove_support(target, divisor)
    return target


SIEVE_ROOTS = [
    (p, next((s for s in range(p) if (s*s+2) % p == 0), None))
    for p in range(3, 98, 2) if prime_divisors(p) == (p,)
]


def remove_small_norms(n, target):
    bound = n**4
    roots = [(p, s, pow(n, -1, p)) for p, s in SIEVE_ROOTS
             if n % p and p < 2*n*n+1]
    count = survivors = 0
    for b in range(1, isqrt(bound//2)//n+1):
        y_squared = 2*(n*b)**2
        radius = isqrt(bound-y_squared)
        lo, hi = -((radius+1)//n), (radius-1)//n
        length = hi-lo+1
        count += length
        keep = bytearray([1])*length
        for p, s, inv in roots:
            if s is None:
                if b % p:
                    continue
                classes = (-inv,)
            else:
                classes = (s*b-inv, -s*b-inv)
            for residue in classes:
                i = (residue-lo) % p
                if i < length:
                    keep[i::p] = bytes(1+(length-1-i)//p)
        values = [(1+n*a)**2+y_squared for a in compress(range(lo, hi+1), keep)]
        survivors += len(values)
        target = remove_support(target, Integer(prod(values)))
    return target, count, survivors


def all_primes(bound):
    sieve = bytearray([1])*(bound+1)
    sieve[:2] = b'\0\0'
    for p in range(2, isqrt(bound)+1):
        if sieve[p]:
            sieve[p*p::p] = bytes(1+(bound-p*p)//p)
    return list(compress(range(bound+1), sieve))


def independent_check(n, target, value, primes):
    trial = target
    for p in primes:
        if p > n**4:
            break
        while trial % p == 0:
            trial //= p
    assert trial == value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--odd-limit', type=int, default=509)
    parser.add_argument('--prime-limit', type=int, default=1009)
    parser.add_argument('--direct-limit', type=int, default=35)
    args = parser.parse_args()
    upper = max(args.odd_limit, args.prime_limit)
    primes = all_primes(max(2, min(upper, args.direct_limit))**4)
    writer = csv.writer(sys.stdout, lineterminator='\n')
    writer.writerow(['n', 'B_bits', 'full_bits', 'residual_bits', 'small_full_part',
                     'norm_pairs', 'pairs_after_sieve', 'residual_is_square'])
    for n in range(3, upper+1, 2):
        if n > args.odd_limit and prime_divisors(n) != (n,):
            continue
        packet = full_packet(n)
        residual, count, survivors = remove_small_norms(n, packet)
        if n <= args.direct_limit:
            independent_check(n, packet, residual, primes)
        square = int(integer_sqrt(residual)**2 == residual)
        if 7 <= n <= 509 or (7 <= n <= 1009 and prime_divisors(n) == (n,)):
            assert residual > 1 and not square
            floor_log2 = residual.bit_length()-1
            assert 100*floor_log2 >= 35*denominator(n).bit_length()
            assert 100*floor_log2 >= 85*packet.bit_length()
        writer.writerow([n, denominator(n).bit_length(), packet.bit_length(),
                         residual.bit_length(), packet//residual, count, survivors, square])
        sys.stdout.flush()


if __name__ == '__main__':
    main()

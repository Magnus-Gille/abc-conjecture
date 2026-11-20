"""Verify the odd-index squarefree-support classification at 10**7.

Python standard library. The optional positional argument is the prime cutoff.
The terminal-divisor assertions are for the default cutoff.
"""

from array import array
from collections import defaultdict
from fractions import Fraction
from functools import cache
from math import isqrt, prod
import sys


def largest_prime_factors(limit):
    factors = array("I", [0]) * (limit + 1)
    for p in range(2, limit + 1):
        if not factors[p]:
            count = (limit - p) // p + 1
            factors[p::p] = array("I", [p]) * count
    return factors


def odd_prime_divisors_above_three(n, factors):
    while n > 1:
        q = factors[n]
        if q < 5:
            break
        yield q
        while n % q == 0:
            n //= q


def division_values(modulus):
    # psi_1, ..., psi_4 at (-8,16) on y^2 = x^3+16x^2+32x.
    x, y = -8, 16
    b2, b4, b8 = 64, 64, -1024
    w2 = 2*y
    w3 = (3*x**4+b2*x**3+3*b4*x*x+b8) % modulus
    w4 = w2*(2*x**6+b2*x**5+5*b4*x**4+10*b8*x*x+b2*b8*x+b4*b8) % modulus
    inverse = pow(w2, -1, modulus)

    @cache
    def w(n):
        if n <= 4:
            return (0, 1, w2, w3, w4)[n] % modulus
        k = n//2
        if n % 2:
            return (w(k+2)*w(k)**3-w(k-1)*w(k+1)**3) % modulus
        return w(k)*inverse*(w(k+2)*w(k-1)**2-w(k-2)*w(k+1)**2) % modulus

    return w


def small_prime_orders(bound, factors):
    buckets = defaultdict(list)
    for a in range(1, isqrt(bound)+1, 2):
        for b in range(1, isqrt((bound-a*a)//2)+1):
            p = a*a+2*b*b
            if factors[p] != p:
                continue
            candidates = set(odd_prime_divisors_above_three(p+1-2*a, factors))
            candidates.update(odd_prime_divisors_above_three(p+1+2*a, factors))
            w = division_values(p)
            for q in candidates:
                if w(q) == 0:
                    assert division_values(p*p)(q) != 0, (p, q)
                    buckets[q].append(p)
                    break
            w.cache_clear()
    return buckets


def pass_character_tests(buckets, factors):
    possible = {q: prod(ps) for q, ps in buckets.items()}
    eliminated = []
    # At auxiliary primes 1 mod 8, both -1 and 2 are squares, so no
    # division-polynomial sign or dyadic normalization formula is needed.
    for aux in range(17, min(len(factors), 4001), 8):
        if factors[aux] != aux:
            continue
        w = division_values(aux)
        for q, small_class in list(possible.items()):
            if pow(w(q)*small_class % aux, (aux-1)//2, aux) == aux-1:
                del possible[q]
                eliminated.append(aux)
        w.cache_clear()
    return possible, max(eliminated, default=0)


@cache
def multiple(n):
    if n == 1:
        return Fraction(-8), Fraction(16)
    if n % 2:
        x, y = multiple(n-1)
        u, v = multiple(1)
        slope = (v-y)/(u-x)
    else:
        x, y = multiple(n//2)
        u = x
        slope = (3*x*x+32*x+32)/(2*y)
    z = slope*slope-16-x-u
    return z, slope*(x-z)-y


def stripped_denominator(n, primes):
    x, _ = multiple(n)
    B = isqrt(x.denominator)
    assert B*B == x.denominator
    residual = B
    small_class = 1
    for p in primes:
        if p > residual:
            break
        e = 0
        while residual % p == 0:
            residual //= p
            e += 1
        if e % 2:
            small_class *= p
    return small_class, residual


def main(bound):
    # CM extends the prime sieve by at most the Hasse radius.
    factors = largest_prime_factors(max(4000, bound+1+2*isqrt(bound)+2))
    buckets = small_prime_orders(bound, factors)
    small_primes = [p for p in range(2, bound+1) if factors[p] == p]
    hits = [p for ps in buckets.values() for p in ps]
    assert len(hits) == len(set(hits))
    survivors, largest_test = pass_character_tests(buckets, factors)
    print('Prime indices, small primes, largest prime index, largest auxiliary prime:',
          len(buckets), len(hits), max(buckets), largest_test)
    print('Prime-index surviving squareclasses:', dict(sorted(survivors.items())))
    if bound != 10**7:
        return
    assert len(buckets) == 22716 and len(hits) == 24813
    assert max(buckets) == 4999529 and largest_test == 433
    assert survivors == {5: 281, 7: 117041, 11: 2797478818681}
    exceptions = {1: 1, 3: 1, 5: 281, 7: 117041, 9: 29651721, 11: 2797478818681}
    for n in (1, 3, 5, 7, 9, 11, 15, 21, 25, 27, 33, 35, 49, 55, 77, 121):
        small_class, residual = stripped_denominator(n, small_primes)
        print(n, small_class, residual.bit_length(), isqrt(residual)**2 == residual)
        if n in exceptions:
            assert residual == 1 and small_class == exceptions[n]
        else:
            assert isqrt(residual)**2 != residual
    points = [(1, 1, 0, 1), (1, 2, 1, 3), (281, 5, 18, 1),
              (117041, 155, 252, 1), (29651721, -10819, 7868, 3),
              (2797478818681, -1853539, 429930, 1)]
    for d, m, n, w in points:
        for u, v in [(m, n), (-n, m)]:
            quartic = u**4+4*u**3*v+10*u*u*v*v-4*u*v**3+v**4
            assert quartic == d*d*w**4


if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 10**7)

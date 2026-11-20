"""Check the finite arithmetic in the signed CM Frobenius prime bounds."""
from functools import cache
from itertools import product
from math import gcd, isqrt

from abc_octic_mixed_simple_density import division_at_r0


def multiply(left, right, real_mod, imag_mod):
    a, b = left
    c, d = right
    return (a*c-2*b*d) % real_mod, (a*d+b*c) % imag_mod


def character(z):
    a, b = z
    return (a % 8 in (1, 3)) == (b % 4 == 0)


def check_frobenius():
    units = tuple(product(range(1, 8, 2), range(4)))
    mul = lambda u, v: multiply(u, v, 8, 4)
    gens = [(7, 0), (1, 1), (3, 2)]
    assert all(not character(g) for g in gens)
    assert all(character(mul(u, v)) == (character(u) == character(v))
               for u, v in product(units, repeat=2))
    generated = {(1, 0)}
    while len(generated) < len(units):
        extra = {mul(u, g) for u in generated for g in gens} - generated
        assert extra
        generated.update(extra)
    for p, trace in [(3, -2), (17, -6)]:
        squares = {i*i % p for i in range(1, p)}
        values = [x*(x*x+4*x+2) % p for x in range(p)]
        assert trace == -sum(0 if y == 0 else 1 if y in squares else -1
                             for y in values)


def check_twisted_ward(modulus, period):
    mul = lambda u, v: multiply(u, v, modulus, modulus)
    def sub(u, v):
        return ((u[0]-v[0]) % modulus, (u[1]-v[1]) % modulus)
    def recurrence(seq, n):
        k = n//2
        if n % 2:
            left = mul(mul(seq(k), seq(k)), mul(seq(k+2), seq(k)))
            right = mul(mul(seq(k+1), seq(k+1)), mul(seq(k-1), seq(k+1)))
            if k % 2:
                right = mul((16, 0), right)
            else:
                left = mul((16, 0), left)
            return sub(left, right)
        left = mul(seq(k+2), mul(seq(k-1), seq(k-1)))
        right = mul(seq(k-2), mul(seq(k+1), seq(k+1)))
        return mul(seq(k), sub(left, right))
    @cache
    def seq(n):
        if n <= 4:
            return [(0, 0), (1, 0), (1, 0), (-1 % modulus, -2 % modulus),
                    (2, 0)][n]
        return recurrence(seq, n)
    cyclic = lambda n: seq(n % period)
    for n in range(4*period):
        assert cyclic(n) == recurrence(cyclic, n)
    for n in range(13, 13+24*period, 24):
        a, b = cyclic(n)
        if modulus == 3:
            assert (a, b) == (1, 0)
        else:
            assert a == 1 and b % 4 == 2


def check_scalar_ward():
    modulus = 27
    w = division_at_r0(modulus)
    cyclic = lambda n: w(n % modulus) % modulus
    for k in range(modulus):
        assert (cyclic(2*k+1)-cyclic(k+2)*cyclic(k)**3
                +cyclic(k-1)*cyclic(k+1)**3) % modulus == 0
        assert (32*cyclic(2*k)-cyclic(k)*(cyclic(k+2)*cyclic(k-1)**2
                -cyclic(k-2)*cyclic(k+1)**2)) % modulus == 0
    for n in range(1, 216, 2):
        if gcd(n, 3) == 1:
            assert n*cyclic(n)*pow(2, -5*((n*n-1)//4), modulus) % modulus == 1


def candidates(r, limit):
    forms = []
    for a in range(-isqrt(limit), isqrt(limit)+1):
        for b in range(1, isqrt(limit//2)+1):
            c = a*a+2*b*b
            if c > limit:
                continue
            real, imag = 1+r*a, r*b
            if real % 2 == 0 or not character((real, imag)):
                continue
            if b % 2 == 0 and real % 8 not in (1, 7):
                continue
            if (real*real+2*imag*imag) % 3:
                forms.append((c, 2*a, b))
    return sorted(forms)


def check_bounds():
    assert candidates(5, 16) == [(6, -4, 1), (12, -4, 2)]
    assert candidates(13, 56) == [(18, -8, 1), (22, -4, 3),
                                  (34, 8, 3), (54, 12, 3)]
    for r, p, residue in [(149, 132611, 14816), (733, 9665339, 4109457)]:
        for v in (r, p):
            assert all(v % i for i in range(2, isqrt(v)+1))
        assert division_at_r0(p*p)(r) == p*residue
        assert p == (6*r*r-4*r+1 if r % 24 == 5 else 18*r*r-8*r+1)


if __name__ == '__main__':
    check_frobenius()
    check_twisted_ward(3, 12)
    check_twisted_ward(8, 16)
    check_scalar_ward()
    check_bounds()
    print('Verified the character, Ward periods, allowed norms, and simple divisors.')

"""Exact checks for the whole abc triple and its Pell parameters."""

from fractions import Fraction
from math import gcd, isqrt

from abc_cm_twist_depth_example import add, degree_eleven_factors


def multiple_abscissa(a, b):
    s = b*b + 2*a*a
    h = s + 2*a*b
    j = b*b - 2*a*a
    twist = s*h
    base = (Fraction(-8*h*h), Fraction(16*h*h*j))
    twice = add(base, base, twist)
    fourth = add(twice, twice, twist)
    fifth = add(fourth, base, twist)
    eleventh = add(add(fifth, fifth, twist), base, twist)
    return eleventh[0]/twist


def exact_square(n):
    root = isqrt(n)
    assert root*root == n
    return root


def example():
    p = 683
    a, b = -6437, 73
    z = multiple_abscissa(a, b)
    u, v = z.numerator, z.denominator
    h = u*u + 16*u*v + 32*v*v
    raw_a, raw_c = h*h, 1024*v**4
    raw_b = -u*(u+16*v)*(u+8*v)**2
    assert raw_a + raw_b == raw_c and raw_a > 0 and raw_b > 0
    g = gcd(raw_a, raw_c)
    assert g == 1024
    c = raw_c//g
    assert c % p**16 == 0 and c % p**17 != 0
    assert len(str(c)) == 3931

    su, sv = 163870930, 9208363
    assert (-u) % su == 0 and v % sv == 0 and (-h) % 2 == 0
    l = exact_square((-u)//su)
    m = exact_square(v//sv)
    w = exact_square((-h)//2)
    support = 2*su*sv*l*m*w*abs(u+8*v)*abs(u+16*v)
    saving = 2**11 * 199 * 683 * 9103
    assert gcd(199*683*9103, 2) == 1
    for prime, exponent in ((2, 12), (199, 2), (683, 2), (9103, 2)):
        assert all(prime % d for d in range(2, isqrt(prime)+1))
        assert support % prime**exponent == 0
        assert support % prime**(exponent+1) != 0
    assert (10**10*c*saving)//support == 2952658019718

    s = b*b + 2*a*a
    h0 = s + 2*a*b
    x = -8*h0*pow(s, -1, p**3) % p**3
    proper, full = degree_eleven_factors()
    assert evaluate(proper, x, p) != 0
    assert evaluate(full, x, p**3) == 316*p*p
    print("3931 digits, exact selected denominator exponent 2,",
          "exact exponent in c 16, c/rad(abc) >= 295.2658019718")


def evaluate(coeff, x, modulus):
    value = 0
    for c in coeff:
        value = (value*x + c) % modulus
    return value


def pell(n, modulus):
    def multiply(v, w):
        return ((v[0]*w[0] + 2*v[1]*w[1]) % modulus,
                (v[0]*w[1] + v[1]*w[0]) % modulus)
    value, power = (1, 0), (1, 1)
    while n:
        if n % 2:
            value = multiply(value, power)
        power = multiply(power, power)
        n //= 2
    return value


def pell_example():
    p = 683
    _, full = degree_eleven_factors()
    assert pell(228, p*p) == (p*p-1, 59*p)
    for n, power, result in ((73, 2, 148*p), (1213, 3, 671*p*p)):
        modulus = p**power
        b, a = pell(n, modulus)
        s = b*b + 2*a*a
        x = -8*(s+2*a*b)*pow(s, -1, modulus) % modulus
        assert evaluate(full, x, modulus) == result
    print("Pell indices 73 and 1213 have full exponents 1 and 2 at 683")


if __name__ == "__main__":
    example()
    pell_example()

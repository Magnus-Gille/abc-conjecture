"""Check the first repeated full prime on a small integer parameter by two methods."""

from fractions import Fraction
from math import isqrt

from sympy import Poly, factor_list, symbols


def degree_eleven_factors():
    x = symbols("x")
    cubic = Poly(x**3 + 16*x**2 + 32*x, x)
    # For even n use psi_n/(2y). Standard recurrences for n=5,6,7,11.
    third = Poly(3*x**4 + 64*x**3 + 192*x**2 - 1024, x)
    fourth = Poly(2*x**6 + 64*x**5 + 320*x**4 - 10240*x**2 - 65536*x - 65536, x)
    fifth = (4*cubic)**2 * fourth - third**3
    sixth = third * (fifth - fourth**2)
    seventh = fifth * third**3 - (4*cubic)**2 * fourth**3
    eleventh = seventh * fifth**3 - (4*cubic)**2 * fourth * sixth**3
    factors = sorted(factor_list(eleventh)[1], key=lambda item: item[0].degree())
    assert [(factor.degree(), e) for factor, e in factors] == [(10, 1), (50, 1)]
    return [[int(c) for c in factor.all_coeffs()] for factor, _ in factors]


def residue(coefficients, k, modulus):
    s = 2*k*k + 1
    t = -8*(s + 2*k)*pow(s, -1, modulus) % modulus
    value = 0
    for c in coefficients:
        value = (value*t + c) % modulus
    return value


def add(left, right, twist):
    if left is None or right is None:
        return right if left is None else left
    x, y = left
    u, v = right
    if x == u and y == -v:
        return None
    if left == right:
        slope = (3*x*x + 32*twist*x + 32*twist*twist)/(2*y)
    else:
        slope = (v-y)/(u-x)
    new_x = slope*slope - 16*twist - x - u
    return new_x, slope*(x - new_x) - y


def check():
    p = 683
    proper, full = degree_eleven_factors()
    lifts = []
    for k in range(p):
        if (2*k*k + 1) % p == 0 or residue(full, k, p):
            continue
        value = residue(full, k, p*p) // p
        derivative = residue(full, k+p, p*p) // p - value
        lifts.append(k + p*((-value * pow(derivative, -1, p)) % p))
    assert len(lifts) == 100
    k = min(lifts)
    assert k == 3872 and residue(proper, k, p)
    assert residue(full, k, p**3) == 382*p*p
    s, h, j = 2*k*k + 1, 2*k*k + 2*k + 1, 1 - 2*k*k
    twist = s*h
    base = Fraction(-8*h*h), Fraction(16*h*h*j)
    x, y = base
    assert y*y == x**3 + 16*twist*x*x + 32*twist*twist*x
    point = None
    for _ in range(11):
        point = add(point, base, twist)
    den = point[0].denominator
    b = isqrt(den)
    assert b*b == den and b % (p*p) == 0 and b % (p**3) != 0
    print("parameter", k, "prime", p, "exponent", 2, "full residues", len(lifts))


if __name__ == "__main__":
    check()

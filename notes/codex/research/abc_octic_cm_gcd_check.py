"""Exact gcd checks for U_N on the j=8000 CM orbit. Uses only the standard library."""

from fractions import Fraction
from functools import cache
from math import gcd, isqrt, lcm


def add(left, right, a, b):
    if left is None:
        return right
    if right is None:
        return left
    x, y = left
    u, v = right
    if x == u:
        if y == -v:
            return None
        slope = (3*x*x + 2*a*x + b) / (2*y)
    else:
        slope = (v-y) / (u-x)
    z = slope*slope-a-u-x
    return z, slope*(x-z)-y


def multiple(n, point, a, b):
    base = tuple(map(Fraction, point))
    if n < 0:
        n, base = -n, (base[0], -base[1])
    result = None
    while n:
        if n % 2:
            result = add(result, base, a, b)
        n //= 2
        if n:
            base = add(base, base, a, b)
    return result


@cache
def U(n):
    x, y = multiple((n+1)//2, (1, 1), -8, 8)
    s, t = ((x+y)/(2*(x-1))).as_integer_ratio()
    return (s+t)**2+t*t


@cache
def multiple_s(n):
    return multiple(n, (-4, -8), 16, 32)


def ideal_gcd(left, right):
    """Norm-Euclidean gcd for coefficient pairs in Z[sqrt(-2)]."""
    a, b = left
    c, d = right
    while c or d:
        norm = c*c + 2*d*d
        q = round(Fraction(a*c + 2*b*d, norm))
        r = round(Fraction(b*c - a*d, norm))
        a, b, c, d = c, d, a-q*c+2*r*d, b-r*c-q*d
    return (a, b) if (a, b) > (0, 0) else (-a, -b)


@cache
def D(a, b):
    """Odd norm of sqrt(denom ideal x([a+b*tau]S)). All inputs have a odd."""
    x, y = multiple_s(a)
    if not b:
        real, imaginary = x, Fraction(0)
    else:
        u, v = multiple_s(b)
        # Rational 2-isogeny followed by the isomorphism via tau²=-2.
        u, c = -(u+16+32/u)/2, v*(1-32/u**2)/4
        # The second summand is (u,c*tau). Its abscissa is distinct from x.
        real = (y*y-2*c*c)/(u-x)**2-16-x-u
        imaginary = -2*y*c/(u-x)**2
    w = lcm(real.denominator, imaginary.denominator)
    u, v = int(real*w), int(imaginary*w)
    assert gcd(w, gcd(u, v)) == 1
    # The ideal (u+v*tau,w) has index gcd(u²+2v²,w*u,w*v,w²).
    denom_norm = w*w // gcd(u*u+2*v*v, w)
    d = isqrt(denom_norm)
    assert d*d == denom_norm
    return d // (d & -d)


def check(n, m):
    left = ideal_gcd((n, -1), (m, -1))
    right = ideal_gcd((n, -1), (m, 1))
    g = gcd(n*n+2, n-m), gcd(n*n+2, n+m)
    assert tuple(a*a+2*b*b for a, b in (left, right)) == g
    factors = D(*left), D(*right)
    assert gcd(*factors) == 1
    assert gcd(U(n), U(m)) == factors[0]*factors[1]
    return g, factors


if __name__ == '__main__':
    indices = list(range(3, 64, 2))
    for n in indices:
        assert U(n) == D(n, -1)
        for m in indices:
            if m < n:
                check(n, m)
    for n, m in [(19, 3), (25, 3), (63, 25), (85, 41), (95, 23), (113, 59)]:
        norms, factors = check(n, m)
        print(f'{n:3} {m:3} | {norms} | {factors} | {factors[0]*factors[1]}')
    norms, factors = check(481, 257)
    assert norms == (1, 369)
    assert factors[1] % 41**3 == 20*41**2
    assert U(481) % 41**2 == U(257) % 41**2 == 0
    print('At (481,257), the conjugate factor D(13-10*tau) has exact 41-adic valuation two.')
    print(f'All {len(indices)*(len(indices)-1)//2} pairs with 3 <= m < n <= 63 passed.')

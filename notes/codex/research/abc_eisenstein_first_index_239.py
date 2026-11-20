"""Verify a first-index quartic square and a whole-radical certificate."""

from math import gcd


def quadratic_power(a, b, discriminand, exponent):
    """Power of a+b*sqrt(discriminand), using integer coordinates."""
    x, y = 1, 0
    while exponent:
        if exponent & 1:
            x, y = x*a + discriminand*y*b, x*b + y*a
        a, b = a*a + discriminand*b*b, 2*a*b
        exponent //= 2
    return x, y


def check():
    prime = 239
    s, t = quadratic_power(7, 2, -1, 2079)
    assert gcd(s, t) == 1 and t % 2 == 0 and s*s + t*t == 53**2079
    x, y = s**4 - t**4//2, t**4//2
    assert min(x, y) > 0 and gcd(x, y) == 1
    w = x*x + 3*y*y
    u, v = quadratic_power(x, y, -3, 12)
    height = w**12
    assert u*u + 3*v*v == height and gcd(u, v) == 1 and v % 24 == 0
    assert 10**172062 <= height < 10**172063

    f0 = x**4 - 18*x*x*y*y + 9*y**4
    difference = 12*x*y*(x*x - 3*y*y)
    f_plus = f0 + difference
    assert f_plus % prime**3 == 105*prime**2
    assert (f0 - difference) % prime == 116 and f0 % prime == 58
    assert u == f0*f_plus*(f0 - difference)

    product, remainder = divmod(3*abs(u*v)*w, abs(s*t)**3)
    assert remainder == 0 and product % abs(s*t) == 0
    assert product % (53**2079 * prime**2) == 0
    known_excess = 53**2078 * prime
    assert 10**8 * height * known_excess // product == 333477463
    print("172063 digits; v_239(F_+)=2; C/rad(3UVW) >= 3.33477463")


if __name__ == "__main__":
    check()

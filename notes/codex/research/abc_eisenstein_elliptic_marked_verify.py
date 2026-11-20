"""Verify the finite calculations for the independent Eisenstein elliptic marks."""
from fractions import Fraction
from math import isqrt


def primes(limit):
    for n in range(2, limit + 1):
        if all(n % m for m in range(2, isqrt(n) + 1)):
            yield n


def add(p, coefficient, left, right):
    if left is None:
        return right
    if right is None:
        return left
    x, y = left
    u, v = right
    if x == u and (y + v) % p == 0:
        return None
    if x == u:
        slope = (3*x*x + coefficient) * pow(2*y, -1, p) % p
    else:
        slope = (v-y) * pow(u-x, -1, p) % p
    w = (slope*slope-x-u) % p
    return w, (slope*(x-w)-y) % p


def multiply(p, coefficient, n, pt):
    total = None
    while n:
        if n % 2:
            total = add(p, coefficient, total, pt)
        pt = add(p, coefficient, pt, pt)
        n //= 2
    return total


def field_size(p, coefficient):
    squares = {(x*x) % p for x in range(1, p)}
    total = 1
    for x in range(p):
        rhs = x * (x*x + coefficient) % p
        total += 1 if not rhs else 2 if rhs in squares else 0
    return total


def test_kummer():
    expected = {
        313: (288, (256, 290), (12, 42)),
        1201: (1152, None, (803, 258)),
    }
    for p, (n, result_a, result_b) in expected.items():
        assert p % 24 == 1 and pow(3, (p-1)//4, p) == 1
        assert all(field_size(p, d)==n for d in (1, 3, 9))
        a = 9*pow(4,-1,p)%p, 45*pow(8,-1,p)%p
        b = 1, 2
        assert multiply(p, 9, n//9, a) == result_a
        assert multiply(p, 3, n//9, b) == result_b


def test_local_marks(limit=2000):
    for p in primes(limit):
        if p < 5:
            continue
        squares = {(x*x)%p for x in range(1,p)}
        count = 0
        for r in range(p):
            f0 = (r**4-18*r*r+9) % p
            cross = 12*r*(r*r-3) % p
            if (f0-cross)*(f0+cross)%p:
                continue
            rhs = -f0*pow(2,-1,p)%p
            assert rhs
            count += 2*int(rhs in squares)
        predicted = 8 if p%24==23 else 16 if p%24==1 and pow(3,(p-1)//4,p)==1 else 0
        assert count == predicted, (p, count, predicted)


def test_numerators():
    assert Fraction(45,8)**2 == Fraction(9,4)**3 + 9*Fraction(9,4)
    assert Fraction(7,8)**2 == Fraction(1,4)**3 + 3*Fraction(1,4)
    assert Fraction(3,16)-Fraction(40,81*32)-Fraction(1,36)==Fraction(187,1296)


if __name__ == "__main__":
    test_kummer()
    test_local_marks()
    test_numerators()
    print("Verified the Kummer witnesses, twist points, density arithmetic, and all local counts through 2000.")

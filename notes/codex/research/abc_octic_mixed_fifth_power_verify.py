"""Verify the finite calculations for 6 y^2 = 1 - x^5, using Python 3."""

from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import gcd


# Units of Z_2[zeta_5] modulo squares. Coefficients are in ascending order.
def cyclotomic_product(a, b):
    terms = [0] * 7
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            terms[i + j] += x * y
    for i in range(6, 3, -1):
        for j in range(i - 4, i):
            terms[j] -= terms[i]
    return tuple(v % 8 for v in terms[:4])


unit_squares = {
    cyclotomic_product(u, u)
    for u in product(range(8), repeat=4)
    if any(v % 2 for v in u)
}


@lru_cache(None)
def unit_class(u):
    return min(cyclotomic_product(u, s) for s in unit_squares)


def dyadic_class(a):
    v = min((abs(x) & -abs(x)).bit_length() - 1 for x in a if x)
    return v % 2, unit_class(tuple((x // 2**v) % 8 for x in a))


def class_product(a, b):
    return a[0] ^ b[0], unit_class(cyclotomic_product(a[1], b[1]))


def check_descent():
    one = dyadic_class((1, 0, 0, 0))
    local_inputs = [(-6, 6, 0, 0), (1, 6, 0, 0), (-2, 6, 0, 0)]
    local = {one}
    for u in local_inputs:
        value = dyadic_class(u)
        local |= {class_product(v, value) for v in local}
    assert len(unit_squares) == 120 and len(local) == 8
    basis = [(-1, 0, 0, 0), (0, 0, -1, -1), (2, 0, 0, 0),
             (3, 0, 0, 0), (1, -1, 0, 0)]
    accepted = []
    for a, c, d in product(range(2), repeat=3):
        bits = (a, c ^ d, c, d, d)
        value = one
        for use, generator in zip(bits, basis):
            if use:
                value = class_product(value, dyadic_class(generator))
        if value in local:
            accepted.append(bits)
    expected = [(0, 0, 0, 0, 0), (0, 1, 1, 0, 0), (1, 1, 0, 1, 1),
                (1, 0, 1, 1, 1)]
    assert accepted == expected
    assert dyadic_class(local_inputs[2]) not in {one, dyadic_class(local_inputs[0])}
    print("2-adic local generators:", [dyadic_class(u) for u in local_inputs])
    print("Surviving global classes:", accepted)


# Cantor arithmetic in the odd-degree model y^2=x^5+6^5.
# Each polynomial is a tuple of ascending coefficients, over Q or F_p.
class Jacobian:
    def __init__(self, prime=None):
        self.prime = prime
        self.f = self.poly((6**5, 0, 0, 0, 0, 1))
        self.one = self.poly((1,))
        self.zero = ()
        self.identity = self.one, self.zero

    def coeff(self, x):
        return x % self.prime if self.prime else Fraction(x)

    def inv(self, x):
        return pow(x, -1, self.prime) if self.prime else 1 / x

    def poly(self, raw):
        a = [self.coeff(x) for x in raw]
        while a and not a[-1]:
            a.pop()
        return tuple(a)

    def scale(self, a, c):
        return self.poly(x * c for x in a)

    def plus(self, a, b):
        terms = [0] * max(len(a), len(b))
        for v in (a, b):
            for j, x in enumerate(v):
                terms[j] += x
        return self.poly(terms)

    def minus(self, a, b):
        return self.plus(a, self.scale(b, -1))

    def times(self, a, b):
        if not a or not b:
            return ()
        terms = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                terms[i + j] += x * y
        return self.poly(terms)

    def divrem(self, a, b):
        assert b
        quot = [0] * max(0, len(a) - len(b) + 1)
        while len(a) >= len(b):
            i = len(a) - len(b)
            c = self.coeff(a[-1] * self.inv(b[-1]))
            quot[i] = c
            a = self.minus(a, (0,) * i + self.scale(b, c))
        return self.poly(quot), a

    def exact(self, a, b):
        q, r = self.divrem(a, b)
        assert not r
        return q

    def monic(self, a):
        return self.scale(a, self.inv(a[-1]))

    def bezout(self, a, b):
        u, v, w, z = self.one, (), (), self.one
        while b:
            q, r = self.divrem(a, b)
            a, b = b, r
            u, w = w, self.minus(u, self.times(q, w))
            v, z = z, self.minus(v, self.times(q, z))
        c = self.inv(a[-1])
        return self.scale(u, c), self.scale(v, c), self.scale(a, c)

    def point(self, x, y):
        return self.poly((-x, 1)), self.poly((y,))

    def add(self, left, right):
        u, v = left
        a, b = right
        v1, v2, d1 = self.bezout(u, a)
        w1, w2, d = self.bezout(d1, self.plus(v, b))
        h = self.monic(self.exact(self.times(u, a), self.times(d, d)))
        first = self.times(v1, self.times(u, b))
        second = self.times(v2, self.times(a, v))
        total = self.plus(self.times(w1, self.plus(first, second)),
                          self.times(w2, self.plus(self.times(v, b), self.f)))
        k = self.divrem(self.exact(total, d), h)[1]
        while len(h) > 3:
            h = self.monic(self.exact(self.minus(self.f, self.times(k, k)), h))
            k = self.divrem(self.scale(k, -1), h)[1]
        assert not self.divrem(self.minus(self.f, self.times(k, k)), h)[1]
        return h, k


def point_counts(p):
    chi = [0] + [1 if pow(i, (p - 1) // 2, p) == 1 else -1 for i in range(1, p)]
    nonsquare = chi.index(-1)
    n1 = p + 1 + sum(chi[(x**5 + 6**5) % p] for x in range(p))
    n2 = p * p + 1
    for a, b in product(range(p), repeat=2):
        u, v = 1, 0
        for _ in range(5):
            u, v = (u * a + nonsquare * v * b) % p, (v * a + u * b) % p
        u += 6**5
        n2 += chi[(u * u - nonsquare * v * v) % p]
    return n1, n2, (n1 * n1 + n2) // 2 - p


def check_reductions():
    for p, counts in [(7, (8, 50, 50)), (11, (16, 118, 176)),
                      (13, (14, 170, 170)), (19, (20, 438, 400))]:
        assert point_counts(p) == counts
        print("Point counts:", p, counts)
    assert gcd(50, 176) == 2
    for p, order in [(13, 85), (19, 10)]:
        j = Jacobian(p)
        p0, t0 = j.point(-2, 88), j.point(-6, 0)
        cyclic = {j.identity}
        q = p0
        while q != j.identity:
            assert q not in cyclic
            cyclic.add(q)
            q = j.add(q, p0)
        assert len(cyclic) == order
        if p == 19:
            subgroup = cyclic | {j.add(z, t0) for z in cyclic}
            found = [(x, y) for x, y in product(range(p), repeat=2)
                     if (y*y-x**5-6**5) % p == 0 and j.point(x, y) in subgroup]
            assert len(subgroup) == 20 and found == [(13, 0), (17, 7), (17, 12)]
            print("Affine disks at 19:", found)


def check_tangent():
    j = Jacobian()
    p0, t0 = j.point(-2, 88), j.point(-6, 0)
    u, v = t0
    for _ in range(11):
        u, v = j.add((u, v), p0)
    p = 19
    def residue(a):
        return a.numerator * pow(a.denominator, -1, p*p) % (p*p)
    u19, v19 = [list(map(residue, g)) for g in (u, v)]
    assert u19 == [240, 46, 1] and v19 == [18, 212]
    xp, = [i for i in range(p*p) if (i+2) % p == 0
           and sum(c*i**k for k, c in enumerate(u19)) % (p*p) == 0]
    yt = (v19[0] - 6*v19[1]) % (p*p)
    assert xp == 321 and yt == 190
    a = (xp + 2) // p * pow(176, -1, p) % p
    b = yt // p * pow(5*6**4, -1, p) % p
    logline = (a+b) % p, (-2*a-6*b) % p
    assert (a, b) == (11, 10) and logline == (2, 13)
    print("Mumford mod 361:", u19, v19, "log(10P)/19 mod 19:", logline)


if __name__ == "__main__":
    check_descent()
    check_reductions()
    check_tangent()

"""Verify the order and rank-lower-bound certificates for the genus-two quotient."""

from itertools import product
from math import comb, gcd


# Coefficients in ascending powers, in all polynomial calculations.
SEXTIC = (512, 512, 192, 0, 24, -8, 1)


def point_counts(p):
    squares = {u * u % p for u in range(1, p)}
    nonsquare = next(u for u in range(1, p) if u not in squares)

    def character(value):
        residue = value % p
        return 0 if not residue else (1 if residue in squares else -1)

    def evaluate(a, b):
        u, v = 0, 0
        for coefficient in reversed(SEXTIC):
            u, v = (a * u + nonsquare * b * v + coefficient) % p, (b * u + a * v) % p
        return u, v

    n1 = p + 2 + sum(character(evaluate(a, 0)[0]) for a in range(p))
    n2 = p * p + 2
    for a, b in product(range(p), repeat=2):
        u, v = evaluate(a, b)
        n2 += character(u * u - nonsquare * v * v)
    return n1, n2


def verify_reduction(p, branch, group_order, ratio):
    """Cantor arithmetic after x=1/(z-branch), y=W/(z-branch)^3."""
    one, zero = (1,), ()
    identity = one, zero

    def poly(coefficients):
        values = [c % p for c in coefficients]
        while values and not values[-1]:
            values.pop()
        return tuple(values)

    def plus(a, b):
        values = [0] * max(len(a), len(b))
        for c in (a, b):
            for j, v in enumerate(c):
                values[j] += v
        return poly(values)

    def scale(a, scalar):
        return poly(c * scalar for c in a)

    def minus(a, b):
        return plus(a, scale(b, -1))

    def times(a, b):
        if not a or not b:
            return zero
        values = [0] * (len(a) + len(b) - 1)
        for i, u in enumerate(a):
            for j, v in enumerate(b):
                values[i + j] += u * v
        return poly(values)

    def divrem(a, b):
        quotient = [0] * max(0, len(a) - len(b) + 1)
        while len(a) >= len(b):
            shift = len(a) - len(b)
            scalar = a[-1] * pow(b[-1], -1, p) % p
            quotient[shift] = scalar
            a = minus(a, (0,) * shift + scale(b, scalar))
        return poly(quotient), a

    def exact(a, b):
        q, r = divrem(a, b)
        assert not r
        return q

    def monic(a):
        return scale(a, pow(a[-1], -1, p))

    def bezout(a, b):
        u, v, uu, vv = one, zero, zero, one
        while b:
            q, r = divrem(a, b)
            a, b = b, r
            u, uu = uu, minus(u, times(q, uu))
            v, vv = vv, minus(v, times(q, vv))
        c = pow(a[-1], -1, p)
        return scale(u, c), scale(v, c), scale(a, c)

    # x^6 f(branch+1/x); the sextic term vanishes at the chosen branch.
    coefficients = [0] * 7
    for j, c in enumerate(SEXTIC):
        for k in range(j + 1):
            coefficients[6 - k] += c * comb(j, k) * branch ** (j - k)
    f = poly(coefficients)
    assert len(f) == 6

    def add(left, right):
        u1, v1 = left
        u2, v2 = right
        a, b, common = bezout(u1, u2)
        e, g, d = bezout(common, plus(v1, v2))
        u = monic(exact(times(u1, u2), times(d, d)))
        numerator = plus(
            times(e, plus(times(a, times(u1, v2)), times(b, times(u2, v1)))),
            times(g, plus(times(v1, v2), f)),
        )
        v = divrem(exact(numerator, d), u)[1]
        while len(u) > 3:
            u = monic(exact(minus(f, times(v, v)), u))
            v = divrem(scale(v, -1), u)[1]
        assert not divrem(minus(f, times(v, v)), u)[1]
        return u, v

    def multiply(n, point):
        result = identity
        while n:
            if n & 1:
                result = add(result, point)
            n //= 2
            if n:
                point = add(point, point)
        return result

    def point(x, y):
        return poly((-x, 1)), poly((y,))

    inf_plus, inf_minus = point(0, 1), point(0, -1)
    inv = pow(-1 - branch, -1, p)
    seed = point(inv, 15 * inv**3)
    # The transformed origin is the chosen Weierstrass point, so the two
    # original infinities represent negative classes.
    d_infinity = add(inf_plus, inf_plus)
    d_seed = add(seed, inf_minus)
    factor = group_order // 7
    u, v = multiply(factor, d_infinity), multiply(factor, d_seed)
    assert u != identity and multiply(7, u) == identity
    assert v == multiply(ratio, u)
    return u, v


if __name__ == "__main__":
    results = {}
    for p, expected in [(3, (4, 18)), (11, (12, 162)), (43, (44, 1986))]:
        n1, n2 = point_counts(p)
        assert (n1, n2) == expected
        results[p] = (n1 * n1 + n2) // 2 - p
        print(f"p={p}: #G(F_p)={n1}, #G(F_p^2)={n2}, #J(F_p)={results[p]}")
    assert gcd(results[3], results[11]) == 2
    for p, branch, ratio in [(3, 1, 3), (43, 11, 4)]:
        u, v = verify_reduction(p, branch, results[p], ratio)
        print(f"p={p}: projected D={u}, projected B={v}, B={ratio}D")

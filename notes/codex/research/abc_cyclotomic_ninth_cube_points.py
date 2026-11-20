"""Full two-descent and ramified 3-adic checks for the ninth cyclotomic cube.

Coefficient triples are in the integral basis 1,r,r^2 with r^3=3. The note
with the same basename derives the equations, local image sizes and generators.
Run directly with Python 3. All membership and congruence tests are exact.
"""

from fractions import Fraction
from functools import cache
from itertools import product


ONE = (1, 0, 0)
D = ((1, 0, 1), (0, 1, 0), (0, -2, 0))
EPSILON = (-2, 0, 1)
TAU = (1, 1, 1)


def add(x, y):
    return tuple(i + j for i, j in zip(x, y))


def scale(x, n):
    return tuple(n * i for i in x)


def sub(x, y):
    return add(x, scale(y, -1))


def mul(x, y):
    a, b, c = x
    d, e, f = y
    return a*d + 3*(b*f+c*e), a*e+b*d+3*c*f, a*f+b*e+c*d


def mod(x, n):
    return tuple(i % n for i in x)


def check_auxiliary_curve():
    counts = []
    for C in (ONE, EPSILON, TAU, mul(EPSILON, TAU)):
        values = {mod(mul(C, mul(v, v)), 8) for v in product(range(4), repeat=3)}
        survivors = [(a, d) for a, d in product(range(8), repeat=2)
                     if (a % 2 or d % 2) and mod((a, -3*d*d, 3*d*d), 8) in values]
        counts.append(len(survivors))
    assert counts == [8, 0, 0, 0]
    orders = [1 + sum((y*y-x**3-81*x-162) % p == 0
                      for x, y in product(range(p), repeat=2)) for p in (7, 13)]
    assert orders == [5, 13]
    print('Auxiliary classes mod 8 and reduction group orders', counts, orders)


def residue_product(x, y):
    # Modulo 8 in the unramified quadratic ring with w^2+w+1=0.
    a, b = x
    c, d = y
    return (a*c-b*d) % 8, (a*d+b*c-b*d) % 8


def quadratic_unit_classes():
    units = [x for x in product(range(8), repeat=2) if any(mod(x, 2))]
    squares = {residue_product(x, x) for x in units}
    classes = {}
    for x in units:
        if x not in classes:
            coset = [residue_product(x, y) for y in squares]
            classes.update((v, min(coset)) for v in coset)
    return classes


UNITS = quadratic_unit_classes()


@cache
def local_class(x, place):
    assert any(x)
    if place == 3:
        valuation = 0
        while x[0] % 3 == 0:
            x = (x[1], x[2], x[0] // 3)
            valuation += 1
        return valuation % 2, x[0] % 3

    # For the two places above 2 send r to r0 or r0*w, where r0 is
    # the odd rational 2-adic cube root of 3. Double precision as needed.
    bits = 6
    a, b, c = x
    while True:
        modulus = 2 ** bits
        r0 = pow(3, pow(3, -1, modulus), modulus)
        if place == 1:
            values = ((a + b*r0 + c*r0*r0) % modulus,)
        else:
            values = mod((a-c*r0*r0, b*r0-c*r0*r0), modulus)
        if any(values):
            valuation = min((v & -v).bit_length()-1 for v in values if v)
            if valuation + 3 <= bits:
                unit = mod(tuple(v // (2 ** valuation) for v in values), 8)
                return valuation % 2, unit if place == 1 else UNITS[unit]
        bits *= 2


def multiply_classes(x, y, place):
    a, u = x
    b, v = y
    if place == 3:
        unit = u*v % 3
    elif place == 1:
        unit = (u[0]*v[0] % 8,)
    else:
        unit = UNITS[residue_product(u, v)]
    return (a+b) % 2, unit


def local_image(place, abscissae):
    neutral = local_class(ONE, place)
    span = {(neutral, neutral)}
    for x in abscissae:
        factors = [add(x, d) for d in D]
        for i, factor in enumerate(factors):
            if not any(factor):
                factors[i] = mul(factors[(i+1) % 3], factors[(i+2) % 3])
                break
        assert local_class(mul(mul(factors[0], factors[1]), factors[2]), place) == neutral
        u, v = (local_class(factor, place) for factor in factors[:2])
        span |= {(multiply_classes(c, u, place), multiply_classes(d, v, place)) for c, d in span}
    return span


def check_rank():
    torsion_x = scale(D[0], -1)
    generators = {3: [torsion_x, (0, -2, -2)],
                  1: [torsion_x, (-2, -2, 2), (-2, -1, -1)],
                  2: [torsion_x, (-2, -1, 0), (-2, 0, -1), (-2, 1, 1)]}
    local = {place: local_image(place, xs) for place, xs in generators.items()}
    assert [len(local[v]) for v in (3, 1, 2)] == [4, 8, 16]
    global_generators = [(-1, 0, 0), EPSILON, (-1, 1, 0), TAU, (0, 1, 0)]
    classes = []
    for bits in product((0, 1), repeat=5):
        x = ONE
        for generator, bit in zip(global_generators, bits):
            if bit:
                x = mul(x, generator)
        classes.append((bits[0], {v: local_class(x, v) for v in local}))
    pairs = list(product(classes, repeat=2))
    counts = [len(pairs)]
    pairs = [(x, y) for x, y in pairs if x[0] == 0]  # First factor is positive.
    counts.append(len(pairs))
    for v in (3, 1, 2):
        pairs = [(x, y) for x, y in pairs if (x[1][v], y[1][v]) in local[v]]
        counts.append(len(pairs))
    assert counts == [1024, 512, 128, 32, 8]
    print('Full two-descent filtration', counts)


def divide(x, y):
    a, b, c = y
    adjugate = (a*a-3*b*c, 3*c*c-a*b, b*b-a*c)
    norm = mul(adjugate, y)
    assert norm[0] and norm[1:] == (0, 0)
    return scale(mul(x, adjugate), Fraction(1, norm[0]))


def check_tangent():
    B = add(add(D[0], D[1]), D[2])
    C = add(add(mul(D[0], D[1]), mul(D[0], D[2])), mul(D[1], D[2]))

    def add_points(first, second):
        x, y = first
        u, v = second
        if first == second:
            slope = divide(add(add(scale(mul(x, x), 3), scale(mul(B, x), 2)), C), scale(y, 2))
        else:
            slope = divide(sub(v, y), sub(u, x))
        new_x = sub(sub(sub(mul(slope, slope), B), x), u)
        return new_x, sub(mul(slope, sub(x, new_x)), y)

    p = ((0, -2, 0), (0, 2, -2))
    x, y = p
    factors = [add(x, d) for d in D]
    assert mul(y, y) == mul(mul(factors[0], factors[1]), factors[2])
    for _ in range(3):
        p = add_points(p, p)
    x, y = add_points(p, add_points(p, p))  # 24 times the original point.
    # Negative valuation of x puts the point in the formal group. Each
    # summand c_i*r^i has a distinct valuation modulo 3.
    def v3(integer):
        valuation = 0
        while integer % 3 == 0:
            integer //= 3
            valuation += 1
        return valuation
    assert min(3*(v3(c.numerator)-v3(c.denominator))+i for i, c in enumerate(x) if c) == -6
    direction = scale(divide(scale(x, -1), y), Fraction(1, 3))
    residues = tuple(c.numerator * pow(c.denominator, -1, 3) % 3 for c in direction)
    assert residues == (2, 0, 2)
    print('Leading residue of the formal parameter of 24P, divided by 3', residues)


if __name__ == '__main__':
    check_auxiliary_curve()
    check_rank()
    check_tangent()

"""Verify the least-kernel calculation for A^6 + A^3 B^3 + B^6.

Run with Python 3. Integer triples denote coefficients in 1,a,a^2, where
 a^3=3a-1. The accompanying note derives the global and local image sizes.
"""

from collections import Counter
from functools import cache
from itertools import product


ONE = (1, 0, 0)
A = (0, 1, 0)
B = (-2, 0, 1)
PI = (2, -1, 0)
E = (13, -10, 4)  # 57/(5+2a)
D = ((1, 2, 1), (0, 4, 4), (16, 0, -4))


def add(x, y):
    return tuple(i + j for i, j in zip(x, y))


def scale(x, n):
    return tuple(n * i for i in x)


def sub(x, y):
    return add(x, scale(y, -1))


def mul(x, y):
    a, b, c = x
    d, e, f = y
    c3 = b*f + c*e
    c4 = c*f
    return a*d-c3, a*e+b*d+3*c3-c4, a*f+b*e+c*d+3*c4


def mod(x, n):
    return tuple(i % n for i in x)


def conjugate(x):
    return add(add(scale(ONE, x[0]), scale(B, x[1])), scale(mul(B, B), x[2]))


def unit_classes():
    units = [x for x in product(range(8), repeat=3) if any(mod(x, 2))]
    squares = {mod(mul(x, x), 8) for x in units}
    classes = {}
    for x in units:
        if x not in classes:
            coset = [mod(mul(x, z), 8) for z in squares]
            classes.update((u, min(coset)) for u in coset)
    assert (len(units), len(squares), len(set(classes.values()))) == (448, 28, 16)
    return classes


UNITS = unit_classes()
ROOT_OFFSETS = [mul(E, d) for d in D]


def check_small_kernels_and_density():
    pairs = [(u, v) for u, v in product(range(8), repeat=2) if u % 2 or v % 2]
    residues = [UNITS[mod((u*u + v*v, -u*v, 0), 8)] for u, v in pairs]
    data = [(19, (1, 1, 1), [0, 0, 0]), (37, (1, -1, 2), [0, 0, 0]),
            (57, (5, 2, 0), [16, 0, 0]), (73, (5, -2, 0), [16, 0, 0]),
            (111, mul(PI, (1, -1, 2)), [0, 0, 0])]
    for kernel, beta, expected in data:
        conjugates = [beta, conjugate(beta), conjugate(conjugate(beta))]
        assert mul(mul(*conjugates[:2]), conjugates[2]) == scale(ONE, kernel)
        counts = [residues.count(UNITS[mod(u, 8)]) for u in conjugates]
        assert counts == expected
        if counts[0]:
            assert {u*v % 8 for (u, v), c in zip(pairs, residues)
                    if c == UNITS[mod(beta, 8)]} == {2, 6}
        print(f'Kernel {kernel}: conjugate cover counts {counts}')
    possible = set(residues)
    orbit = {UNITS[mod(v, 8)] for u in possible
             for v in (u, conjugate(u), conjugate(conjugate(u)))}
    joint = Counter((u in orbit, UNITS[mod(mul(PI, u), 8)] in orbit) for u in set(UNITS.values()))
    assert (len(possible), len(orbit)) == (5, 7)
    assert joint == {(False, False): 6, (True, False): 3, (False, True): 3, (True, True): 4}
    print('Ray classes by joint acceptance of p and 3p', dict(sorted(joint.items())))


@cache
def local_class(x, place):
    """place = (residue characteristic, root of g mod p if split)."""
    p, root = place
    assert any(x)
    valuation = 0
    if p == 2:
        while not any(mod(x, 2)):
            x = tuple(i // 2 for i in x)
            valuation += 1
        return valuation % 2, UNITS[mod(x, 8)]
    if p == 3:
        while (x[0] + 2*x[1] + 4*x[2]) % 3 == 0:
            numerator = mul(x, (1, 2, 1))  # divide by 2-a = 3/(1+a)^2
            assert not any(mod(numerator, 3))
            x = tuple(i // 3 for i in numerator)
            valuation += 1
        return valuation % 2, (x[0] + 2*x[1] + 4*x[2]) % 3
    assert p == 19 and root in (3, 9)
    modulus = p
    while True:
        z = (x[0] + x[1]*root + x[2]*root*root) % modulus
        if z:
            while z % p == 0:
                z //= p
                valuation += 1
            return valuation % 2, pow(z, (p-1)//2, p)
        error = (root**3 - 3*root + 1) // modulus
        root += modulus * ((-error * pow(3*root*root-3, -1, p)) % p)
        modulus *= p


def multiply_classes(first, second, place):
    i, u = first
    j, v = second
    p, _ = place
    unit = UNITS[mod(mul(u, v), 8)] if p == 2 else u*v % p
    return (i+j) % 2, unit


def local_image(place):
    neutral = local_class(ONE, place)
    span = {(neutral, neutral)}
    xs = [scale(d, -1) for d in ROOT_OFFSETS[:2]]
    if place[0] == 2:
        xs += [(-5, -1, -5), (-4, -3, 1), (-4, 1, -3)]
    for x in xs:
        values = [add(x, d) for d in ROOT_OFFSETS]
        for i, v in enumerate(values):
            if not any(v):
                values[i] = mul(values[(i+1) % 3], values[(i+2) % 3])
                break
        assert local_class(mul(mul(values[0], values[1]), values[2]), place) == neutral
        u, v = [local_class(z, place) for z in values[:2]]
        span |= {(multiply_classes(c, u, place), multiply_classes(d, v, place))
                 for c, d in span}
    assert len(span) == (32 if place[0] == 2 else 4)
    return span


def check_rank():
    generators = [((-1, 0, 0), (-1, -1, -1)), (A, (1, 1, -1)), (B, (1, -1, 1)),
                  ((2, 0, 0), (1, 1, 1)), (PI, (1, 1, 1)),
                  ((1, -3, 3), (1, 1, 1)), ((19, -3, -6), (1, 1, 1))]
    places = [(3, None), (19, 3), (19, 9), (2, None)]
    classes = []
    for bits in product((0, 1), repeat=7):
        x, signs = ONE, (1, 1, 1)
        for bit, (generator, signature) in zip(bits, generators):
            if bit:
                x = mul(x, generator)
                signs = tuple(s*t for s, t in zip(signs, signature))
        classes.append((signs, *(local_class(x, place) for place in places)))
    pairs = list(product(classes, repeat=2))
    counts = [len(pairs)]
    pairs = [(x, y) for x, y in pairs
             if all((s, t) in ((1, 1), (-1, k)) for s, t, k in zip(x[0], y[0], (1, -1, 1)))]
    counts.append(len(pairs))
    for i, place in enumerate(places, 1):
        image = local_image(place)
        pairs = [(x, y) for x, y in pairs if (x[i], y[i]) in image]
        counts.append(len(pairs))
    assert counts == [16384, 2048, 512, 128, 32, 8]
    print('Global Kummer pairs after successive constraints', counts)


def check_disks():
    def quotient(x, y):
        # A unit of Z[a]/25 has exponent dividing 5*(125-1).
        assert any(mod(y, 5))
        power, base = ONE, mod(y, 25)
        exponent = 5*124 - 1
        while exponent:
            if exponent % 2:
                power = mod(mul(power, base), 25)
            base = mod(mul(base, base), 25)
            exponent //= 2
        return mod(mul(x, power), 25)

    a2 = add(add(ROOT_OFFSETS[0], ROOT_OFFSETS[1]), ROOT_OFFSETS[2])
    a4 = add(add(mul(ROOT_OFFSETS[0], ROOT_OFFSETS[1]), mul(ROOT_OFFSETS[1], ROOT_OFFSETS[2])),
             mul(ROOT_OFFSETS[2], ROOT_OFFSETS[0]))
    he = scale(ROOT_OFFSETS[0], 4)
    p = quotient(scale(he, -2), scale(ONE, 9)), quotient(mul(he, E), scale(ONE, 27))

    def add_points(first, second):
        x, y = first
        u, v = second
        if first == second:
            m = quotient(add(add(scale(mul(x, x), 3), scale(mul(a2, x), 2)), a4), scale(y, 2))
        else:
            m = quotient(sub(v, y), sub(u, x))
        new_x = mod(sub(sub(sub(mul(m, m), a2), x), u), 25)
        return new_x, mod(sub(mul(m, sub(x, new_x)), y), 25)

    sixteen = p
    for _ in range(4):
        sixteen = add_points(sixteen, sixteen)
    fifteen = add_points(sixteen, (p[0], mod(scale(p[1], -1), 25)))
    dx = mod(sub(sixteen[0], fifteen[0]), 25)
    dy = mod(sub(sixteen[1], fifteen[1]), 25)
    assert not any(mod(dx, 5)) and any(mod(dy, 5))
    # The slope of 15P+16P is dy/dx. In the formal group -X/Y starts with dx/dy.
    w = mod(quotient(tuple(i//5 for i in dx), dy), 5)
    at_o = mod(mul(he, mul(w, w)), 5)
    at_p = mod(quotient(mul(scale(E, -3), w), scale(ONE, 2)), 5)
    assert (w, at_o, at_p) == ((4, 3, 1), (4, 3, 4), (0, 1, 1))
    print('Formal direction and initial residues at O and +P', w, at_o, at_p)


if __name__ == '__main__':
    check_small_kernels_and_density()
    check_rank()
    check_disks()

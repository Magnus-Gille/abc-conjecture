"""Finite arithmetic for the full 2-descent and 3-adic disk test at index 7.

Run directly with Python 3. Elements are coefficient triples in the integral
basis 1,a,a^2 for a^3+a^2-2a-1=0. The accompanying note proves that the
local generators and the finite global squareclass list are exhaustive.
"""

from itertools import product


ONE = (1, 0, 0)
A = (0, 1, 0)
D = ((4, 3, 1), (4, 4, 4), (16, 0, -4))


def add(x, y):
    return tuple(i + j for i, j in zip(x, y))


def scale(x, n):
    return tuple(n * i for i in x)


def sub(x, y):
    return add(x, scale(y, -1))


def mul(x, y):
    i, j, k = x
    l, m, n = y
    c3 = j * n + k * m
    c4 = k * n
    return (i * l + c3 - c4, i * m + j * l + 2 * c3 - c4,
            i * n + j * m + k * l - c3 + 3 * c4)


def mod(x, n):
    return tuple(i % n for i in x)


def powmod(x, exponent, modulus):
    result = ONE
    while exponent:
        if exponent % 2:
            result = mod(mul(result, x), modulus)
        x = mod(mul(x, x), modulus)
        exponent //= 2
    return result


def unit_classes_2():
    units = [x for x in product(range(8), repeat=3) if any(mod(x, 2))]
    squares = {mod(mul(x, x), 8) for x in units}
    classes = {}
    for x in units:
        if x not in classes:
            coset = [mod(mul(x, y), 8) for y in squares]
            representative = min(coset)
            classes.update((y, representative) for y in coset)
    assert len(squares) == 28 and len(set(classes.values())) == 16
    return classes


UNITS_2 = unit_classes_2()


def class_2(x):
    assert any(x)
    valuation = 0
    while not any(mod(x, 2)):
        x = tuple(i // 2 for i in x)
        valuation += 1
    return valuation % 2, UNITS_2[mod(x, 8)]


def class_7(x):
    assert any(x)
    valuation = 0
    residue = x[0] + 2 * x[1] + 4 * x[2]
    while residue % 7 == 0:
        # 1/(2-a) = D[0]/7.
        numerator = mul(x, D[0])
        assert not any(mod(numerator, 7))
        x = tuple(i // 7 for i in numerator)
        valuation += 1
        residue = x[0] + 2 * x[1] + 4 * x[2]
    return valuation % 2, pow(residue, 3, 7)


def local_image(prime, classify, xs):
    neutral = classify(ONE)
    span = {(neutral, neutral)}

    def multiply_classes(first, second):
        v, u = first
        w, t = second
        unit = UNITS_2[mod(mul(u, t), 8)] if prime == 2 else u * t % 7
        return (v + w) % 2, unit

    for x in xs:
        values = [add(x, d) for d in D]
        for i in range(3):
            if not any(values[i]):
                values[i] = mul(values[(i + 1) % 3], values[(i + 2) % 3])
                break
        assert classify(mul(mul(values[0], values[1]), values[2])) == neutral
        u, v = map(classify, values[:2])
        span |= {(multiply_classes(c, u), multiply_classes(d, v)) for c, d in span}
    return span


def check_descent():
    torsion_x = [scale(d, -1) for d in D[:2]]
    at_7 = local_image(7, class_7, torsion_x)
    at_2 = local_image(2, class_2, torsion_x + [(0, 0, -2), (0, 0, 2), (1, -1, 0)])
    assert (len(at_7), len(at_2)) == (4, 32)
    # The three ordered embeddings send a to the positive, middle, negative root.
    generators = [(scale(ONE, -1), (-1, -1, -1)), (A, (1, -1, -1)),
                  ((-2, 0, 1), (-1, -1, 1)), ((2, 0, 0), (1, 1, 1)),
                  ((2, -1, 0), (1, 1, 1))]
    classes = []
    for bits in product((0, 1), repeat=5):
        x = ONE
        signs = (1, 1, 1)
        for bit, (generator, signature) in zip(bits, generators):
            if bit:
                x = mul(x, generator)
                signs = tuple(s * t for s, t in zip(signs, signature))
        classes.append((signs, class_7(x), class_2(x)))

    def real_allowed(pair):
        signs_1, signs_2 = pair[0][0], pair[1][0]
        return all((s, t) in [(1, 1), (-1, sign_at_second_root)]
                   for s, t, sign_at_second_root in zip(signs_1, signs_2, (1, -1, 1)))

    pairs = list(product(classes, repeat=2))
    real = list(filter(real_allowed, pairs))
    seven = [(u, v) for u, v in real if (u[1], v[1]) in at_7]
    two = [(u, v) for u, v in seven if (u[2], v[2]) in at_2]
    counts = [len(s) for s in (pairs, real, seven, two)]
    assert counts == [1024, 128, 32, 8]
    print('Global squareclass pairs, then real, 7-adic and 2-adic survivors', counts)


def check_disks():
    # Work modulo 9. Unit inversion uses the exponent 3*(27-1) of the unit group.
    def quotient(x, y, n):
        assert any(mod(y, 3))
        return mod(mul(x, powmod(y, 77, 9)), n)

    B = add(add(D[0], D[1]), D[2])
    C = add(add(mul(D[0], D[1]), mul(D[0], D[2])), mul(D[1], D[2]))
    h = scale(D[0], 4)

    def derivative(x):
        return add(add(scale(mul(x, x), 3), scale(mul(B, x), 2)), C)

    def double(x, y):
        m = quotient(derivative(x), scale(y, 2), 9)
        new_x = mod(sub(sub(mul(m, m), B), scale(x, 2)), 9)
        return new_x, mod(sub(mul(m, sub(x, new_x)), y), 9)

    x2, y2 = double((0, 0, 0), h)
    x4, y4 = double(x2, y2)
    assert mod(x4, 3) == mod(scale(D[0], -1), 3) and not any(mod(y4, 3))
    w = quotient(scale(tuple(c // 3 for c in y4), 2), derivative(x4), 3)
    assert w == (1, 2, 1)
    w2 = mul(w, w)
    at_o = mod(mul(h, w2), 3)
    at_p = mod(scale(w, 2), 3)
    diff = mul(sub(D[1], D[0]), sub(D[2], D[0]))
    at_t = quotient(scale(mul(mul(h, diff), w2), -1), mul(D[0], D[0]), 3)
    assert all(any(v[1:]) for v in (at_o, at_p, at_t))
    print('3-adic direction w and coefficients at O, +P and T', w, at_o, at_p, at_t)


if __name__ == '__main__':
    check_descent()
    check_disks()

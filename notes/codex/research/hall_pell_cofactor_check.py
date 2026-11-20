"""Verify the finite steps in the squarefree-cofactor bounds for A and B."""

from decimal import Decimal, getcontext
from fractions import Fraction
from math import isqrt


# Each row gives d, the shift of L_n, the norm, the reduced x-coordinate,
# the unit (a+b*sqrt(d))/h, and P,Q for the logarithm approximation.
CASES = [
    (269, 6, 20, 17, (13449, 820, 1),
     21473628162972426227039401319, 455156868552413661108046288950),
    (509, 6, 20, 23, (855627, 37925, 2),
     2621637617279832424443039265, 74417320240643374127076896746),
    (395, 9, 5, 20, (159, 8, 1),
     2310477234192820976949282895, 27665707699958778260603549634),
]


def sieve(shift, norm, limit, moduli):
    remaining = [
        (d, j) for d in range(1, limit + 1)
        if all(d % (s * s) for s in range(2, isqrt(d) + 1))
        for j in range(60)
    ]
    for q in moduli:
        a, b = 29 % q, 9349 % q
        residues = []
        for _ in range(60):
            residues.append(((a - shift) ** 2 - norm) % q)
            a, b = b, (322 * b - a) % q
        assert (a, b) == (29 % q, 9349 % q)
        squares = {s * s % q for s in range(q)}
        allowed = {d: {d * r % q for r in squares} for d in {k for k, _ in remaining}}
        remaining = [(d, j) for d, j in remaining if residues[j] in allowed[d]]
    return {d for d, _ in remaining}


def log_interval(a, b, d, h):
    """Enclose log((a+b sqrt(d))/h) at exact terminating decimal endpoints."""
    scale = 10 ** 80
    w = isqrt(d * scale ** 2)
    numerators = sorted([a * scale + b * w, a * scale + b * (w + 1)])
    lo, hi = [Decimal(k) / Decimal(h * scale) for k in numerators]
    # All divisions above terminate exactly at this precision (h is 1 or 2).
    assert Fraction(lo) == Fraction(numerators[0], h * scale)
    assert Fraction(hi) == Fraction(numerators[1], h * scale)
    # Decimal.ln is correctly rounded. Widen by one representable value.
    return Fraction(lo.ln().next_minus()), Fraction(hi.ln().next_plus())


def divide_intervals(numerator, denominator):
    assert denominator[0] > 0
    endpoints = [x / y for x in numerator for y in denominator]
    return min(endpoints), max(endpoints)


def verify_orbit(d, norm, x0, unit):
    a, b, h = unit
    assert a * a - d * b * b == h * h
    assert h == 1 or (h == 2 and d % 4 == 1 and a % 2 == b % 2)
    # epsilon < 2*a/h. For 2*gamma = X+Y*sqrt(d), the normalization
    # in the proof gives |Y| <= sqrt(norm*epsilon/d).
    bound = isqrt((2 * norm * a) // (h * d))
    representatives = []
    for Y in range(-bound, bound + 1):
        X = isqrt(d * Y * Y + 4 * norm)
        if X * X - d * Y * Y == 4 * norm:
            representatives.append((X, Y))
    assert representatives == [(2 * x0, -2), (2 * x0, 2)]


def verify_approximation(d, x0, unit, p, q):
    a, b, h = unit
    log_unit = log_interval(a, b, d, h)
    tau = divide_intervals(log_interval(1, 1, 5, 2), log_unit)
    assert 0 < q < 10 ** 30
    assert max(abs(q * t - p) for t in tau) * 10 ** 25 < Fraction(1, 100)
    for sign in (-1, 1):
        shift = divide_intervals(log_interval(x0, sign, d, 2), log_unit)
        low, high = (q * x for x in shift)
        integer = low.numerator // low.denominator
        assert low - integer > Fraction(1, 10)
        assert high - integer < Fraction(9, 10)


def main():
    assert sieve(6, 20, 509, [3, 5, 8, 11, 17, 19, 41, 61]) == {269, 509}
    assert sieve(9, 5, 395, [3, 7, 8, 23, 25]) == {395}
    getcontext().prec = 110
    lucas = [2, 1]
    for _ in range(2, 160):
        lucas.append(lucas[-2] + lucas[-1])
    hits = []
    for d, shift, norm, x0, unit, p, q in CASES:
        verify_orbit(d, norm, x0, unit)
        verify_approximation(d, x0, unit, p, q)
        for n in range(7, 160, 12):
            value = (lucas[n] - shift) ** 2 - norm
            if d * isqrt(value // d) ** 2 == value:
                hits.append((n, d))
    assert 8 ** 160 > 267 * 10 ** 30 * 5 ** 160
    assert hits == [(7, 509), (7, 395)]
    print("Surviving (n, squarefree cofactor) pairs:", hits)


if __name__ == "__main__":
    main()

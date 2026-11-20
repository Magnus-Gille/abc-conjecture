"""Certify different signed log-skewness for all ten nonlinear target orbits."""

from flint import acb_poly, arb, ctx
from cypari import pari

from abc_pell_whole_trace import build


def rational_ball(q):
    return arb(int(q.numerator())) / int(q.denominator())


def orbit_skew(polynomial, root_two):
    coefficients = []
    for i in range(int(polynomial.poldegree()) + 1):
        coefficient = polynomial.polcoef(i).lift()
        rational = rational_ball(coefficient.polcoef(0, "y"))
        irrational = rational_ball(coefficient.polcoef(1, "y"))
        coefficients.append(rational + irrational * root_two)
    roots = acb_poly(coefficients).roots(tol=arb("1e-30"), maxprec=2048)
    assert len(roots) == len(coefficients) - 1
    lower, upper = -8-4*root_two, -8+4*root_two
    logs = [abs((upper-x)/(x-lower)).log() for x in roots]
    mean = sum(logs)/len(logs)
    variance = sum((x-mean)**2 for x in logs)/len(logs)
    assert variance > 0
    skew = sum((x-mean)**3 for x in logs)/(len(logs)*variance*variance.sqrt())
    assert skew.rad() < arb("1e-12")
    return len(logs), skew


def main():
    ctx.prec = 1024
    pari.allocatemem(128000000)
    real_quadratic = pari("nfinit(y^2-2)")
    root_two = arb(2).sqrt()
    support, _ = build()
    records = []
    for factor, exponent in support.factor()[1]:
        assert exponent == 1
        if factor.degree() == 1:
            continue
        polynomial = pari.Polrev([int(c) for c in factor.coeffs()])
        for orbit in pari.nffactor(real_quadratic, polynomial)[0]:
            records.append(orbit_skew(orbit, root_two))
    assert sorted(d for d, _ in records) == [10]*4 + [50]*4 + [121]*2
    for i, (degree, skew) in enumerate(records):
        assert all(not skew.overlaps(other) for _,other in records[:i])
        print(degree, str(skew.str(12)))


if __name__ == "__main__":
    main()

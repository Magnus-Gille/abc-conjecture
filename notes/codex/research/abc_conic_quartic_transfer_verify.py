"""Exact finite computations for the quartic conic-transfer obstruction."""
from itertools import combinations_with_replacement, product

import sympy as sp


def branch_signatures():
    weights = {"-": 0, "S": 1, "H": 2, "T": 2, "Q": 3}
    pairs = list(combinations_with_replacement(weights, 2))
    signatures = set()
    for rational, quadratic in product(pairs, repeat=2):
        cycles = rational + quadratic * 2
        if sum(weights[cycle] for cycle in cycles) != 6:
            continue
        if cycles.count("H") + cycles.count("Q") <= 1:
            signatures.add(("".join(rational), "".join(quadratic)))
    assert signatures == {
        ("--", "ST"), ("-H", "-T"), ("-H", "SS"), ("-T", "-T"),
        ("-T", "SS"), ("SS", "-T"), ("SS", "SS"), ("SQ", "-S"),
        ("HT", "-S"), ("TT", "-S"),
    }


def critical_values():
    x, u, t = sp.symbols("x u t")
    first = sp.resultant(3*x**2-(4*u+2)*x+3*u, x**3*(x-1)-t*(x-u), x)
    first = sp.cancel(first / (-u*(u-1)))
    assert sp.expand(first - 27*t**2 - (-256*u**3+192*u**2+6*u+4)*t-27*u**2) == 0
    assert not sp.polys.polytools.ground_roots(128*u**3-96*u**2-3*u-2, u)
    second = sp.resultant(3*x**2-(4*u+1)*x+2*u, x**2*(x-1)**2-t*(x-u), x)
    linear = sp.Poly(second, t).nth(1)
    assert sp.expand(linear - 4*u*(u-1)*(2*u-1)*(32*u**2-32*u-1)) == 0


def quartic_discriminant():
    z, t, r, v = sp.symbols("z t r v")
    disc = sp.Poly(sp.discriminant(z**4+z**3+r*z**2+t*z+v, z), t).monic()
    center = sp.factor(-disc.nth(3)/4)
    assert sp.expand(center-(9*r-2)/54) == 0
    depressed = sp.Poly(disc.as_expr().subs(t, t+center), t)
    result = sp.resultant(depressed.nth(2), depressed.nth(1), v)
    expected = 995328*r**6-1492992*r**5+839808*r**4-237600*r**3+38115*r**2-3696*r+188
    assert sp.cancel(result/expected) == sp.Rational(4, 1594323)
    assert all(expected.subs(r,i)%5 for i in range(5))
    a, c, e = sp.symbols("a c e", nonzero=True)
    symmetric = sp.Poly(sp.discriminant(a*z**4+c*z**2+t*z+e,z),t).monic()
    assert symmetric.nth(3)==symmetric.nth(1)==0
    assert sp.expand(symmetric.nth(2)-4*c*(c**2-36*a*e)/(27*a))==0


def jacobian_point_counts():
    p = 7
    # A pair represents a+bi in F_49, where i^2=-1.
    def multiply(z, w):
        a,b=z
        c,d=w
        return ((a*c-b*d)%p, (a*d+b*c)%p)
    field = list(product(range(p), repeat=2))
    squares = {multiply(y,y) for y in field}
    counts = []
    for elements in ([(a,0) for a in range(p)], field):
        local_squares = {multiply(y,y) for y in elements}
        count = 1
        for x in elements:
            xx = multiply(x,x)
            fourth = multiply(xx,xx)
            value = multiply(x,((fourth[0]-4)%p,fourth[1]))
            count += int(value==(0,0)) + 2*int(value in local_squares and value!=(0,0))
        counts.append(count)
    assert len(squares)==25 and counts==[8,78]
    trace = p+1-counts[0]
    second = (trace**2-(p*p+1-counts[1]))//2
    assert (trace,second)==(0,14)


if __name__ == "__main__":
    branch_signatures()
    critical_values()
    quartic_discriminant()
    jacobian_point_counts()
    print("Verified all ten signatures, critical values, discriminant and finite-field counts.")

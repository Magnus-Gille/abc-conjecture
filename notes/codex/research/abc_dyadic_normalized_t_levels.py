"""Verify the fixed Frey traces and exact Hecke calculation for t_n/17."""

from collections import Counter
from itertools import product
from math import gcd

try:
    from cypari import pari
except ImportError:
    from cypari2 import Pari
    pari = Pari()


def abscissas(p):
    x = 31**2 * pow(14, -2, p) % p if 14 % p else None
    orbit = []
    while x not in orbit:
        orbit.append(x)
        if x is None:
            continue
        denominator = 4*x*(x*x+16*x+32) % p
        x = (x*x-32)**2 * pow(denominator, -1, p) % p if denominator else None
    return orbit


def split_trace(p, A, B):
    assert (B*B*(A*A-4*B)) % p
    squares = {x*x % p for x in range(1,p)}
    trace = 0
    for x in range(p):
        rhs = x*(x*x+A*x+B) % p
        if rhs:
            trace += -1 if rhs in squares else 1
    return trace


def inert_trace(p, h):
    # The norm of an element has the same quadratic character in F_p as the element in F_{p^2}.
    squares = {x*x % p for x in range(1,p)}
    assert 2 not in squares

    def mult(x, y):
        a,b = x
        c,d = y
        return (a*c+2*b*d) % p, (a*d+b*c) % p

    trace = 0
    for x in product(range(p), repeat=2):
        # RHS = x*(x^2 + 4*s*x + (4+s*(h+4))).
        u,v = mult(x,x)
        a,b = mult(x, (u+8*x[1]+4, v+4*x[0]+h+4))
        norm = (a*a-2*b*b) % p
        if norm:
            trace += -1 if norm in squares else 1
    return trace


def fixed_traces():
    for p, target in [(3,-2), (5,0), (7,0), (23,16), (31,0), (47,144)]:
        roots = [s for s in range(p) if s*s % p == 2]
        for x in abscissas(p):
            if x in (None,0):
                assert roots
                assert all(split_trace(p,0,s)**2 == target for s in roots)
                continue
            h = (x*x+16*x+32)*pow(4*x,-1,p) % p
            if roots:
                assert all(split_trace(p,4*s,s*(h+4+2*s))**2 == target for s in roots)
            else:
                assert h == 1 and (h*h+8*h+8) % p  # g*g_sigma, divided by b^4
                assert inert_trace(p,h)-2*p == target


def exact_kernels():
    pari.allocatemem(2_500_000_000, silent=True)
    pari('M=mfinit([17408,2,8],0)')
    assert int(pari('mfdim(M)')) == 512
    pari('H=mfheckemat(M,3);V=matker(H^2+2)')
    assert int(pari('matsize(V)[2]')) == 20
    for p, dimension in [(5,4), (7,0)]:
        pari(f'H=mfheckemat(M,{p});V=V*matker(H*V)')
        assert int(pari('matsize(V)[2]')) == dimension


def determinant_gcd():
    pari.allocatemem(4_000_000_000, silent=True)
    pari('M=mfinit([17408,2,8],0)')
    assert int(pari('mfdim(M)')) == 512
    pari('H3=mfheckemat(M,3);Z=(H3^2+2)^2')
    pari('H5=mfheckemat(M,5);V=-H5^2')
    pari('H7=mfheckemat(M,7);W=H7^2')
    first = int(pari('matdet(Z+V+W)'))
    second = int(pari('matdet(Z+2*V+3*W)'))
    assert first > 0 and second > 0
    assert gcd(first,second) == 2**364*3**28*5**4*7**28*11**4*71**4*83**4*97**4


def small_exponents():
    from abc_dyadic_t_simple_cover import allowed
    for q,p in ((2,7),(3,7),(5,31),(7,127),(11,199),(17,103),(23,47),(31,9239),
                (47,473479),(71,2273),(83,6143),(97,11447)):
        bits, _, _ = allowed(q,p)
        assert not any(bits)


def newform_norms():
    pari.allocatemem(3_000_000_000, silent=True)
    space = pari.mfinit([17408,2,8],0)
    assert int(pari.mfdim(space)) == 512
    rows = Counter()
    for form in pari.mfeigenbasis(space):
        c = pari.mfcoefs(form,47)
        constraints = (c[7], c[23]**2-16, c[31], c[47]**2-144)
        common = gcd(*(abs(int(value.norm())) for value in constraints))
        assert common > 0 and common & (common-1) == 0
        degree = int(pari.mfparams(form)[3].poldegree())
        rows[degree, common.bit_length()-1] += 1
    expected = {
        (2,2):8, (2,4):2, (4,2):2, (8,2):5, (12,6):1,
        (16,10):2, (20,8):1, (24,4):2, (30,10):2, (32,12):2,
        (40,20):2, (64,24):1, (64,28):1,
    }
    assert rows == expected
    assert sum(rows.values()) == 31
    assert sum(degree*n for (degree,e),n in rows.items()) == 512


if __name__ == '__main__':
    import sys
    fixed_traces()
    small_exponents()
    if '--kernels' in sys.argv:
        exact_kernels()
    elif '--determinants' in sys.argv:
        determinant_gcd()
    else:
        newform_norms()
    print('All selected normalized t checks passed.')

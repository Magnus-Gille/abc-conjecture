"""Independent trace, full Hecke-space, and modular-character check for s and t."""

from itertools import product
from math import gcd, isqrt

try:
    from cypari import pari
except ImportError:
    from cypari2 import Pari
    pari = Pari()


def point_count_trace(p, A, B):
    squares = {x*x % p for x in range(1, p)}
    tr = 0
    for x in range(p):
        value = x*(x*x+A*x+B) % p
        if value:
            tr += -1 if value in squares else 1
    return tr


def inert_trace(p, coefficient):
    # Fp[tau] with tau^2=-2; the quadratic character equals that of the norm.
    def multiply(left, right):
        x, y = left
        u, v = right
        return (x*u-2*y*v) % p, (x*v+y*u) % p

    squares = {x*x % p for x in range(1, p)}
    assert (-2) % p not in squares
    tr = 0
    for x, y in product(range(p), repeat=2):
        first, second = multiply((x,y), (x,y))
        a, b = multiply((x,y), ((first+4*x+2) % p, (second+4*y+coefficient) % p))
        norm = (a*a+2*b*b) % p
        if norm:
            tr += -1 if norm in squares else 1
    return tr


def traces():
    for s in (7, 40):
        assert s*s % 47 == 2
        assert point_count_trace(47, 4*s, s*(24+4+2*s)) == 12
    assert inert_trace(47, 8) == inert_trace(47, -8) == 4
    assert point_count_trace(31, 4, 2) == 0
    assert inert_trace(31, 0) == -62

    pari.allocatemem(160_000_000, silent=True)
    pari('M=mfinit([1024,2,8],1); H=mfheckemat(M,47)')
    assert int(pari('mfdim(M)')) == 104
    assert bool(pari('charpoly(H)==x^60*(x^2-64)^10*(x^2-128)^4*(x^2-96)^4*(x^4-64*x^2+512)^2'))
    target = 2**208*3**64*5**10*47**2
    assert abs(int(pari('matdet(H-12)'))) == abs(int(pari('matdet(H+12)'))) == target
    pari('M=mfinit([1024,2],1); H=mfheckemat(M,47)')
    assert int(pari('mfdim(M)')) == 105
    assert bool(pari('charpoly(H)==x^57*(x^2-64)^12*(x^2-128)^4*(x^2-96)^4*(x^4-64*x^2+512)^2'))
    assert int(pari('matdet(H^2-98)')) == -2**105*3**8*5**8*7**114*17**24*31**8
    pari('M=mfinit([512,2],1); H=mfheckemat(M,47)')
    assert int(pari('mfdim(M)')) == 49
    assert int(pari('matdet(H^2-98)')) == -2**49*3**4*5**4*7**66*17**12


def orbit(p, q, c):
    """All possible power classes of X+cY, X=u^2, Y=v^2, starting at n=8."""
    assert not any(p % d == 0 for d in range(2, isqrt(p) + 1))
    assert (p-1) % q == 0
    def chi(z):
        return pow(z % p, (p-1)//q, p)
    X, Y = 961 % p, 196 % p
    x = X*pow(Y,-1,p) % p if Y else None
    scale = chi(Y or X)
    allowed = []
    seen = {}
    while (x, scale) not in seen:
        seen[x, scale] = len(allowed)
        if x is None:
            allowed.append(scale == 1)
            scale = pow(scale, 4, p)
            continue
        allowed.append(scale*chi(x+c) % p in (0,1))
        num = (x*x-32)**2 % p
        den = 4*x*(x*x+16*x+32) % p
        scale = pow(scale,4,p)*chi(den or num) % p
        x = num*pow(den,-1,p) % p if den else None
    start = seen[x, scale]
    period = len(allowed)-start
    return allowed[:start], period, {j % period for j in range(start,len(allowed)) if allowed[j]}


def verify_characters():
    witnesses = {
        8: {2: (113,), 3: (7,), 5: (31,), 7: (113,), 17: (2687,), 31: (311,),
            47: (3761,2351), 1103: (132361,2207)},
        16: {2: (5,), 3: (7,), 5: (31,), 47: (283,8273)}
    }
    for c, exponent_data in witnesses.items():
        for q, places in exponent_data.items():
            rows = [orbit(p,q,c) for p in places]
            for j in range(max(len(initial) for initial,period,allowed in rows)):
                if all(initial[j] if j < len(initial) else j % period in allowed
                       for initial,period,allowed in rows):
                    assert (c,q,j) == (16,5,0)
                    assert 31**2 + 16*14**2 == 17*241 and 241 % 17
            for classes in product(*(allowed for initial,period,allowed in rows)):
                assert any((classes[i]-classes[j]) % gcd(rows[i][1],rows[j][1])
                           for i in range(len(rows)) for j in range(i))
    print('All finite modular traces, Hecke determinants, and residual power obstructions pass.')


if __name__ == '__main__':
    traces()
    verify_characters()

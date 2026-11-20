"""Certify the split-prime CM denominator formula modulo seven."""

from collections import Counter
from fractions import Fraction
from functools import cache
from math import gcd, isqrt

from abc_odd_rank_quartic_cutoff import denominator, full_packet, split_generator


def initial_values(curve_a, curve_b, x, y):
    b2, b4, b8 = 4*curve_a, 2*curve_b, -curve_b**2
    w3 = 3*x**4+b2*x**3+3*b4*x**2+b8
    w4 = 2*y*(2*x**6+b2*x**5+5*b4*x**4+10*b8*x**2+b2*b8*x+b4*b8)
    return 0, 1, 2*y, w3, w4


def certify_cycle(cycle, curve_a, curve_b, x, y, p=7):
    w = lambda n: cycle[n % len(cycle)]
    assert tuple(w(n) for n in range(5)) == tuple(v % p for v in initial_values(curve_a, curve_b, x, y))
    for n in range(len(cycle)):
        assert w(-n) == -w(n) % p
        assert w(2*n+1) == (w(n+2)*w(n)**3-w(n-1)*w(n+1)**3) % p
        assert (2*y*w(2*n)-w(n)*(w(n+2)*w(n-1)**2-w(n-2)*w(n+1)**2)) % p == 0
    return w, lambda n: (x*w(n)**2-w(n-1)*w(n+1)) % p


def exact_values(curve_a, curve_b, x, y):
    initial = initial_values(curve_a, curve_b, x, y)

    @cache
    def w(n):
        if n < 0:
            return -w(-n)
        if n <= 4:
            return initial[n]
        k = n//2
        if n % 2:
            return w(k+2)*w(k)**3-w(k-1)*w(k+1)**3
        numerator = w(k)*(w(k+2)*w(k-1)**2-w(k-2)*w(k+1)**2)
        assert numerator % (2*y) == 0
        return numerator//(2*y)

    return w, lambda n: x*w(n)**2-w(n-1)*w(n+1)


def main():
    P = (0,1,4,6,0,1,3,6)
    W = (0,1,2,4,0,6,6,6,0,4,2,1,0,6,5,3,0,1,1,1,0,3,5,6)
    wp, fp = certify_cycle(P, 4, 2, -2, 2)
    ww, fw = certify_cycle(W, -8, 8, 1, 1)
    rows = Counter()
    for a in range(24):
        for b in range(24):
            q = a*a+2*b*b
            if gcd(q,24) != 1:
                continue
            m = (2*fp(a)*ww(b)**2+fw(b)*wp(a)**2) % 7
            power = ((q-1)//2)**2+b*b
            c = wp(q)*pow(m*pow(2,power,7), -1, 7) % 7
            expected = {1: (1 if b%4==0 else 5), 11: 3, 17: (4 if b%4==0 else 6), 19: 6}
            assert c == expected[q%24]
            rows[q%24,c] += 1
    print('Residue class counts for (q mod 24, C mod 7):', sorted(rows.items()))

    wp, fp = exact_values(4, 2, -2, 2)
    ww, fw = exact_values(-8, 8, 1, 1)
    cycle_p = tuple(wp(i)%11 for i in range(45))
    cycle_w = tuple(ww(i)%11 for i in range(45))
    p11, f11 = certify_cycle(cycle_p, 4, 2, -2, 2, 11)
    w11, g11 = certify_cycle(cycle_w, -8, 8, 1, 1, 11)
    possible = {}
    for a in range(45):
        for b in range(45):
            q = a*a+2*b*b
            if gcd(q,45) != 1:
                continue
            m = (2*f11(a)*w11(b)**2+g11(b)*p11(a)**2) % 11
            e = (3*(q-1))**2+b*b  # 3 == 1/2 modulo 5
            square = p11(q)**2*pow(m*m*pow(4,e,11),-1,11) % 11
            possible.setdefault(q%45,set()).add(square)
    residues = sorted(q for q, squares in possible.items() if 1 not in squares)
    assert residues == [2,4,7,13,14,17,22,23,29,32,34,37,38,43]
    print('Split prime residues modulo 45 obstructing a fifth power:', residues)
    for q in (11,17,19,41,43,59,67,73,83,89,97,107,113,131,137,139):
        a, b = split_generator(q)
        m = 2*fp(a)*ww(b)**2+fw(b)*wp(a)**2
        h = Fraction((-1)**b*m, 2**((a*a-1)//2))
        c = Fraction(wp(q), 2**(((q-1)//2)**2+b*b)*m)
        assert h.denominator == 1 and c.denominator == 1
        assert c == int(full_packet(q)) and h*c == int(denominator(q))
    print('Both exact identities verified at 16 split prime indices from 11 through 139.')

    c11 = int(full_packet(11))
    assert c11 == 82633*1781803 and c11 % 82633**2 != 0
    assert all(82633 % j for j in range(2, isqrt(82633)+1))
    # Modulo 23 the division sequences have common period 2*(23**2-1).
    period = 1056
    a, b = 3, 97
    q = a*a+2*b*b
    assert gcd(q,period) == 1 and (a%96,b%96) == (3,1)
    m = (2*fp(a)*ww(b)**2+fw(b)*wp(a)**2) % 23
    power = ((q-1)//2)**2+b*b
    c = (wp(q%period) * pow(m*pow(2,power,23),-1,23)) % 23
    assert (q%period,m,c,c*c%23) == (875,4,14,12)
    print('The ray class (3,97) modulo 1056 gives C = 14 mod 23.')


if __name__ == '__main__':
    main()
